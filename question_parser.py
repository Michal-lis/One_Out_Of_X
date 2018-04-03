#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
import zipfile
import os, sys
from pprint import pprint

namespace_dict = {'body': '{urn:oasis:names:tc:opendocument:xmlns:office:1.0}body',
                  'text': '{urn:oasis:names:tc:opendocument:xmlns:office:1.0}text',
                  'p': '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p',
                  'name': '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name',
                  'span': '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}span'}

dict_to_db = imdict


class imdict(dict):
    def __hash__(self):
        return id(self)

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    update = _immutable
    setdefault = _immutable
    pop = _immutable
    popitem = _immutable


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
        # root to cały xml jako string
        root = self.m_odf.read('content.xml').decode('utf-8')
        root = et.fromstring(root)
        body = root.find(namespace_dict['body'])
        text = body.find(namespace_dict['text'])
        title = text.find(namespace_dict['p']).text.split(' ')
        dict_to_db['series_number'] = title[3]
        dict_to_db['episode_number'] = title[1]
        questions = []
        stage = 0
        for child in text:
            # print(child.tag, child.attrib, child.text)
            if child.get(namespace_dict['name']) == 'P4':
                dict_to_db['answer'] = child.text
                print(dict_to_db['stage'], dict_to_db['question'], dict_to_db['answer'])
                questions.append(dict_to_db)
            if child.get(namespace_dict['name']) == 'P2':
                if child.text == 'Etap I':
                    stage = 1
                if child.text == 'Etap II':
                    stage = 2
                if child.text == 'Etap III':
                    stage = 3
            if child.get(namespace_dict['name']) == 'P3' and child.text is not None:
                dict_to_db['question'] = child.text
                dict_to_db['stage'] = stage
                if child.find(namespace_dict['span']):
                    dict_to_db['answer'] = child.find(namespace_dict['span'])[0].tail
                    # print(child.find(namespace_dict['span']).text)
                    print(dict_to_db['stage'], dict_to_db['question'], dict_to_db['answer'])
                    questions.append(dict_to_db)
                elif hasattr(child.find(namespace_dict['span']), 'text'):
                    dict_to_db['answer'] = child.find(namespace_dict['span']).text
                    print(dict_to_db['stage'], dict_to_db['question'], dict_to_db['answer'])
                    questions.append(dict_to_db)
                continue
                # słowiniki muatble więc wszystko się zmienia!
        print(questions)
        # SUMMARY
        print("Summary:")
        first_round = [question for question in questions if question['stage'] == 1]
        print('{} questions in the third round'.format(len(first_round)))
        second_round = [question for question in questions if question['stage'] == 2]
        print('{} questions in the third round'.format(len(second_round)))
        third_round = [question for question in questions if question['stage'] == 3]
        print('{} questions in the third round'.format(len(third_round)))


if __name__ == '__main__':
    # odt_name=input('Please give the odt name:')
    odt_name = 's79 e01.odt'
    odt = OdfReader(odt_name)
    odt.get_content()
