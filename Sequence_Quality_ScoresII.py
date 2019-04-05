#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:56:10 2018

@author: luishdz
"""
#%%
import numpy as np
import pandas as pd
import re
import os
WorkingDirectory='/Users/luishdz/Documents/TemporalLIIGH/MezcalYeastunzip/'

Names=os.listdir(WorkingDirectory)
FinalScores=[]
for x in range (len(Names)):
    #Open and save in a list TOI from txt file
    f=open(WorkingDirectory+Names[x]+'/fastqc_data.txt','r')
    #f=open('/Users/luishdz/Documents/TemporalLIIGH/TemporalData/fastqc_data05.txt','r')
    #Txt file is saved in a list
    lines=f.readlines()
    SequenceGCcontent=[]
    Max=len(lines)
    for i in range (Max):
        if lines[i] == '>>Per sequence GC content\tpass\n' or lines[i] == '>>Per sequence GC content\tfail\n' or lines[i]== '>>Per sequence GC content\twarn\n':
            i=i+1
            for i in range (i,Max):
                if lines[i] == '>>END_MODULE\n':
                    break
                SequenceGCcontent.append(lines[i])
#%%
    #Values of interest are saved in a list [SequenceQuality2]
    Max2=len(SequenceGCcontent)
    SequenceGCcontent2=[]
    
    for ii in range (1,Max2):
        t=[int(s) for s in re.findall(r'\b\d+\b', SequenceGCcontent[ii])]
        SequenceGCcontent2.append(t[1])
    #%%
    #Maximum value is localized to establish a point of symmetry
    Symmetry=max(SequenceGCcontent2)
    
    for iii in range(Max2):
        if SequenceGCcontent2[iii] == Symmetry:
            SymmetryListValue=iii
            break
    #%%    
    #Do accumulative substract [left side minus right side]
    jj=SymmetryListValue-1
    AccumulateSubstraction=[]
    length=len(SequenceGCcontent2)
    for j in range(SymmetryListValue, (SymmetryListValue * 2)-1):
        substract=SequenceGCcontent2[jj] - SequenceGCcontent2[j+1]
        AccumulateSubstraction.append(substract)
        jj=jj-1 
    #%%
    #Total Accumulative Substract is done
    FAS=0
    for k in range(len(AccumulateSubstraction)):
        FAS=FAS + AccumulateSubstraction[k]
        
    FinalScores.append((Names[x],FAS))

myarray=np.asarray(FinalScores)
np.save('myarray', myarray)
df=pd.DataFrame(myarray)
df.to_csv("file.csv")
    


'''MISSING TASKS'''
# 1) Unzip all R1 files [done]
# 2) For loop in this script to calculate FAS values from 1 [missing]
# 3) Save FAS values and names in Excel sheet [missing]
# 4) May be an additional script will be necesary to correlate FAS values with
#    data in Excel [missing]

'''New missing tasks'''
# 1) Access to one folder in MezcalYeastunzip directory
# 2) Save folder name
# 3) Read file fastqc_data.txt
# 4) Run current script
# 5) Save FAS value
# 6) Repeat