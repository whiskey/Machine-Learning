'''
Created on May 19, 2011

@author: Carsten Witzke
'''
import numpy as np
from de.staticline.kernels.kernels import Polynomial


class SMO_Keerthi(object):
    '''SMO (Keerthi 2001) implementation'''
        
    def __init__(self,complexity=1, accuracy=1e-10, kernel=Polynomial(2), verbose=False):
        self.set_complexity(complexity)
        self.set_accuracy(accuracy)
        self.__kernel = kernel
        self.__verbose = verbose
    
    def __repr__(self):
        return 'SMO (Keerthi 2001) implementation. Parameters:\n'\
            '  complexity: {comp}\n  accuracy: {acc}\n  kernel: {kernel}'\
            .format(comp=self.get_complexity(), acc=self.get_accuracy(), kernel=self.get_kernel())
    
    def train(self, instances, targets):
        self.__alpha = np.zeros(len(targets))
        f = targets[:] #copy - necessary?
        
        tmp = targets.flatten(1).tolist()
        i = tmp.index(+1.)
        j = tmp.index(-1.)
        
        while f[i]-f[j] > self.__accuracy:
            #TODO: kernel chaching
            ij = self.__kernel.calc(instances[i], instances[j])
            delta_alpha = (f[i]-f[j]) / ij
            if targets[i] * targets[j] == -1:
                delta_alpha = targets[i] * self.__bounded(targets[i] * delta_alpha, 
                                                          self.__complexity-max(self.__alpha[i], self.__alpha[j]), 
                                                          -min(self.__alpha[i], self.__alpha[j]))
            else:
                delta_alpha = targets[i] * self.__bounded(targets[i] * delta_alpha, 
                                                          min(self.__complexity-self.__alpha[i], self.__alpha[j]), 
                                                          -min(self.__alpha[i], self.__complexity-self.__alpha[j]))
            self.__alpha[i] += targets[i] * delta_alpha
            self.__alpha[j] -= targets[j] * delta_alpha
            #maintain f and find new i,j
            argmax_i = 0
            argmin_j = 0
            for k in range(len(targets)):
                ki = self.__kernel.calc(instances[k], instances[i])
                kj = self.__kernel.calc(instances[k], instances[j])
                
                f[k] = f[k] - delta_alpha * (ki - kj)
                #set new i,j
                if (targets[k] == +1 and self.__alpha[k] < self.__complexity) or (targets[k] == -1 and self.__alpha[k] > 0):
                    if f[k] > argmax_i:
                        i = k
                        argmax_i = f[k]
                if (targets[k] == -1 and self.__alpha[k] < self.__complexity) or (targets[k] == +1 and self.__alpha[k] > 0):
                    if f[k] < argmin_j:
                        j = k
                        argmin_j = f[k]
            
            ## statistics
            if self.__verbose:
                print 'f[{i}]-f[{j}]: {f}'.format(i=i, j=j, f=f[i]-f[j])
            self.__num_support_vectors = 0
            for a in self.__alpha.flatten(1).tolist():
                if a > 0:
                    self.__num_support_vectors += 1
                
    
    def __bounded(self, x, upper, lower):
        '''keeps an input x in the two defined bounds'''
        if x < lower: return lower
        elif x > upper: return upper
        else: return x
        
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
        
    def get_alpha(self):
        return self.__alpha
    
    def get_num_support_vectors(self):
        return self.__num_support_vectors
    
    ### properties
    complexity = property(get_complexity, set_complexity, doc='complexity value of the model')
    accuracy = property(get_accuracy, set_accuracy, doc='accuracy value of the model')
    kernel = property(get_kernel, set_kernel, doc='the models kernel')
    alpha = property(get_alpha, doc='alpha values')
    num_support_vectors = property(get_num_support_vectors, doc='the number of support vectors')
    verbose = property(doc='print tons of more or less useful stuff?')
   