'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''
import unittest
from de.staticline.classification.Dummys import Always1Predictor


class Test(unittest.TestCase):


    def testDummyModel(self):
        dummy = Always1Predictor()
        dummy.buildClassifier('../../../../data/a1a')
        dummy.validateModel('../../../../data/a1a.t')
        self.assertTrue(dummy.get_pctCorrect() > 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()