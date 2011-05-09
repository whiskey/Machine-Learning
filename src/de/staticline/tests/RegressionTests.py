'''
Created on May 6, 2011

@author: Carsten Witzke
'''
import unittest
from numpy import *
from de.staticline.regression.SimpleRegression import RidgeRegression
from de.staticline.tools.LibsvmTools import DataSet

class Test(unittest.TestCase):

    def testRidgeRegression(self):
        _x = matrix('1 1 2; 1 2 3; 1 4 1; 1 5 5')
        _y = matrix('3;2;7;1')
        trainSet = DataSet(max_f_index=3, x=_x, y=_y)
        rr = RidgeRegression(5)
        rr.trainModel(trainSet)
        #TODO: implement test case
        print 'model:\n',rr.get_model()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPlay']
    unittest.main()