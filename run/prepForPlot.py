#!/usr/bin/env python

# This script removes lines with an @ and the last line 'END' from the fort.16 output file

import os,glob

inpF = 'a28si28.0'
runID = 'w24'
outF = '../out/'+inpF+runID+'.out'
os.system('fresco < ../inp/'+inpF+'.inp')
os.system("grep -v '@' fort.16 | grep -v 'END' > "+outF)

