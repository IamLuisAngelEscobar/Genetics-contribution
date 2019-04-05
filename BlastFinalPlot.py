#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:55:21 2018

@author: luishdz
"""

import matplotlib.pyplot as plt
import pandas as pd

#Import library
B=pd.read_csv('BlastFinal.csv')
#B=pd.read_csv('Blast4Test.csv')
X=pd.read_csv('Xdata.csv')
Y=pd.read_csv('Ydata.csv')
#%%
#Color assignment
red='#FF0000'
black='#000000'
yellow='#FFFF00'
blue='#000000FF'
gray='#808080'
gray2='#A9A9A9'
gray3='#BEBEBE'
gray4='#C0C0C0'
gray5='#D3D3D3'
#Area assignemnt
area=1
#%%
X=X.set_index('#Scaffold')
Y=Y.set_index('#Scaffold')
#%%
#my_dpi=96
my_dpi=200
plt.figure(figsize=(1200/my_dpi, 1200/my_dpi), dpi=my_dpi)
#%%
#List for X and Y values
for i in range(len(B)):
    #Save offset index from blast file
    offset_X=B.loc[i,'Xoffset']
    offset_Y='>'+B.loc[i,'Yoffset']
    #Search index for offset value 
    offset_X=X.loc[offset_X,'Decalage'] 
    offset_Y=Y.loc[offset_Y,'Decalage']
    #X & Y points
    x=B.loc[i,'X']+offset_X
    y=B.loc[i,'Y']+offset_Y
    identidad=B.loc[i,'Identidad']
    if 98<=identidad<=100:
        plt.scatter(x,y,s=area,color=red)
    elif 95<=identidad<98:
        plt.scatter(x,y,s=area,color=black)
    elif 90<=identidad<95:
        plt.scatter(x,y,s=area,color=yellow)
    elif 80<=identidad<90:
        plt.scatter(x,y,s=area,color=gray)
    elif 80<=identidad<90:
        plt.scatter(x,y,s=area,color=gray2)
    elif 70<=identidad<80:
        plt.scatter(x,y,s=area,color=gray3)
    elif 60<=identidad<70:
        plt.scatter(x,y,s=area,color=gray4)
    else:
        plt.scatter(x,y,s=area,color=gray5) 
        #print('Here be dragons')
    plt.savefig('Test_plot.png',dpi=my_dpi)    
#%%
#plt.savefig('Test_plot.png')