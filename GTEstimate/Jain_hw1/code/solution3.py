#!/usr/bin/python
import sys
import matplotlib.pylab as pl                        #defining libraries
import numpy as np
f=open('C:/Python27/Codes/HW1/bigwordlist75k.txt','rU');
freqList=[]
wordList=[]                         #lists that will store frequencies, words and ranks
rankList=[]
i=1
for line in f:
    s=line
    
    word=s.split()                #separating words and frequencies
    wordList.append(word[0])           #storing words
    freqList.append(word[1])                  #storing frequencies
    rankList.append(i)                        # storing ranks
    i=i+1
for i in range(0,len(freqList)):
    freqList[i] = int(freqList[i])
rankList = np.log(rankList)                 #converting to log values
freqList = np.log(freqList)

pl.yscale('log')                           #defining log-log scale of graph
pl.xscale('log')

pl.plot(rankList,freqList)

#pl.axis([0,75000,164438,23135851162])
po=np.polyfit(rankList,freqList,5)              #for the smoothed graph 
yfit = np.polyval(po,rankList)

pl.plot(rankList,yfit)                        #plotting the graph
pl.xlabel('Log Rank')                  
pl.ylabel('Log Frequency')                   # defining labels, titles and legends

pl.suptitle("Solution 3 : Frequency vs Rank")
pl.legend(["Log Frequency vs Log Rank", "Smoothened Graph"])
pl.show()

f.close()    