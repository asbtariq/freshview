#!/usr/bin/env python

import os,sys
from plotComb import plotMult


def runFresco(inF,outF):
    # run fresco
    print 'Running Fresco with input '+inF+' and output '+outF
    os.system('fresco < '+inF+' > fresco.stdout')
    # remove lines (beginning) with @ and # and 
    # the last line 'END' from the fort.16 output file
    os.system("grep -v '@' fort.16 | grep -v '#' | grep -v 'END' > "+outF)


# for a given 'target','energyMeV' and 'runID' 
# creates .dat, .inp and .out filenames
# run Fresco and plot
def filesRunPlot(target,energyMeV,runID):
    datFiles = []
    inpFiles = []
    outFiles = []
    for en in range(len(energyMeV)):
        print 'Set ',en
        stem = target+str(int(float(energyMeV[en])*1000))
        datFiles.append('../expDat/'+stem+'.dat')
        inpFiles.append('../inp/'+stem+'.inp')
        outFiles.append('../out/'+stem+runID[0]+'.out')
        print 'Experimental data in: '+datFiles[en]
        print 'Fresco input file:    '+inpFiles[en]
        print 'Output file for plot: '+outFiles[en]
        runFresco(inpFiles[en],outFiles[en])

    plotMult(datFiles,outFiles)
    print 
    print 'Plotted for Target: '+target+' at ',energyMeV,' MeV'

    return inpFiles


#files = datInOut(sys.argv[1],sys.argv[2])
#runFresco(files['inF'],files['outF'])



