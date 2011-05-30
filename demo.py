#!/usr/bin/python
'''
Created on May 7, 2011

@author: "Carsten Witzke"
'''
from de.staticline.tools.libsvmtools import LibsvmFileImporter
from de.staticline.regression.linreg import RidgeRegression


def regressionDemo():
    '''how to use this modules as library'''
    # get data sets from file
    trainingSet = LibsvmFileImporter('./data/regression/lin_reg').get_dataSet()
    #testSet = LibsvmFileImporter('./data/lin_reg.t').get_dataSet()
    
    # make new ridge regression
    rr = RidgeRegression()
    
    for i in range(5):
        # optional: set complexity parameter
        rr.set_lambda(i) # 0: linear regression w/o regularization
        # train the model
        rr.trainModel(trainingSet)
        # get model
        print 'model:\n%s' % rr.get_model()
        # get RSS
        #print u'RSS(\u03bb=%d): %f' % (rr.get_lambda(),rr.get_rss())
        # validation
        ##currently not implemented

if __name__ == '__main__':
    regressionDemo()
