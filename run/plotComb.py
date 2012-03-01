#!/usr/bin/env python

import numpy
from matplotlib import pyplot

def plotMult(exF,thF):
    fig = pyplot.figure()
    for setId in range(len(exF)):
        print 'Plotting Set ',setId,' ...'
        eDat = numpy.loadtxt(exF[setId])
        tDat = numpy.loadtxt(thF[setId])
        subPlotIdx = str(len(exF))+'1'+str(setId+1)
        subFig = fig.add_subplot(subPlotIdx)
        ePlot = pyplot.semilogy(eDat[:,0],eDat[:,1],'go')
        tPlot = pyplot.semilogy(tDat[:,0],tDat[:,1])
    pyplot.show()

exFiles = [ '../expDat/28Si26000.dat', '../expDat/28Si26500.dat', '../expDat/28Si27000.dat']
thFiles = ['../out/28Si26000run1.out','../out/28Si26500run1.out','../out/28Si27000run1.out']
plotMult(exFiles,thFiles)


