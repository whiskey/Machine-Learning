#!/usr/bin/python
'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''

import numpy as np
from numpy.linalg.linalg import inv

class RidgeRegression(object):
    '''
    Ridge regression
    '''

    def __init__(self, complexity=1):
        #lambda is keyword, so I'm using complexity instead
        self.set_lambda(complexity)

    def trainModel(self, train):
        instances = train.get_features()
        ones = np.ones((instances.shape[0],1))
        instances = np.matrix(np.concatenate((ones,instances), axis=1))
        targets = np.array(train.get_targets())
        
        # build model - FIXME: currently only correct with complex. = 0
        xTx = np.dot(instances.T, instances)
        xTx += np.dot(self.__complexity, np.eye(xTx.shape[0],xTx.shape[1]))
        xTy = np.dot(instances.T, targets)
        solution = np.linalg.lstsq(xTx, xTy)
        self.__model = solution[0] #model

#        xTx = np.dot(instances.T,instances)
#        m1 = inv(xTx + self.__complexity * xTx.I)
#        self.__model = np.dot(np.dot(m1,instances.T),targets)
        
        # RSS
        self.__rss = 0
#        for i in range(len(train.get_features())):
#            fx = self.__model[1] * train.get_features()[i] + self.__model[0]
#            self.__rss += (targets[i] -  fx)**2 #FIXME: ValueError: input must be a square array
        
        self.__rmse = np.sqrt(self.__rss / (train.get_numInstances()-2))
#        f1 = targets - np.dot(instances,self.get_model())
#        f2 = np.dot(np.dot(self.__complexity,self.__model.T),self.__model)
#        self.__rss = np.dot(f1.T,f1) + f2
        
        # RMSE
        
        
        
    def validate_model(self, test):#FIXME: make new
        pass
#        testdata = np.array(test.get_np.array(get_features  sum_error = 0)
#        for i in testdata:
#            x = float(i[:,0])
#            predicted = self.get_slope() * x + self.get_intercept()
#            target = float(i[:,1])
#            sum_error += (target - predicted)**2
#            #print 'f_predicted(%.1f) = %.3f  f_target(x) = %.3f' % (x, predicted, target)
#        print 'avg. error: %.4e' % (sum_error / test.get_numInstances())

    def get_lambda(self):
        return self.__complexity
    
    def set_lambda(self, value):
        self.__complexity = value
        
    def get_model(self):
        return self.__model
    
    def get_rss(self):
        return float(self.__rss)
    
    def get_rmse(self):
        return float(self.__rmse)
    
    complexity = property(get_lambda, set_lambda, doc='the model complexity factor lambda')
    model = property(get_model, doc='the learned model')
    rss = property(get_rss, doc='residual sum of squares')
    rmse = property(get_rmse, doc='root mean squared error')