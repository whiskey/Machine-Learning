'''
Created on May 7, 2011

@author: "Carsten Witzke"
'''
from de.staticline.tools.libsvmtools import LibsvmFileImporter
from de.staticline.regression.simpleregression import RidgeRegression

if __name__ == '__main__':
    # get data sets from file
    trainingSet = LibsvmFileImporter('data/lin_reg').get_dataSet()
    testSet = LibsvmFileImporter('data/lin_reg.t').get_dataSet()
    
    # make new ridge regression
    rr = RidgeRegression()
    # optional: set complexity parameter
    rr.set_lambda(2)
    # train the model
    rr.trainModel(trainingSet)
    # get model
    print 'model:\n%s' % rr.get_model()
    # get RSS
    print 'RSS: %f' % rr.get_rss()
    # validation
    #rr.validate_model(testSet) #currently not implemented
