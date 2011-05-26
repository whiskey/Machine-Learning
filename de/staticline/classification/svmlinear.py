'''
Created on May 26, 2011

@author: Carsten Witzke
'''

import math
import numpy as np
from de.staticline.kernels.kernels import poly

class DualCoordinateDescent(object):
    def __init__(self):
        pass
    
    def train(self, predictors, targets, complxity, accuracy, kernel=poly):
        '''Dual coordinate descent implementation'''
        #init alpha and beta with zeros
        alpha = np.zeros(targets.shape)
        beta = np.zeros((1,(predictors.shape[1])))
        
        #init vector for all delta alphas with value infinity
        delta_alpha = float('inf') * np.ones(alpha.shape)
        #loop
                    
        while self.__foundDA(delta_alpha, accuracy):
            indices = range(len(predictors))
            np.random.shuffle(indices)
            for i in indices:
                #delta alpha
                x = (1 - float(targets[i]) * np.dot(beta, predictors[i]))/kernel(predictors[i])
                delta_alpha[i] = self.__bounded(x, float(alpha[i]), complxity)
                #alpha_i
                alpha[i] += delta_alpha[i]
                #beta_i
                beta = beta + delta_alpha[i] * targets[i] * predictors[i]
        print 'alpha: %s' % alpha
        print 'beta: %s' % beta
        return (alpha, beta)
                
    def __bounded(self, x, ai, gamma):
        '''keeps an input x in the two defined bounds'''
        if x < -ai: return -ai
        elif x > gamma-ai: return gamma-ai
        else: return x
            
    def __foundDA(self, list, acc):
        # ugly method - TODO: improve (np.exp())
        found = False
        for i in list:
            if math.fabs(i) > acc:
                found = True
        return found
    
    
if __name__ == '__main__':
    #print 'TODO: handle command line parameters'
    x = np.array([[1,1],[1,2],[-1,1],[-1,2]])
    y = np.array([1,1,0,0])
    DualCoordinateDescent().train(x, y, 1, 1e-10)
    #Results: -----> not verified atm! <------
    # alpha: [ 0.5  0.   1.   1. ]
    # beta: [[ 0.5  0.5]]