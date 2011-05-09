'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''

from numpy import *
from math import sqrt
from numpy.linalg.linalg import inv

class RidgeRegression(object):
    '''
    Ridge regression
    '''

    def __init__(self, complexity=1):
        #lambda is keyword, so I'm using this instead
        self.set_lambda(complexity)

    def trainModel(self, train):
        x = matrix(train.get_matrix())
        y = matrix(train.get_target())
        xTx = dot(x.transpose(),x)
        i = eye(xTx.shape[0],xTx.shape[1])
        m1 = inv(xTx + self.__complexity * i)
        self.__model = dot(dot(m1,x.transpose()),y)
        print self.get_model()
        
    def validate_model(self, test):#FIXME: make new
        testdata = matrix(test.get_matrix())
        sum_error = 0
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

    def get_rmse(self):
        return self.__rmse#TODO: implement rmse

    complexity = property(get_lambda, set_lambda, doc='the model complexity factor lambda')
    model = property(get_model, doc='the learned model')
    rmse = property(doc='root mean squared error')
