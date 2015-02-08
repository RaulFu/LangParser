'''
Created on Feb 8, 2015

@author: raul
'''
from parser.Parser import LangParser

if __name__ == '__main__':
    langParser = LangParser.instance()
    print langParser.getContent('format')