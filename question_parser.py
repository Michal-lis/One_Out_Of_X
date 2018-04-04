#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
import zipfile
import os
import simpledb_connection

from copy import deepcopy
from pprint import pprint

namespace_dict = {'body': '{urn:oasis:names:tc:opendocument:xmlns:office:1.0}body',
                  'text': '{urn:oasis:names:tc:opendocument:xmlns:office:1.0}text',
                  'p': '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p',
                  'name': '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name',
                  'span': '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span'}

dict_to_db = {}


class DatabaseQuestionsInput(list):
    def add(self, dict):
        dict_to_db = deepcopy(dict)
        self.append(dict_to_db)

    def present(self):
        pprint(self)

    def summary(self):
        print("Summary:")
        first_round = [question for question in self if question['stage'] == 1]
        print('{} questions in the third round'.format(len(first_round)))
        second_round = [question for question in self if question['stage'] == 2]
        print('{} questions in the third round'.format(len(second_round)))
        third_round = [question for question in self if question['stage'] == 3]
        print('{} questions in the third round'.format(len(third_round)))

    def clean(self):
        for row in self:
            if row['answer'] is None or row['question'] is None:
                self.remove(row)
        return self


class OdfReader():
    def __init__(self, filename):
        # open an ODF file
        self.filename = filename
        self.m_odf = zipfile.ZipFile(self.filename)
        self.filelist = self.m_odf.infolist()

    def save_to_xml(self):
        xml_name = self.filename.split('.')[0] + '.xml'
        fd = open(xml_name, 'wb')
        bh = self.m_odf.read('content.xml')
        fd.write(bh)
        fd.close()

    def show_manifest(self):
        for s in self.filelist:
            print(s.orig_filename)

    def get_content(self):
        # returning a list of dictionaries that can be put into a database
        root = self.m_odf.read('content.xml').decode('utf-8')
        root = et.fromstring(root)
        body = root.find(namespace_dict['body'])
        text = body.find(namespace_dict['text'])
        title = text.find(namespace_dict['p']).text.split(' ')
        questions = DatabaseQuestionsInput()
        stage = 0
        question_number = 1
        for child in text:
            dict_to_db['series_number'] = title[1]
            if len(title) >= 4:
                dict_to_db['episode_number'] = title[3]
            dict_to_db['done'] = '0'
            dict_to_db['question_number'] = str(question_number)
            question_number += 1
            if child.get(namespace_dict['name']) == 'P4':
                dict_to_db['answer'] = child.text
                print(dict_to_db['stage'], dict_to_db['question'], dict_to_db['answer'])
                questions.add(dict_to_db)

            if child.get(namespace_dict['name']) == 'P2':
                if child.text == 'Etap I':
                    stage = 1
                if child.text == 'Etap II':
                    stage = 2
                if child.text == 'Etap III':
                    stage = 3

            if child.get(namespace_dict['name']) == 'P3' and child.text is not None:
                # soft page break
                dict_to_db['question'] = child.text
                dict_to_db['stage'] = stage
                if child.find(namespace_dict['span']):
                    dict_to_db['answer'] = child.find(namespace_dict['span'])[0].tail
                    print(dict_to_db['stage'], dict_to_db['question'], dict_to_db['answer'])
                    questions.add(dict_to_db)
                elif hasattr(child.find(namespace_dict['span']), 'text'):
                    dict_to_db['answer'] = child.find(namespace_dict['span']).text
                    print(dict_to_db['stage'], dict_to_db['question'], dict_to_db['answer'])
                    questions.add(dict_to_db)
                continue
        questions.clean()
        questions.summary()
        questions.present()
        return questions


def get_odt_names():
    odt_list = []
    current_path = os.getcwd()
    path = current_path + '/questions'
    for filename in os.listdir(path):
        if not filename.endswith('.odt'):
            continue
        else:
            direct_path = 'questions/' + filename
            odt_list.append(direct_path)
    return odt_list


def insert_questions_into_db(conn, questions):
    conn.insert_questions(questions)
    conn.commit()


if __name__ == '__main__':
    odt_files_with_questions = get_odt_names()
    for odt_filename in odt_files_with_questions:
        odt = OdfReader(odt_filename)
        conn = simpledb_connection.DbConnection('questions.db')
        questions = odt.get_content()
        insert_questions_into_db(conn, questions)
        print("Successfully inserted questions into database.")
