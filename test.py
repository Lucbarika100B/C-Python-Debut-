#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Jour 4,

from ift099 import *
from math import *



test = (((3,),'*',(4,)),'-',((7,),'/',(2,))),'*',(5,)

def compileFinal(tree):
    compile(tree)
    print '='

def compile(tree):

    if(len(tree)==1):
        print tree[0]

    else:
        compile(tree[0])
        if(len(tree[0])>1):
            print'SG'
            compile(tree[2])
            print 'SD'
            print'RG'
            print tree[1]
            print 'RD'
        else:
            print tree[1]
            compile(tree[2])





compileFinal(test)

