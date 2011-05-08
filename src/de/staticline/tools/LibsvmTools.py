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
                data_['class'] = int(tokens.popleft())
                for token in tokens:
                    t = token.split(':')
                    feature = int(t[0])
                    if feature > max_f_index:
                        max_f_index = feature
                    data_[feature] = float(t[1]) if '.' in t[1] else int(t[1])
                dataList.append(data_)
            except Exception as e:
                print line
                print e
        self.__dataSet = DataSet(dataList, max_f_index)
        #print self.__dataSet.get_numInstances()
            
    def get_dataSet(self):
        return self.__dataSet
    

class DataSet(object):
    '''a data set'''
        
    def __init__(self, data, max_f_index):
        self.__data = data
        self.__build_matrix(max_f_index)
        self.__numInstances, self.__numFeatures = self.__matrix.shape
    
    def __build_matrix(self, max_f_index):
        self.__matrix = numpy.zeros(shape=(len(self.__data),len(range(max_f_index))))
        for i in range(len(self.__data)):
            for key, value in self.__data[i].iteritems():
                # ignore label
                if key == 'class': continue
                self.__matrix[i][key-1] = value

    ## getter / setter ##
    def get_data(self):
        return self.__data
    
    def get_matrix(self):
        return self.__matrix
        
    def get_numInstances(self):
        return self.__numInstances
    
    def get_numFeatures(self):
        return self.__numFeatures
        
    ## properties
    data = property(get_data, doc='old data format: list of dictionaries')
    matrix = property(get_matrix, doc='numpy matrix')
    numInstances = property(get_numInstances)
    numFeatures = property(get_numFeatures)