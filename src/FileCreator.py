# -*- coding: utf-8 -*-
"""
Created on Tue May 18 20:01:00 2018

@author: Ezequiel
"""


class FileCreator:

    def __init__(self, directory, name_file, content):
        directory = directory + name_file
        f = open(directory, "w+")
        f.write(content)



