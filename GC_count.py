#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:39:05 2018

@author: luishdz
"""
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to fq file")
args=vars(ap.parse_args())

#f=open('/Users/luishdz/Documents/TemporalLIIGH/G499_FY4_R1.fastx.fq','r')

f=open(args["--input"], 'r')
lines=f.readlines()

MaxValue=len(lines)
GClist=[]
UnnecessaryList=[]
#Con excepción de la primer iteración sumar 4 y leer 2 
for i in range(0,len(lines),4):
        header=lines[i]
        Sequence=lines[i+1]
        Separator=lines[i+2]
        Quality=lines[i+3]
        GC=0; ATN=0
        for ii in range(len(Sequence)):
            if Sequence[ii]=='G' or Sequence[ii]=='C':
                GC=GC+1
            elif Sequence[ii]=='A' or Sequence[ii]=='T' or Sequence[ii]=='N':
                ATN=ATN+1
            elif Sequence[ii]=='$' or Sequence[ii]== '\n':
                break
            else:
                print('Here be dragons ' + str(i) + '\n' + header)
                
        AmountGC=GC/(GC+ATN)
        if AmountGC <= 0.14:
            GClist.append((header))
            GClist.append((Sequence))
            GClist.append((Separator))
            GClist.append((Quality))

        else:
            UnnecessaryList.append(AmountGC)
            
if not GClist:
    print('Any Sequence meet the condition [Amount of GC <= 14%]')
else:
    file=open('New_fastq.fq','w')
    for i in range(len(GClist)):
        file.write(GClist[i])
    file.close()
    #myarray=np.asarray(GClist)
    #df=pd.DataFrame(myarray)
    #df.to_csv('test.csv')
    print('Fq was saved')
    
