#!/usr/bin/env python


import os,sys,glob

# for a given 'inStem' and 'runID' creates .dat, .inp and .out filenames

# inStem = 'a28si28.0'
# runID = 'w24'
print sys.argv
inStem = sys.argv[1]
runID = sys.argv[2]
datF = '../dat/'+inStem+'.dat'
inF = '../inp/'+inStem+'.inp'
outF = '../out/'+inStem+runID+'.out'
print datF
print inF
print outF
# run fresco
# os.system('fresco < '+inF)
# remove lines (beginning) with @ and the last line 'END' from the fort.16 output file
# os.system("grep -v '@' fort.16 | grep -v 'END' > "+outF)

