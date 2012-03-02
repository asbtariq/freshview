#!/usr/bin/env python

from potTypePosn import potType
from potTypePosn import potPosn

def chPotParam(param,newVal,inF):
    print 'Changing '+param+' to '+str(newVal)+' in '+inF
    print 'First, we have to find '+param+' in '+inF

    #newValue packed as a string 8 chars long
    newVal = float(newVal)
    newVal = ' '+str(newVal)+'      '
    newVal = newVal[:8]

    pInd = str(potType[param])
    pStart = potPosn[param][0]
    pEnd   = potPosn[param][1]

    filetext = open(inF).readlines()
    newfiletext = filetext[:9]
    # leave first eight cards(lines)
    for line in filetext[9:]:
        # leave out cards(lines) below that do not deal with potential params
        if len(line) > 14:
            potInd = line.split()[:3]
            # take first char only in cases like '2-42.0' i.e. no space betn params
            potInd[2] = potInd[2][:1]
            if param == 'rC':
                if potInd[1] == '0':
                    print 'Parameter line is: '+line[:-2]
                    print param+' is: '+line[pStart:pEnd]+'\n'
                    line = line[:pStart]+newVal+line[pEnd:]
                    print 'After changing ...'
                    print 'Parameter line is: '+line[:-2]
                    print 'Now '+param+' is: '+line[pStart:pEnd]
            elif potInd[2] == pInd:
                print 'Parameter line is: '+line[:-2]
                print param+' is: '+line[pStart:pEnd]+'\n'
                line = line[:pStart]+newVal+line[pEnd:]
                print 'After changing ...'
                print 'Parameter line is: '+line[:-2]
                print 'Now '+param+' is: '+line[pStart:pEnd]
            elif potInd[2] == pInd:
	        print 'Found Gaussian'
                print 'Gaussian param line is: '+line
            newfiletext.append(line)
        else:
            newfiletext.append(line)
    f=open(inF,'w')
    f.writelines(newfiletext)

'''        
import sys

potParam = sys.argv[1]
newValue = sys.argv[2]
inpFile  = sys.argv[3]

chPotParam(potParam,newValue,inpFile)
'''
