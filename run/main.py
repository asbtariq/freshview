#!/usr/bin/env python

import sys,os
from setFilesAndRun import datInOut
from setFilesAndRun import runFresco

if len(sys.argv) <= 1:
    print
    print 'Usage python ./main.py [target] [Energy_1] ... [Energy_n] [runID]'
    print 'e.g. python ./main.py 28Si 26 26.5 27 Run1'
    print '[runID] is any string (character) label to identify the run'
    print 
    exit
target = sys.argv[1]
energyMeV = sys.argv[2:-1]
runId = sys.argv[-1:]

for en in range(len(energyMeV)):
    print 'Set ',en
    stem = target+str(int(float(energyMeV[en])*1000))
    files = datInOut(stem,runId[0])
    runFresco(files['inF'],files['outF'])

