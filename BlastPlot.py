#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:24:43 2018

@author: luishdz
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import time
start = time.time()
#%%

ap = argparse.ArgumentParser()
ap.add_argument("-x", "--x_data", required=True,
	help="path to X data")
ap.add_argument("-y", "--y_data", required=True,
	help="path to Y data")
ap.add_argument("-b", "--blast_data", required=True,
	help="path to Blast data")
args = vars(ap.parse_args())


X=pd.read_table(args["x_data"])
Y=pd.read_table(args["y_data"])
B=pd.read_table(args["blast_data"])
B.columns=['Xoffset','Yoffset','Identity','D','E','F','X','H','Y','J','K','L']

X_Names=[]
Y_Names=[]
B_Names=[]

print('%%%%%%%%%%%   Loading files......   %%%%%%%%%%%%%%%%%')

for i in X.columns.values:
    if i == '#Scaffold' or i == 'Decalage':
        pass
    else:
        X_Names.append(i)
        
for i in Y.columns.values:
    if i == '#Scaffold' or i == 'Decalage':
        pass
    else:
        Y_Names.append(i)

for i in B.columns.values:
    if i == 'Xoffset' or i == 'Yoffset' or i == 'Identity' or i == 'X' or i == 'Y':
        pass
    else:
        B_Names.append(i)
        
X=X.drop(X_Names, axis=1)
Y=Y.drop(Y_Names, axis=1)
B=B.drop(B_Names, axis=1)
#%%
#Color assignment
red='#FF0000'
black='#000000'
blue='#000000FF'
gray='#808080'

#Area assignemnt
area=0.0001
Alpha=0.5
#%%
X=X.set_index('#Scaffold')
Y=Y.set_index('#Scaffold')
#%%
my_dpi=200
Xlist=[]
Ylist=[]
Hex_colors=[]
#plt.ioff()
#plt.figure(figsize=(1200/my_dpi, 1200/my_dpi), dpi=my_dpi)
print('%%%%%%%%%%%   Working on graph   %%%%%%%%%%%%%%%%%')

#%%
#List for X and Y values
for i in range(len(B)):
    #print(i)
    #Save offset index from blast file
    offset_X=B.loc[i,'Xoffset']
    offset_Y='>'+B.loc[i,'Yoffset']
    #Search index for offset value 
    offset_X=X.loc[offset_X,'Decalage'] 
    offset_Y=Y.loc[offset_Y,'Decalage']
    #X & Y points
    x=B.loc[i,'X']+offset_X
    y=B.loc[i,'Y']+offset_Y
    identidad=int(B.loc[i,'Identity'])   
    if 98<=identidad<=100:
        Hex_colors.append(red)
    elif 95<=identidad<98:
        Hex_colors.append(black)
    elif 90<=identidad<95:
        Hex_colors.append(blue)
    else:
        Hex_colors.append(gray)    
    Xlist.append(x)
    Ylist.append(y)
#%%
print('%%%%%%%%%%%   Almost done   %%%%%%%%%%%%%%%%%')
plt.scatter(Xlist,Ylist,s=area,color=Hex_colors,alpha=Alpha)

Vertical=X.loc[:,'Decalage']
Horizontal=Y.loc[:,'Decalage']

#Vertical offset
for i in range(1,len(Vertical)):
    value=Vertical[i]
    plt.axvline(x=value,linewidth=0.2)

#Horizontal offset
for i in range(1,len(Horizontal)):
    value=Horizontal[i]
    plt.axhline(y=value,linewidth=0.2)

plt.savefig('Test_plot.png',dpi=my_dpi)

end = time.time()
print(end - start)    
    

