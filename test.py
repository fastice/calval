#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:25:57 2020

@author: ian
"""
import sarfunc as s
import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
from datetime import datetime

useErrors=False
#myVel.readProduct('Vel.2015-08-13.2015-08-24/TSX_W69.10N_13Aug15_24Aug15_10-05-49_*_v02.0',useErrors=useErrors)
useXR=False
startTime=datetime.now()
myVel=s.nisarVel()
myVel.readProduct(
    'Vel-2018-01-01.2018-12-31/release//GL_vel_mosaic_Annual_01Jan18_31Dec18_*_v02.0',useErrors=useErrors,useXR=useXR)
axImage=myVel.displayVel()

myVel.setupInterp(useVelocity=True,useErrors=useErrors)
myTies=s.tiePoints(tieFile='/Users/ian/tiepoints/TiepointsGL.ll.culled')
vx,vy,v,igood=myTies.zeroVData(myVel)



myTies.zeroStats(myVel)
myTies.plotAllTieLocs(vel=myVel,ax=axImage,color='r',marker='.')
myTies.plotZeroTieLocs(vel=myVel,ax=axImage,color='b',marker='.')
plt.show()
print(f'Time {datetime.now()-startTime}')
print(myTies.zeroStats(myVel))
exit()

print(f'sizeInPixels {myVel.sizeInPixels()}')
print(f'sizeInM {myVel.sizeInM()}')
print(f'sizeInKm {myVel.sizeInKm()}')
print(f'originInM {myVel.originInM()}')
print(f'originInKm {myVel.originInKm()}')
print(f'boundsInM {myVel.boundsInM()}')
print(f'boundsInKm {myVel.boundsInKm()}')
#
myTies=s.tiePoints(tieFile='/Users/ian/tiepoints/TiepointsGL.ll.culled')
vx,vy,v,igood=myTies.zeroVData(myVel)
print(f'Time {datetime.now()-startTime}')
print(myTies.zeroStats(myVel))
x,y=myTies.xyzerokm()
#
if useXR :
    vImg=np.array(myVel.vv.values)
    vImg=vImg.reshape((vImg.shape[1],vImg.shape[2]))
    print(myVel.vv)
    print(vImg.shape)
else :
    vImg=np.flipud(myVel.vv)


absmax=15000
mxcapped=min(np.percentile(vImg[np.isfinite(vImg)],99),absmax)

sss=vImg.shape
r=(sss[1]+50)/sss[0]
r=max((r,.5))
print(r)
#fig1,ax1=plt.subplots(figsize=(10.*r,10.))
fig1=plt.figure(constrained_layout=True,figsize=(10.*r,10.))
gs=fig1.add_gridspec(12,12)
axImage=fig1.add_subplot(gs[1:9,0:10])
axSub=fig1.add_subplot(gs[11,:])
axTit=fig1.add_subplot(gs[0,:])
axCb=fig1.add_subplot(gs[1:10,10:])
axSub.set_axis_off()
axCb.set_axis_off()
axTit.set_axis_off()
b= myVel.boundsInKm()

imgplot = axImage.imshow(vImg,vmin=0,vmax=mxcapped,extent=(b[0],b[2],b[1],b[3]))
plt.tight_layout()

#

axImage.plot(x[igood],y[igood],'r.')
#print(vx)
#exit()
plt.figure()
#print(v[igood])
plt.plot(v[igood])


