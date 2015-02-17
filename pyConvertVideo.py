#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import getopt, sys

#from misc import makeDir
#from error import usage, onError
#from video import checkIfVideo, generateFrames
#from image import makeContactSheet

from error import onError, usage


############### handle arguments ###############
try:
    myopts, args = getopt.getopt(sys.argv[1:],'vh', 
                                 ['verbose', 
                                  'help'])

except getopt.GetoptError as e:
    onError(1, str(e))

if len(sys.argv) == 1:  # no options passed
    onError(2, "No options given")

myFile = ""
path = ""
outDir = ""
skipExisting = False
info = False
verbose = False
keepGoing = False
noRename = True
outDir = ""

for option, argument in myopts:
    if option in ('-v', '--verbose'):
        verbose = True
    elif option in ('-h', '--help'):
        usage(0)
    else:
        onError(11, "Option %s not recognised" % option)
        