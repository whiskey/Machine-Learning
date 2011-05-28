#!/usr/bin/python
'''
Created on May 22, 2011

@author: Carsten Witzke
'''
import unittest
import numpy as np
from de.staticline.kernels import kernels
from de.staticline.kernels.kernels import Linear, Polynomial, RBF

class KernelTestCase(unittest.TestCase):

    def setUp(self):
        self.a = np.array([1,2,3])
        self.b = np.array([-7,8,9])

    def tearDown(self):
        pass

    def testLinear(self):
        self.assertEqual(Linear().calc(self.a, self.b), 36)
    
    def testPoly(self):
        self.assertEqual(Polynomial(2).calc(self.a, self.b), 1296)
        
    def testRBF(self):
        #self.assertAlmostEqual(RBF(1/100).calc(self.a, self.b), 0.256660776954)
        for gamma in [0, 10, 10000, 1./1000, 1./100000]:
            self.assertTrue(RBF(gamma).calc(self.a, self.b) >= 0)
            self.assertTrue(RBF(gamma).calc(self.a, self.b) <= 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()