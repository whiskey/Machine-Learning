'''
Created on May 21, 2011

@author: Carsten Witzke
'''
import numpy as np

#TODO: Python 'interfaces'?
#TODO: make kernel-Class for all kernels
#--> abstract base class: http://docs.python.org/library/abc.html
class Linear(object):
    '''linear kernel'''
    def __init__(self):
        pass
    
    def __repr__(self):
        return 'linear kernel.'
    
    def calc(self,v1,v2):
        if v2 == None: v2 = v1
        return np.dot(v1.T, v2)
    
    
class Polynomial(object):
    '''polynomial kernel of degree d'''
    __degree = 0
    
    def __init__(self, deg=2):
        self.__degree = deg
        
    def __repr__(self):
        return 'polynomial kernel of degree {degree}.'.format(degree=self.__degree)
        
    def calc(self,v1,v2=None):
        if v2 == None: v2 = v1
        return np.power(np.dot(v1.T, v2), self.__degree)

class RBF(object):
    '''radial basis kernel'''
    __gamma = 0
    
    def __init__(self, gamma=1):
        self.__gamma = gamma
    
    def __repr__(self):
        return 'radial basis kernel with gamma = {gamma}.'.format(gamma=self.__gamma)
        
    def calc(self,v1,v2=None):
        if v2 == None: v2 = v1
        l2 = np.linalg.norm(v1-v2)
        return np.exp(-self.__gamma * l2**2)


#### 'old' kernels ####
#def linear(v1, v2=None):
#    '''linear kernel'''
#    if v2 == None: v2 = v1
#    return np.dot(v1.T, v2)
#
#def poly(v1, v2=None, degree=2):
#    '''polynomial kernel of degree d'''
#    if v2 == None: v2 = v1
#    return np.power(np.dot(v1.T, v2), degree)
#
#def rbf(v1, v2=None, gamma=1):
#    '''radial basis kernel'''
#    if v2 == None: v2 = v1
#    l2 = np.linalg.norm(v1-v2)
#    return np.exp(-gamma * l2**2)