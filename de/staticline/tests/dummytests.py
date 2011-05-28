#!/usr/bin/python
'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''
import unittest
from de.staticline.classification.dummys import Always1Predictor
import os
import sys


class DummyClassificatorTestCase(unittest.TestCase):

    def testDummyModel(self):
        cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
        
        dummy = Always1Predictor()
        dummy.buildClassifier(os.path.join(cwd,'data/classification/a1a'))
        dummy.validateModel(os.path.join(cwd,'data/classification/a1a.t'))
        self.assertTrue(dummy.get_pctCorrect() > 24) # for data set a1a !!!


if __name__ == "__main__":
    unittest.main()