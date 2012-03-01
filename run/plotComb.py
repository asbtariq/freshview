#!/usr/bin/env python

import numpy
from matplotlib import pyplot

def plotMult(exF,thF):
    fig = pyplot.figure()
    for setId in range(len(exF)):
        print 'Plotting Set ',setId,' ...'
        eDat = numpy.loadtxt(exF[setId])
        tDat = numpy.loadtxt(thF[setId])
        # setting subPlotIdx to n11,n12, ... ,n1n
        subPlotIdx = str(len(exF))+'1'+str(setId+1)
        subFig = fig.add_subplot(subPlotIdx)
        subFig.set_xlim(0,180)
        subFig.semilogy(eDat[:,0],eDat[:,1],'go')
        subFig.semilogy(tDat[:,0],tDat[:,1])
#        ePlot = pyplot.semilogy(eDat[:,0],eDat[:,1],'go')
#        tPlot = pyplot.semilogy(tDat[:,0],tDat[:,1])
    pyplot.show()



