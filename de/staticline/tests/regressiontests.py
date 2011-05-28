'''
Created on May 6, 2011

@author: Carsten Witzke
'''

import numpy as np
import unittest
import sys, os
from de.staticline.regression.linreg import RidgeRegression
from de.staticline.tools.libsvmtools import DataSet, LibsvmFileImporter

class RidgeRegressionTestCase(unittest.TestCase):

    def testRidgeRegression(self):
        cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
        data = LibsvmFileImporter(os.path.join(cwd,'data/regression/lin_reg'), binary=False).get_dataSet()
        rr = RidgeRegression(5)
        rr.trainModel(data)
        #TODO: create test
        self.assertTrue(True)
        

if __name__ == "__main__":
    unittest.main()