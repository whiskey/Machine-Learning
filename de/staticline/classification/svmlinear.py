'''
Created on May 26, 2011

@author: Carsten Witzke
'''

import math
import numpy as np
from de.staticline.kernels.kernels import Polynomial

class DualCoordinateDescent(object):
    def __init__(self,complexity=1, accuracy=1e-10, kernel=Polynomial(2), verbose=False):
        self.set_complexity(complexity)
        self.set_accuracy(accuracy)
        self.__kernel = kernel
        self.__verbose = verbose
        
    def __repr__(self):
        return 'SVM dual coordinate descent implementation. Parameters:\n'\
            '  complexity: {comp}\n  accuracy: {acc}\n  kernel: {kernel}'\
            .format(comp=self.get_complexity(), acc=self.get_accuracy(), kernel=self.get_kernel())
    
    def train(self, predictors, targets):
        '''Dual coordinate descent implementation'''
        #init alpha and beta with zeros
        alpha = np.zeros(len(targets))
        beta = np.zeros((predictors.shape[1]))
        
        #init vector for all delta alphas with value infinity
        delta_alpha = float('inf') * np.ones(len(alpha))
        #loop
                    
        while self.__foundDA(delta_alpha, self.__accuracy):
            indices = range(len(predictors))
            np.random.shuffle(indices)
            for i in indices:
                #delta alpha
                x = (1 - float(targets[i]) * np.dot(beta, predictors[i]))/self.__kernel.calc(predictors[i])
                delta_alpha[i] = self.__bounded(x, float(alpha[i]), self.get_complexity())
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

    def set_complexity(self, value):
        try:
            self.__complexity = float(value)
        except ValueError, err:
            print str(err)
        
    def get_complexity(self):
        return self.__complexity
    
    def set_accuracy(self, value):
        try:
            self.__accuracy = float(value)
        except ValueError, err:
            print str(err)
        
    def get_accuracy(self):
        return self.__accuracy
    
    def set_kernel(self, kernel):
        if kernel != None:#TODO: make kernel-Class for all kernels
            self.__kernel = kernel
    
    def get_kernel(self):
        return self.__kernel
        
#    def get_alpha(self):
#        return self.__alpha
#    
#    def get_num_support_vectors(self):
#        return self.__num_support_vectors
    
    ### properties
    complexity = property(get_complexity, set_complexity, doc='complexity value of the model')
    accuracy = property(get_accuracy, set_accuracy, doc='accuracy value of the model')
    kernel = property(get_kernel, set_kernel, doc='the models kernel')
#    alpha = property(get_alpha, doc='alpha values')
