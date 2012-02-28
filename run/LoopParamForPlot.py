#!/usr/bin/env python


import os,sys,glob

# inStem = 'a28si28.0'
# runID = 'w24'
print sys.argv
inStem = sys.argv[1]
runID = sys.argv[2]
inF = '../inp/'+inStem+'.inp'
outF = '../out/'+inStem+runID+'.out'
print inF
print outF
# run fresco
# os.system('fresco < '+inF)
# remove lines (beginning) with @ and the last line 'END' from the fort.16 output file
# os.system("grep -v '@' fort.16 | grep -v 'END' > "+outF)

