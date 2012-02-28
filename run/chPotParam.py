def chPotParam(param,inF):
#    filetext = open(datafile).read()
    print 'Changing '+param+' in '+inF
    filetext = open(inF).read()
    print filetext
#    filetext=filetext.replace(': N',': M')
#    chdatafile = open(datafile,'w')
#    chdatafile.write(filetext)
#    chdatafile.close()
#    print 'done!'


chPotParam('W0','../inp/test.inp')
