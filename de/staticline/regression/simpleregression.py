#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''

from numpy import *
from numpy.linalg.linalg import inv

class RidgeRegression(object):
    '''
    Ridge regression
    '''

    def __init__(self, complexity=1):
        #lambda is keyword, so I'm using complexity instead
        self.set_lambda(complexity)

    def trainModel(self, train):
        x = matrix(train.get_matrix())
        y = matrix(train.get_target())
        
        xTx = dot(x.T,x)
        # (X'X + λI)^-1
        m1 = inv(xTx + self.__complexity * xTx.I)
        # 
        self.__model = dot(dot(m1,x.T),y)
        
        #RSS(λ) = (y − Xβ)T (y − Xβ) + λβT β
        #         ---f1--T  ---f1--   --f2--
        f1 = y - dot(x,self.get_model())
        f2 = dot(dot(self.__complexity,self.__model.T),self.__model)
        self.__rss = dot(f1.T,f1) + f2
        #TODO: validate RSS        
        
    def validate_model(self, test):#FIXME: make new
        testdata = matrix(test.get_matrix())
#        sum_error = 0
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
        return self.__rss
    
    complexity = property(get_lambda, set_lambda, doc='the model complexity factor lambda')
    model = property(get_model, doc='the learned model')
    rss = property(get_rss, doc='residual sum of squares')