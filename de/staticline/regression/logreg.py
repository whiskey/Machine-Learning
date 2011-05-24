'''
Created on May 23, 2011

@author: "Carsten Witzke"
'''

import numpy as np
from de.staticline.kernels import kernels
from de.staticline.tools.libsvmtools import DataSet


class LogisticRegression(object):
    def __init__(self):
        pass
    
    def trainModel(self, train):
        x = np.matrix(train.get_matrix())
        y = np.matrix(train.get_target())
        
        ones = np.ones((x.shape[0],1))
        x = np.concatenate((ones,x), axis=1)


if __name__ == '__main__':
    _x = np.matrix('1 1 2; 1 2 3; 1 4 1; 1 5 5')
    _y = np.matrix('3;2;7;1')
    trainSet = DataSet(max_f_index=3, x=_x, y=_y)