'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''

from numpy import *

class RidgeRegression(object):
    '''
    Ridge regression a.k.a. Tikhonov regularization
    '''

    def __init__(self):
        pass

    def trainModel(self, training):
        training = matrix(training)
        # means
        means = training.mean(0)
        # sum of squares
        print training
        print training - means
        
