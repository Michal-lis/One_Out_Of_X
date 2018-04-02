#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import xml.etree.ElementTree as et
from pprint import pprint

odt_name = 's79 e01.odt'


def save_odt_to_xml(filename):
    myfile = zipfile.ZipFile(filename)
    listoffiles = myfile.infolist()
    for s in listoffiles:
        if s.orig_filename == 'content.xml':
            fd = open('example.xml', 'wb')
            bh = myfile.read(s.orig_filename)
            pprint(bh)
            fd.write(bh)
            fd.close()


def save_odt_to_database(filename):
    myfile = zipfile.ZipFile(filename)
    listoffiles = myfile.infolist()
    for s in listoffiles:
        if s.orig_filename == 'content.xml':
            bh = myfile.read(s.orig_filename)
            tree = et.parse(bh)
            root = tree.getroot()
            el = root.find('office')
            pprint(el)


if __name__ == '__main__':
    save_odt_to_database(odt_name)
