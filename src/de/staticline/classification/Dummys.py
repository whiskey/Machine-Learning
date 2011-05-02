'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''
from de.staticline.tools.LibsvmTools import LibsvmFileImporter

class Always1Predictor(object):
    '''
    A dummy predictor assuming always "1" for each instance.
    '''

    def __init__(self):
        pass
    
    def buildClassifier(self, trainFile):
        '''builds a classification model returning always 1 for each instance'''
        train = LibsvmFileImporter(trainFile)
        train.get_data()
    
    def validateModel(self, testFile):
        test = LibsvmFileImporter(testFile)
        testdata = test.get_data()

        ## --- statistics
        correct = 0.
        for i in testdata:
            if i['class'] == 1: #correct
                correct += 1.
        # percent correct
        self.__pct_correct = 100 * (correct/len(testdata))
        # root mean squared error
        # assuming classes {-1,1} the error can be computed IN THIS CASE as
        # 2 * (instances_total - instances_correct)
        self.__rmse = 2 * (len(testdata) - correct)
        
    def get_pctCorrect(self):
        return self.__pct_correct
    
    def get_rmse(self):
        return self.__rmse
    
    #properties
    pct_correct = property(get_pctCorrect, doc='the percentage of correct instances')
    rmse = property(get_rmse, doc='the root mean squared error')


