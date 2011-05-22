'''
Created on May 21, 2011

@author: Carsten Witzke
'''
import numpy as np

def linear(v1, v2):
    '''linear kernel'''
    return np.dot(v1.T, v2)

def poly(v1, v2, degree):
    '''polynomial kernel of degree d'''
    return np.power(np.dot(v1.T, v2), degree) #TODO: add constant?

def rbf(v1, v2, gamma):
    '''radial basis kernel'''
    l2 = np.linalg.norm(v1-v2)
    return np.exp(-gamma * l2**2)