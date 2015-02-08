'''
Created on Feb 8, 2015

@author: raul
'''
import xml.dom.minidom
from xml.dom.minidom import Node

class LangParser():
    
    _instance = None
    
    def __init__(self, path):
        '''
        @param path: the path of the language file
        '''
        self.__initialize()
        self.__xmlPath = path
        self.__parseXml()
    
    def __initialize(self):
        '''
        All properties are here.
        '''
        self.__dom = None
        self.__lang = None
        self.__xmlPath = None
        self.__langDict = {}
    
    def __parseXml(self, lang='en'):
        self.__lang = lang
        self.__dom = xml.dom.minidom.parse(self.__xmlPath)
        collection = self.__dom.documentElement
        
        langNode = collection.getElementsByTagName(self.__lang)[0]
        for node in (langNode.childNodes):
            if node.nodeType == Node.ELEMENT_NODE:
                self.__langDict[node.nodeName] = node.childNodes[0].nodeValue
        
    def setLanguage(self, lang):
        self.__parseXml(lang)
    
    def getContent(self, name):
        return self.__langDict.get(name)
        
    @staticmethod
    def instance():
        if None == LangParser._instance:
            path = '../language/lang.xml'
            LangParser._instance = LangParser(path)
        
        return LangParser._instance
            
