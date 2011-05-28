'''
Created on Apr 25, 2011

@author: Carsten Witzke
'''
import os
import unittest
from de.staticline.tools.libsvmtools import LibsvmFileImporter
import sys


class DataFetchTestCase(unittest.TestCase):

    def testInitFileImporter(self):
        #no filename
        with self.assertRaises(TypeError):
            LibsvmFileImporter()
        #wrong filename
        with self.assertRaises(IOError):
            LibsvmFileImporter('efwef')
            
    def testImportData(self):
        cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
        l = LibsvmFileImporter(os.path.join(cwd,'data/classification/debug'))
        ds = l.get_dataSet()
        ''' contents of the debug file
        -1 3:1.4324 76:1 80:1 83:1
        +1 14:1 19:1.324 84:1 # A comment
        # another comment
        -1 73:1 75:1 76:1 80:1 85:1.155
        '''
        
        # 1. we have a result
        self.assertTrue(ds is not None)
        # 2. class is loaded correct
        self.assertTrue(ds.get_targets(0) == -1)
        # 3. comment lines correctly skipped
        self.assertTrue(ds.get_targets(2) == -1)
        with self.assertRaises(IndexError):
            #should not exist
            self.assertTrue(ds.get_targets(3) == -1)
    
    def testBinaryImport(self):
        cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
        # should do
        importer = LibsvmFileImporter(os.path.join(cwd,'data/classification/a1a'),binary=True)
        importer.get_dataSet()
        
        # should fail
        with self.assertRaises(TypeError):
            importer = LibsvmFileImporter(os.path.join(cwd,'data/classification/satimage.scale'),binary=True)

if __name__ == "__main__":
    unittest.main()