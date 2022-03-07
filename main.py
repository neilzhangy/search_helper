# -*- coding: utf-8 -*-

import os
import sys
import argparse
import re
from openpyxl import load_workbook
from openpyxl import Workbook


def DebugLog(*msgs):
    if True:
        print('[DEBUG]: ', msgs)


def GetArgs():
    parser = argparse.ArgumentParser(description='Search from Google, translate to chinese and write results to excel.')

    parser.add_argument('--keyword', dest='key_word', required=False,
                        help='Key words for Google search.')
    parser.add_argument('--file', dest='file_name',
                        help='File name of excel to save result.')
    parser.add_argument('--translate', dest='translate', type=bool,
                        help='If translate to Chinese.')
    
    args = parser.parse_args()
    return args


def GetSearchResults(key_word):
    pass

def Translate(results):
    pass

def WriteExcel(file_name, results):
    pass

if __name__ == '__main__':
    args = GetArgs()
    if args.key_word:
        results = GetSearchResults(args.key_word)
    if args.translate:
        results= Translate(results)
    if args.file_name:
        WriteToExcel(args.file_name, results)
    
    sys.exit(0)
