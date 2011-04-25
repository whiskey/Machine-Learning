'''
Created on Apr 25, 2011

@author: Carsten Witzke
'''
from pydoc import deque

class LibsvmFileImporter(object):
    '''
    classdocs
    '''
    __file = None
    __data = []
    
    def __init__(self, filename):
        '''
        New file importer with file from given URL string
        '''
        try:
            self.__file = open(filename, 'r')
            #self.__data = []
            self.__read_data()
        except IOError:
            raise IOError('No such file \'%s\'' % filename)

    def __read_data(self):
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
                self.__data.append(data_)
            except Exception as e:
                print line
                print e

            
    def get_data(self):
        return self.__data
