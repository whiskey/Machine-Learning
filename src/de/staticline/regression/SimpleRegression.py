'''
Created on Apr 29, 2011

@author: Carsten Witzke
'''

from numpy import *
from math import sqrt

class RidgeRegression(object):
    '''
    Ridge regression a.k.a. Tikhonov regularization
    '''

    def __init__(self):
        pass

    def trainModel(self, train):
        training = matrix(train.get_matrix())
        # means
        means = training.mean(0)
        # sum of squares
        diff = training - means
        #FIXME: currently only 2D
        sxx = sum(multiply(diff[:,0],diff[:,0])) #sum (x-x')^2
        rss = sum(multiply(diff[:,1],diff[:,1])) #sum (y-y')^2
        sxy = sum(multiply(diff[:,0],diff[:,1])) #sum (x-x')(y-y')
        
        self.__a = sxy / sxx
        self.__b = float(means[:,1] - self.__a * means[:,0])
        
#        print 'slope = ',self.get_slope()
#        print 'intercept = ',self.get_intercept()
#        print 'rss = ',rss
        
    def validate_model(self, test):
        testdata = matrix(test.get_matrix())
        sum_error = 0
        for i in testdata:
            x = float(i[:,0])
            predicted = self.get_slope() * x + self.get_intercept()
            target = float(i[:,1])
            sum_error += (target - predicted)**2
            #print 'f_predicted(%.1f) = %.3f  f_target(x) = %.3f' % (x, predicted, target)
        print 'avg. error: %.4e' % (sum_error / test.get_numInstances())

    def get_slope(self):
        return self.__a

    def get_intercept(self):
        return self.__b

    def get_rmse(self):
        return self.__rmse

    a = property(doc='slope')
    b = property(doc='intercept')
    rmse = property(doc='root mean squared error')
