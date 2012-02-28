#!/usr/bin/env python

import os,sys,glob

# for a given 'inStem' and 'runID' creates .dat, .inp and .out filenames
def datInOut(inStem,runID):
    files = { \
    'datF':'../expDat/'+inStem+'.dat',  \
    'inF' :'../inp/'+inStem+'.inp',  \
    'outF':'../out/'+inStem+runID+'.out'  }
    print 'Experimental data in: '+files['datF']
    print 'Fresco input file:    '+files['inF']
    print 'Output file for plot: '+files['outF']
    return files

def runFresco(inF,outF):
    # run fresco
    print 'fresco < '+inF
    os.system('fresco < '+inF)
    # remove lines (beginning) with @ and the last line 'END' from the fort.16 output file
    os.system("grep -v '@' fort.16 | grep -v 'END' > "+outF)

files = datInOut(sys.argv[1],sys.argv[2])
runFresco(files['inF'],files['outF'])



