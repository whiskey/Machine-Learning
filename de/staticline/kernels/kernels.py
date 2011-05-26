'''
Created on May 21, 2011

@author: Carsten Witzke
'''
import numpy as np

def linear(v1, v2=None):
    '''linear kernel'''
    if v2 == None: v2 = v1
    return np.dot(v1.T, v2)

def poly(v1, v2=None, degree=2):
    '''polynomial kernel of degree d'''
    if v2 == None: v2 = v1
    return np.power(np.dot(v1.T, v2), degree) #TODO: add constant?

def rbf(v1, v2=None, gamma=1/10):
    '''radial basis kernel'''
    if v2 == None: v2 = v1
    l2 = np.linalg.norm(v1-v2)
    return np.exp(-gamma * l2**2)