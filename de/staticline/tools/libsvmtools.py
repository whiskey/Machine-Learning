'''
Created on Apr 25, 2011

@author: Carsten Witzke
'''
from pydoc import deque
import os
import numpy

class LibsvmFileImporter(object):
    '''
    Imports files in LIBSVM format. Includes simple comment-handling.
    '''
    __file = None
    __dataSet = None
    
    def __init__(self, filename, binary=False):
        '''
        New file importer with file from given URL string
        '''
        try:
            self.__file = open(os.path.abspath(filename), 'r')
        except IOError:
            raise IOError('No such file \'%s\'' % filename)
        
        if binary:
            self.__read_binary_data()
        else:
            self.__read_data()

    def __read_data(self):
        '''reads (multi)labeled data'''
        dataList = []
        max_f_index = 0
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
                data_['target'] = float(tokens.popleft())
                for token in tokens:
                    t = token.split(':')
                    feature = int(t[0])
                    if feature > max_f_index:
                        max_f_index = feature
                    data_[feature] = float(t[1]) if '.' in t[1] else int(t[1])
                dataList.append(data_)
            except Exception as e:
                print e
        self.__dataSet = DataSet(dataList, max_f_index)
    
    def __read_binary_data(self):
        '''reads data and checks for binary classes'''
        targetList = []
        dataList = []
        max_f_index = 0
        for line in self.__file:
            # strip comments, whitespaces and line breaks
            line = line[:line.find('#')]
            line = line.strip('\n')
            line = line.strip()
            if line == '':
                continue
            
            # something left? go!
            data_ = {}
            tokens = deque(line.split(' '))
            data_['target'] = float(tokens.popleft())
            if len(targetList) <= 2:
                if data_['target'] not in targetList:
                    targetList.append(data_['target'])
            else:
                raise TypeError('Not a binary class file')
            for token in tokens:
                t = token.split(':')
                feature = int(t[0])
                if feature > max_f_index:
                    max_f_index = feature
                data_[feature] = float(t[1]) if '.' in t[1] else int(t[1])
            dataList.append(data_)
        self.__dataSet = DataSet(dataList, max_f_index)
    
    
    
    def get_dataSet(self):
        return self.__dataSet
    

class DataSet(object):
    '''a data set'''
        
    def __init__(self, data=None, max_f_index=None, x=None, y=None):#TODO: handle max_f_index internally!
        if x != None and y != None:
            self.__matrix = x
            self.__target = y
            self.__numInstances, self.__numFeatures = self.__matrix.shape
            return
        self.__data = data
        self.__build_matrix(max_f_index)
        self.__numInstances, self.__numFeatures = self.__matrix.shape
    
    def __build_matrix(self, max_f_index):
        self.__matrix = numpy.zeros(shape=(len(self.__data),len(range(max_f_index))+1))
        self.__target = numpy.zeros(shape=(len(self.__data),1))
        for i in range(len(self.__data)):
            for key, value in self.__data[i].iteritems():
                # ignore label
                if key == 'target': 
                    self.__matrix[i][0] = 1
                    self.__target[i] = value
                    continue
                self.__matrix[i][key] = value

    ## getter / setter ##
    def get_data(self):
        return self.__data
    
    def get_matrix(self):
        return self.__matrix
    
    def get_target(self,index=None):
        if index != None:
            return int(self.__target[index])
        return self.__target
        
    def get_numInstances(self):
        return self.__numInstances
    
    def get_numFeatures(self):
        return self.__numFeatures - 1
        
    ## properties
    data = property(get_data, doc='old data format: list of dictionaries')
    matrix = property(get_matrix, doc='feature vector X')
    target = property(get_target, doc='target vector Y')
    numInstances = property(get_numInstances)
    numFeatures = property(get_numFeatures)