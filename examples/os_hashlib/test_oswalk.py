#!/usr/bin/env python

import os


def enumaratepaths(path):
    path_collection = []
    for dirpath,dirs,filenames in os.walk(path):
        for filename in filenames:
            fullpath = os.path.join(dirpath,filename)
            path_collection.append(fullpath)
    return path_collection

def enumaratefiles(path):
    file_collection = []
    for dirpath,dirs,filenames in os.walk(path):
        for filename in filenames:
            file_collection.append(filename)
    return file_collection

def enumaratedirs(path):
    dir_collection = []
    for dirpath,dirs,filenames in os.walk(path):
        for dir in dirs:
            dir_collection.append(dir)
    return dir_collection


if __name__ == '__main__':
    for dir in enumaratedirs('/data/wwwroot'):
        print dir
