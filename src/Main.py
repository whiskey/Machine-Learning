'''
Created on Apr 25, 2011

@author: Carsten Witzke
'''
from de.staticline.ml.LibsvmTools import LibsvmFileImporter


if __name__ == '__main__':
    l = LibsvmFileImporter('../data/debug')
    print l.get_data()
    
