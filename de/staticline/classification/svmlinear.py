'''
Created on May 26, 2011

@author: Carsten Witzke
'''

import math
import numpy as np
from collections import deque
from de.staticline.kernels.kernels import Polynomial
from numpy import linalg

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

class StochasticBatchDescent(object):
    '''Stochastic/Batch subgradient descent implementation.'''
    
    def __init__(self, regularization=1, accuracy=1e-10, stepLength=0.5, stopCount=10, sampleSize=1):
        self.__regularization = regularization
        self.__accuracy = accuracy
        self.__stepLength = stepLength
        self.__stopCount = stopCount
        self.__sampleSize = sampleSize
        
    def train(self, instances, targets):    
        #init values
        self.__intercept = 0
        self.__beta = np.zeros(len(instances[0]))
        currentAccuracy = float('infinity')
        numInstances = len(instances)
        last_results = deque(maxlen=self.__stopCount)
        
        while currentAccuracy >= self.__accuracy:
            # doing this every time is not a speedbump but an easy way to show the only
            ### different stocastic vs. batch descent ###
            if(self.__sampleSize == 1):
                # draw ONE item
                i = np.random.randint(0,numInstances)
                #FIXME: currently not implemented
                # compute delta beta
                delta_beta = 0#dummy
                # compute delta intercept
                delta_intercept = 0#dummy
            else:
                # draw subset (indices)
                indices = range(len(instances))
                np.random.shuffle(indices)
                subset = indices[:self.__sampleSize]
                # compute delta beta and intercept
                sum_subset_y = 0
                sum_subset_yx = 0
                for i in subset:
                    x = targets[i] * (self.__beta.T * instances[i] + self.__intercept)
                    if x < 1:#FIXME: shape x is 'm x m' not 1 - misinterpretation of slides?
                        sum_subset_y += (x * targets[i])
                        sum_subset_yx += (x * targets[i] * instances[i])
                delta_beta = -1/self.__sampleSize * sum_subset_yx
                delta_intercept = -1/self.__sampleSize * sum_subset_y                
            ### same for stochastic and batch ###
            #update beta
            self.__beta = (1-self.__stepLength*self.__regularization) * self.__beta \
                - self.__stepLength * delta_beta
            #update intercept
            self.__intercept = self.__intercept - self.__stepLength * delta_intercept
            #compute current accuracy
            last_results.append(self.__stepLength * linalg.norm(delta_beta))
            currentAccuracy = sum(last_results)
        #debug
        print 'done\nbeta0 = {intercept:.4f}\nbeta = {beta}'.format(intercept=self.__intercept,beta=self.__beta)
        

    def get_regularization(self):
        return self.__regularization

    def get_accuracy(self):
        return self.__accuracy

    def get_step_length(self):
        return self.__stepLength

    def get_stop_count(self):
        return self.__stopCount
    
    def get_sample_size(self):
        return self.__sampleSize
    
    def get_intercept(self):
        return self.__intercept
    
    def get_beta(self):
        return self.__beta

    def set_regularization(self, value):
        self.__regularization = value

    def set_accuracy(self, value):
        self.__accuracy = value

    def set_step_length(self, value):
        self.__stepLength = value

    def set_stop_count(self, value):
        if value <= 0:
            value = 10
        self.__stopCount = value
        
    def set_sample_size(self, value):
        if value <= 0:
            value = 1
        self.__sampleSize = value

    ### properties
    intercept = property(get_intercept, doc="intercept of the model")
    beta = property(get_beta, doc="beta values")
    regularization = property(get_regularization, set_regularization, doc="regularization value")
    accuracy = property(get_accuracy, set_accuracy, doc="accuracy value of the model")
    stepLength = property(get_step_length, set_step_length, doc="step length of the gradient descent")
    stopCount = property(get_stop_count, set_stop_count, doc="stop count")
    sampleSize = property(get_sample_size, set_sample_size, doc="sample size; 1 means stochastic, 2+ batch")
