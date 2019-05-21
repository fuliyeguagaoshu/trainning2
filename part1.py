#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import sys
import csv




class Args(object):
    def __init__(self):
        self._args = sys.argv[1:]
        if len(self._args) != 6:
            print("Parameter Error")
            sys.exit()
        self._filelist = []
        try:
            self._index = self._args.index('-c')
            self._filelist.append(self._args[self._index+1])
            self._index = self._args.index('-d')
            self._filelist.append(self._args[self._index+1])
            self._index = self._args.index('-o')
            self._filelist.append(self._args[self._index+1])
        except:
            print("Parameter Error")
            sys.exit()
    def get_configfile(self):
        return self._filelist[0]
    def get_userdatafile(self):
        return self._filelist[1]
    def get_outputfile(self):
        return self._filelist[2]



if __name__ == '__main__':
    a = Args()
    print('configfile:  {0}\nuserdatafile:  {1}\noutputfile:  {2}'.format(a.get_configfile(),a.get_userdatafile(),a.get_outputfile()))
            





