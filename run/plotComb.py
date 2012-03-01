#!/usr/bin/env python

import numpy
from matplotlib import pyplot

e1Dat = numpy.loadtxt( '../expDat/28Si26000.dat')
t1Dat = numpy.loadtxt('../out/28Si26000run1.out')
e2Dat = numpy.loadtxt( '../expDat/28Si26500.dat')
t2Dat = numpy.loadtxt('../out/28Si26500run1.out')
e3Dat = numpy.loadtxt( '../expDat/28Si27000.dat')
t3Dat = numpy.loadtxt('../out/28Si27000run1.out')

fig1 = pyplot.figure(1)

fig1a = fig1.add_subplot(311)
fig1a = pyplot.semilogy(e1Dat[:,0],e1Dat[:,1],'go')
fig1a = pyplot.semilogy(t1Dat[:,0],t1Dat[:,1])
fig2a = fig1.add_subplot(312)
fig2a = pyplot.semilogy(e2Dat[:,0],e2Dat[:,1],'go')
fig2a = pyplot.semilogy(t2Dat[:,0],t2Dat[:,1])
fig3a = fig1.add_subplot(313)
fig3a = pyplot.semilogy(e3Dat[:,0],e3Dat[:,1],'go')
fig3a = pyplot.semilogy(t3Dat[:,0],t3Dat[:,1])


pyplot.show()


