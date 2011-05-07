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

    def trainModel(self, trainFile):
        pass
        
    def play(self):
        m = matrix('1 2 3; 4 5 6')
        m2 = matrix('2 2; 2 2')
        print m.transpose()
        print m.sort(0)