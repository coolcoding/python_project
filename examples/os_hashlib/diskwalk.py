#!/usr/bin/env python

import os

class diskwalk():
    def __init__(self,path):
        self.path = path


    def enumeratePaths(self):
        path_collection = []
        for dirpath,dirs,filenames in os.walk(self.path):
            for filename in filenames:
                fullpath = os.path.join(dirpath,filename)
                path_collection.append(fullpath)
        return path_collection



    def enumerateDirs(self):
        dir_collection = []
        for dirpath,dirs,filenames in os.walk(self.path):
            for dir in dirs:
                dir_collection.append(dir)
        return dir_collection


    def enumeratefiles(self):
        file_collection = []
        for dirpath,dirs,filenames in os.walk(self.path):
            for filename in filenames:
                file_collection.append(filename)
        return file_collection


