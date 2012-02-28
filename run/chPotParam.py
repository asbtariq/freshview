def chPotParam(param,newVal,inF):
#    filetext = open(datafile).read()
    print 'Changing '+param+' to '+str(newVal)+' in '+inF
    print 'First, we have to find '+param+' in '+inF
    filetext = open(inF).readlines()
    newfiletext = filetext[:9]
    # leave first eight cards(lines)
    for line in filetext[9:]:
#        print line,'has length: ',len(line)
        # leave out cards(lines) below that do not deal with potential params
        if len(line) > 14:
            potInd = line.split()[1:3]
            # take first char only in cases like '2-42.0' i.e. no space betn params
            potInd[1] = potInd[1][:1]
#            print potInd
            if potInd == ['1','0']:
                print 'Found WS'
                print 'WS param line is: '+line
                print 'V0 is: '+line[8:16]
                line = line[:8]+' 24.00  '+line[16:]
                print 'After changing'
                print 'WS param line is: '+line
                print 'V0 is: '+line[8:16]
            elif potInd == ['1','2']:
	        print 'Found Gaussian'
                print 'Gaussian param line is: '+line
            newfiletext.append(line)
        else:
            newfiletext.append(line)
    print
    print 'original filetext', filetext
    print
    print 'updated newfiletext', newfiletext
    print
    f=open(inF,'w')
    f.writelines(newfiletext)
        
#        potInd[
#        if potInd 
    
#    filetext=filetext.replace(': N',': M')
#    chdatafile = open(datafile,'w')
#    chdatafile.write(filetext)
#    chdatafile.close()
#    print 'done!'


chPotParam('V0',24.0,'../inp/test.inp')
