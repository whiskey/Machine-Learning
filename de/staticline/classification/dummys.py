'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''
from de.staticline.tools.libsvmtools import LibsvmFileImporter
import math

class Always1Predictor(object):
    '''
    A dummy predictor assuming always "1" for each instance.
    '''

    def __init__(self):
        pass
    
    def buildClassifier(self, trainFile):
        '''"builds" a classification model returning always 1 for each instance'''
        train = LibsvmFileImporter(trainFile).get_dataSet()
        self.__inst_train = train.get_numInstances()
        # no training needed
    
    def validateModel(self, testFile):
        testdata = LibsvmFileImporter(testFile).get_dataSet()
        self.__inst_test = testdata.get_numInstances()
        ## --- statistics
        correct = 0.
        sum_error = 0
        for i in testdata.get_targets():
            if i == 1: #correct
                correct += 1.
            else:
                sum_error += math.pow(1 - i, 2)
        # percent correct
        self.__pct_correct = 100 * (correct/self.__inst_test)
        # root mean squared error
        self.__rmse = math.sqrt(sum_error / self.__inst_test)
        
    def get_pctCorrect(self):
        return self.__pct_correct
    
    def get_rmse(self):
        return self.__rmse
    
    def get_inst_train(self):
        return self.__inst_train

    def get_inst_test(self):
        return self.__inst_test
    
    #properties
    inst_train = property(get_inst_train, doc='number of training instances')
    inst_test = property(get_inst_test, doc='number of test instances')
    pct_correct = property(get_pctCorrect, doc='the percentage of correct instances')
    rmse = property(get_rmse, doc='the root mean squared error')


