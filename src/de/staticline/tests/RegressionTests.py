'''
Created on May 6, 2011

@author: Carsten Witzke
'''
import unittest
from de.staticline.classification.Regression import RidgeRegression


class Test(unittest.TestCase):


    def testRidgePlay(self):
        RidgeRegression().play()
        #TODO: test case


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPlay']
    unittest.main()