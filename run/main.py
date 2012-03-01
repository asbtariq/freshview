#!/usr/bin/env python

import sys,os
from setFilesAndRun import datInOut
from setFilesAndRun import runFresco

if len(sys.argv) <= 1:
    print
    print 'Usage: python ./main.py [target] [Energy_1] ... [Energy_n] [runID]'
    print 'e.g. python ./main.py 28Si 26 26.5 27 Run1'
    print '[runID] is any string (character) label to identify the run'
    print 
    exit
target = sys.argv[1]
energyMeV = sys.argv[2:-1]
runId = sys.argv[-1:]

datFiles = []
inFiles = []
outFiles = []
for en in range(len(energyMeV)):
    print 'Set ',en
    stem = target+str(int(float(energyMeV[en])*1000))
    files = datInOut(stem,runId[0])
    datFiles.append(files['datF'])
    outFiles.append(files['outF'])
    runFresco(files['inF'],files['outF'])

from plotComb import plotMult
plotMult(datFiles,outFiles)


print 
print 'Plotted for Target: '+target+' at ',energyMeV,' MeV'
print 
print 'Select your option'
print
print '1 - Change parameter'
print '2 - Finished'
code = input()
if code == 1:
    print '[Parameter] [New value] [energy("all" for all energies)]'
if code == 2:
    print 'Thank you!'

