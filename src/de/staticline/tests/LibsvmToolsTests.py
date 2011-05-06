'''
Created on Apr 25, 2011

@author: Carsten Witzke
'''
import unittest
from de.staticline.tools.LibsvmTools import LibsvmFileImporter
from tempfile import mkstemp
import os



class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_initFileImporter(self):
        #no filename
        with self.assertRaises(TypeError):
            LibsvmFileImporter()
        #wrong filename
        with self.assertRaises(IOError):
            LibsvmFileImporter('efwef')
            
    def test_importData(self):
        tmp = mkstemp()
        try:
            file = open(tmp[1], 'w')
            # create dummy file
            file.write('-1 3:1.4324 76:1 80:1 83:1\n'
                       '+1 14:1 19:1.324 84:1 # A comment\n'
                       '# another comment\n' # will be skipped
                       '-1 73:1 75:1 76:1 80:1 85:1.155\n')
            file.close()
            l = LibsvmFileImporter(tmp[1])
            
            # 1. we have a result
            self.assertTrue(l.get_dataSet() is not None)
            # 2. class is loaded correct
            self.assertTrue(l.get_dataSet()[0]['class'] is -1)
            # 3. comment lines correctly skipped
            self.assertTrue(l.get_dataSet()[2]['class'] is -1)
            # 3a. floating point conversion
            self.assertTrue(l.get_dataSet()[2].get(85) == 1.155)
        except Exception as e:
            print e
        finally:
            os.remove(tmp[1])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()