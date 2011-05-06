'''
Created on Apr 25, 2011

@author: Carsten Witzke
'''
from pydoc import deque
import os

class LibsvmFileImporter(object):
    '''
    Imports files in LIBSVM format. Includes simple comment-handling.
    '''
    __file = None
    __dataSet = None
    
    def __init__(self, filename):
        '''
        New file importer with file from given URL string
        '''
        try:
            self.__file = open(os.path.abspath(filename), 'r')
            self.__read_data()
        except IOError:
            raise IOError('No such file \'%s\'' % filename)

    def __read_data(self):
        __dataList = []
        for line in self.__file:
            try:
                # strip comments, whitespaces and line breaks
                line = line[:line.find('#')]
                line = line.strip('\n')
                line = line.strip()
                if line == '':
                    continue
                
                # something left? go!
                data_ = {}
                tokens = deque(line.split(' '))
                data_['class'] = int(tokens.popleft())
                for token in tokens:
                    t = token.split(':')
                    data_[int(t[0])] = float(t[1]) if '.' in t[1] else int(t[1])
                __dataList.append(data_)
            except Exception as e:
                print line
                print e
        self.__dataSet = DataSet(__dataList)
        #print self.__dataSet.get_numInstances()
            
    def get_dataSet(self):
        return self.__dataSet
    

class DataSet(object):
    '''a data set'''
        
    def __init__(self, data):
        self.set_data(data)
        #self.data = data
    
    ## getter / setter ##
    def get_data(self):
        return self.__data

    def set_data(self, newData):
        self.__data = newData
        self.__set_numInstances(len(self.__data))
        
    def get_numInstances(self):
        return self.__numInstances
    
    def __set_numInstances(self, num):
        self.__numInstances = num
        
    ## properties
    data = property(get_data, set_data)
    numInstances = property(get_numInstances)