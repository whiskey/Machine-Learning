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
        pass


if __name__ == '__main__':
    #debug
    _x = np.array('1 1 2; 1 2 3; 1 4 1; 1 5 5')
    _y = np.array('3;2;7;1')
    trainSet = DataSet(max_f_index=3, x=_x, y=_y)