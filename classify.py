#!/usr/bin/python
'''
Created on May 28, 2011

@author: Carsten Witzke
'''
import sys
import getopt
from de.staticline.classification.svmlinear import DualCoordinateDescent
from de.staticline.classification.dummys import Always1Predictor
from de.staticline.classification.svm import SMO_Keerthi
import os
from de.staticline.tools.libsvmtools import LibsvmFileImporter
from de.staticline.kernels.kernels import Polynomial, Linear, RBF

def main(argv):
    ## get arguments
    try:
        opts, args = getopt.getopt(argv, 'hvc:k:', 
               ['help','verbose','classifier=','complexity=','accuracy=','kernel=','degree=','gamma=','training-file=','test-file='])
    except getopt.GetoptError, error:
        print str(error)
        usage()
        sys.exit(2)
    
    ## handle arguments
    classifier = None
    kernel = None
    trainingFile = None
    testFile = None
    verbose = False
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        if opt in ('-v', '--verbose'):
            verbose = True
        # -------------- CLASSIFIER -----------------
        if opt in ('-c', '--classifier'):
            if arg == 'dummy': # -------- dummy --
                classifier = Always1Predictor()
            elif arg == 'svm-cd': # -------- svm coordinate descent --
                c=1
                a=1e-10
                for opt2, arg2 in opts:
                    if opt2 == '--complexity':
                        c = arg2
                    elif opt2 == '--accuracy':
                        a = arg2
                classifier = DualCoordinateDescent(accuracy=a, complexity=c, verbose=verbose)
            elif arg == 'svm-smo-keerthi': # -------- SMO (Keerthi) --
                c=1
                a=1e-10
                for opt2, arg2 in opts:
                    if opt2 == '--complexity':
                        c = arg2
                    elif opt2 == '--accuracy':
                        a = arg2
                classifier = SMO_Keerthi(accuracy=a, complexity=c, verbose=verbose)
            else:
                print 'Sorry, this classifier is currently not implemented :('
                sys.exit()
        # -------------- KERNEL -----------------
        if opt in ('-k', '--kernel'):
            if arg == 'linear':
                kernel = Linear()
            elif arg == 'poly':
                # search parameters
                for opt2, arg2 in opts:
                    if opt2 == '--degree':
                        kernel = Polynomial(arg2)
                kernel = Polynomial()
            elif arg == 'rbf':
                # search parameters
                for opt2, arg2 in opts:
                    if opt2 == '--gamma':
                        kernel = RBF(arg2)
                kernel = RBF()
            else:
                print 'unknown kernel {kernel}'.format(kernel=arg)
                kernel = None
        # -------------- TRAINING FILE -----------------
        if opt == '--training-file':
            if os.path.exists(arg):
                trainingFile = arg
            else:
                print 'It seems that the training file you specified does not exist. Please check path.'
                sys.exit()
        # -------------- TEST FILE -----------------
        if opt == '--test-file':
            if os.path.exists(arg):
                testFile = arg
            else:
                print 'It seems that the test file you specified does not exist. Please check path.'
                sys.exit()
    
    ## process input
    if classifier == None:
        print 'No classifier specified.'
        usage()
        sys.exit()
    if trainingFile == None:
        print 'No training file specified.'
        usage()
        sys.exit()
    if testFile == None:
        print 'No test file specified.'
        usage()
        sys.exit()
    training = LibsvmFileImporter(trainingFile, binary=True).get_dataSet()
    testing = LibsvmFileImporter(testFile, binary=True).get_dataSet()
    
    #start classification - TODO: implement report and validation
    if classifier.__class__ == DualCoordinateDescent().__class__:
        classifier.set_kernel(kernel)
        if verbose: print classifier
        classifier.train(training.get_features(), training.get_targets())
    elif classifier.__class__ == SMO_Keerthi().__class__:
        classifier.set_kernel(kernel)
        if verbose: print classifier
        classifier.train(training.get_features(), training.get_targets())
        print '# support vectors:',classifier.get_num_support_vectors()
    
    
def usage(): # not 100% UNIX style... don't care atm
    print '''usage: {file} [options]
    
    -h, --help                                        display this usage information
    
    -c, --classifier=svm-cd|svm-smo-keerthi|dummy      select a classifier
    --complexity=VALUE                                set the complexity VALUE for the classifier
    
    -k, --kernel=linear|poly|rbf                      select a kernel
    --degree=VALUE                                    set the degree VALUE of a poly-Kernel
    --gamma=VALUE                                     set the gamma VALUE for a rbf-Kernel
    
    --training-file=FILE                              read training data from FILE
    --test-file=FILE                                  evaluate on FILE
'''.format(file=__file__)

if __name__ == '__main__':
    main(sys.argv[1:])