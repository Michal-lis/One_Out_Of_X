#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile

myfile = zipfile.ZipFile('s79 e01.odt')
listoffiles = myfile.infolist()
for s in listoffiles:
    if s.orig_filename == 'content.xml':
        fd = open('example.xml', 'wb')
        bh = myfile.read(s.orig_filename)
        fd.write(bh)
        fd.close()
