'''
Created on May 28, 2011

@author: Carsten Witzke
'''
import unittest
from de.staticline.tests.dummytests import DummyClassificatorTestCase
from de.staticline.tests.libsvmtoolstests import DataFetchTestCase
from de.staticline.tests.kerneltests import KernelTestCase
from de.staticline.tests.regressiontests import RidgeRegressionTestCase

if __name__ == '__main__':
    suite = unittest.makeSuite(DummyClassificatorTestCase, 'test')
    suite = unittest.makeSuite(DataFetchTestCase, 'test')
    suite = unittest.makeSuite(KernelTestCase, 'test')
    suite = unittest.makeSuite(RidgeRegressionTestCase, 'test')
