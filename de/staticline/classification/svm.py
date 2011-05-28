'''
Created on May 19, 2011

@author: Carsten Witzke
'''
import numpy as np
from de.staticline.kernels.kernels import poly, Polynomial


class SMO_Keerthi(object):
    
    def __init__(self):
        pass
    
    def train(self, instances, targets, complexity=1, accuracy=1e-10, kernel=Polynomial(2)):
        '''SMO (Keerthi 2001) implementation'''
        self.__alpha = np.zeros(len(targets))
        f = targets[:] #copy - necessary?
        
        tmp = targets.flatten(1).tolist()
        i = tmp.index(+1.)
        j = tmp.index(-1.)
        
        while f[i]-f[j] > accuracy:
            #TODO: kernel chaching
            ij = kernel.calc(instances[i], instances[j])
            delta_alpha = (f[i]-f[j]) / ij
            if targets[i] * targets[j] == -1:
                delta_alpha = targets[i] * self.__bounded(targets[i] * delta_alpha, 
                                                          complexity-max(self.__alpha[i], self.__alpha[j]), 
                                                          -min(self.__alpha[i], self.__alpha[j]))
            else:
                delta_alpha = targets[i] * self.__bounded(targets[i] * delta_alpha, 
                                                          min(complexity-self.__alpha[i], self.__alpha[j]), 
                                                          -min(self.__alpha[i], complexity-self.__alpha[j]))
            self.__alpha[i] += targets[i] * delta_alpha
            self.__alpha[j] -= targets[j] * delta_alpha
            #maintain f and find new i,j
            argmax_i = 0
            argmin_j = 0
            for k in range(len(targets)):
                ki = kernel.calc(instances[k], instances[i])
                kj = kernel.calc(instances[k], instances[j])
                
                f[k] = f[k] - delta_alpha * (ki - kj)
                #set new i,j
                if (targets[k] == +1 and self.__alpha[k] < complexity) or (targets[k] == -1 and self.__alpha[k] > 0):
                    if f[k] > argmax_i:
                        i = k
                        argmax_i = f[k]
                if (targets[k] == -1 and self.__alpha[k] < complexity) or (targets[k] == +1 and self.__alpha[k] > 0):
                    if f[k] < argmin_j:
                        j = k
                        argmin_j = f[k]
            print 'f[i]-f[j]: ', f[i]-f[j]
        print self.__alpha
    
    def __bounded(self, x, upper, lower):
        '''keeps an input x in the two defined bounds'''
        if x < lower: return lower
        elif x > upper: return upper
        else: return x
    
    ### properties
    alpha = property(doc='alphas')