#!/usr/bin/env python

import sys,os
from setFilesAndRun import filesRunPlot
from chPotParam import chPotParam

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print
        print 'Usage: python ./FreshView.py [target] [Energy_1] ... [Energy_n] [runID]'
        print 'e.g. python ./FreshView.py 28Si 26 26.5 27 Run1'
        print '[runID] is any string (character) label to identify the run'
        print 
        exit

    target = sys.argv[1]
    energyMeV = sys.argv[2:-1]
    runId = sys.argv[-1:]         

    
    runIdx = 0
    while runIdx == 0:
        inpFiles = filesRunPlot(target,energyMeV,runId)
        print 
        print 'Select your option'
        print
        print '1 - Change parameter'
        print '2 - Finished'
        code = input()
        if code == 1: 
            print '[Param] [NewVal] [engy("all" for all energies)] [runID("0" for overwrite)]'
            chp = raw_input()
            par,newValue,engy,runIDnew = chp.split()        
            if engy != 'all':
                inpFileToChange = '../inp/'+target+     \
                    str(int(float(engy)*1000))+'.inp'
                print inpFileToChange
                chPotParam(par,newValue,inpFileToChange)
            elif engy == 'all':
                for inpFileToChange in inpFiles:
                    chPotParam(par,newValue,inpFileToChange)
            if runIDnew != '0':
                runId = [runIDnew]
        elif code == 2:
            print 'Thank you!'
            runIdx = 1

