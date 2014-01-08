import sys

import os
import re
import matplotlib.pylab as pl
import numpy as np

from collections import Counter

def formTokens():
    freqList=[]        #lists that will store frequencies, words and ranks
    wordList=[]
    rankList=[]
    rank=0
    list1=[]
    i=-1
    one_frequency=[]
    sum_frequency=0
    path = 'E:/ASU/Intro to NLP/HW/hw1_data/part1/'  

    
    for dirPath in os.listdir(path):               #loop for eading the part1 text files
        fileName = os.path.join(path, dirPath)
        f=open(fileName,'r');
        
        textFile=f.read()
        
        p=re.compile('\w+-\w+|\w+\'s|\w+')           #defining the RE

        tokens=p.findall(textFile)              #tokenizing the text
        
        for wrd in tokens:
            list1.append(wrd)                  #creating a list storing the tokens
    
           
    
    uniqueList=Counter(list1)                   #list storing word types and their frequencies
    
    wordList=uniqueList.keys()               
    frequencyList=uniqueList.values()          #storing frequencies
    
    print '(a) Tokens of part 1:',wordList
    
    
    list2=[]                                        #same process for part 2
    i2=-1
    one_frequency2=[]
    sum_frequency2=0
    path2 = 'E:/ASU/Intro to NLP/HW/hw1_data/part2/'  

    
    for dirPath2 in os.listdir(path2):
        fileName2 = os.path.join(path2, dirPath2)
        f2=open(fileName2,'r');
        
        textFile2=f2.read()
        
        p2=re.compile('\w+-\w+|\w+\'s|\w+')

        tokens2=p2.findall(textFile2)
        
        for wrd2 in tokens2:
            list2.append(wrd2)
    
           
    
    uniqueList2=Counter(list2)
    
    wordList2=uniqueList2.keys()
    frequencyList2=uniqueList2.values()
    
    print '(a) Tokens of part 2:',wordList2
    
    
                    
    list3=[]              #same as above for part 3
    i3=-1
    one_frequency3=[]
    sum_frequency3=0
    path3 = 'E:/ASU/Intro to NLP/HW/hw1_data/part3/'  

    
    for dirPath3 in os.listdir(path3):
        fileName3 = os.path.join(path3, dirPath3)
        f3=open(fileName3,'r');
        
        textFile3=f3.read()
        
        p3=re.compile('\w+-\w+|\w+\'s|\w+')

        tokens3=p3.findall(textFile3)
        
        for wrd3 in tokens3:
            list3.append(wrd3)
    
           
    
    uniqueList3=Counter(list3)
    
    wordList3=uniqueList3.keys()
    frequencyList3=uniqueList3.values()
    
    print '(a) Tokens of part 3:',wordList3
    
    
    
    
    for freq3 in frequencyList3:          #finding words with frequency 1 in part 3
        i3=i3+1
        if freq3==1:
            one_frequency3.append(wordList3[i3])
            
    
                    
    
    for num3 in frequencyList3:                 # finding total words        
        sum_frequency3=sum_frequency3+num3
    
    probab_newwordtype3=float(len(one_frequency3))/sum_frequency3     #calculating GT estimate
    
    
                
    print '(b) No of word tokens in part 1', len(list1)
    print '(b) No of word types in part 1 :', len(wordList)
    
    for freq in frequencyList:         #words with one frequency in part 1
        i=i+1
        if freq==1:
            one_frequency.append(wordList[i])
            
            
    print '(c) Words with one frequency in part 1 :', len(one_frequency)
    
    for num in frequencyList:
        sum_frequency=sum_frequency+num
    
    probab_newwordtype=float(len(one_frequency))/sum_frequency       #GT estimate of part 1
    print '(d) Probability of new word type of part 1 :', probab_newwordtype
    
    
    for freq2 in frequencyList2:           #one word frequency for part 2
        i2=i2+1
        if freq2==1:
            one_frequency2.append(wordList2[i2])
            
            
    
    for num2 in frequencyList2:
        sum_frequency2=sum_frequency2+num2
    
    probab_newwordtype2=float(len(one_frequency2))/sum_frequency2    # GT estimate for part 2
    
    print '(e) Percentage of new word type addition in part 2 :', (probab_newwordtype2)*100
    print '(e) Percentage of new word type addition in part 1 :', (probab_newwordtype)*100
    print '(e) Difference in percentage between part 2 and part 1 :', ((probab_newwordtype2)*100)-((probab_newwordtype)*100)
    
    
    book2by3WordToken=len(list1)+len(list2)                      #finding word tokens and word types in part 1+part 2
    book2by3WordType=len(wordList)+len(wordList2)
    
    print '(f) No of word tokens in part 1 and part 2', book2by3WordToken
    print '(f) No of word types in part 1 and part 2 :', book2by3WordType
    
    
    freqone2by3=len(one_frequency)+len(one_frequency2)
    
    print '(g) Words with one frequency in part 1 and part 2 :', freqone2by3         #finding words with one frequency in part 1+part 2
    
    totalwordsin1and2=sum_frequency+sum_frequency2
    onefreqin1and2=len(one_frequency)+len(one_frequency2)
    probab_new_word_1and2=float(onefreqin1and2)/totalwordsin1and2
    
    print '(h) Probability of new word type of first 2/3rd of the book :', probab_new_word_1and2
    
    
    print '(i) Percentage of new word type of last 1/3rd of the book :', (probab_newwordtype3)*100
    print '(i) Percentage of new word type of first 2/3rd of the book :', (probab_new_word_1and2)*100
    print '(i) Difference between last 1/3rd part and first 2/3rd part :', ((probab_newwordtype3)*100)-((probab_new_word_1and2)*100)
    
    
    list=list1+list2+list3
    
    uniqueListfinal=Counter(list)
    
    l = uniqueListfinal.items()
    l.sort(key = lambda item: item[1])
   
    #l=uniqueListfinal.items()
    #l.sort()
    
    #print l
    
    for ce in range(len(l)-1,0,-1):                   # ordering frequencies according to decreasing ranks
        rank=rank+1
        rankList.append(rank)
        
        freqList.append(l[ce][1])
        #freqList.append(ce[1])
        
    
    
    
    for i in range(0,len(freqList)):
        freqList[i] = int(freqList[i])

    
    rankList = np.log(rankList)
    freqList = np.log(freqList)                #converting to log values

    pl.yscale('log')
    pl.xscale('log')                  #defining log-log scale of graph


    pl.plot(rankList,freqList)
    
    po=np.polyfit(rankList,freqList,2)           #for the smoothed graph 
    yfit = np.polyval(po,rankList)
    pl.plot(rankList,yfit)                       #plotting the graph
    pl.xlabel('Log Rank')                    #defining labels, titles and legends
    pl.ylabel('Log Frequency')
    
    pl.suptitle("Solution 4 : Frequency vs Rank of entire corpus")
    pl.legend(["Log Frequency vs Log Rank", "Smoothened Graph"])
    
    #pl.axis([0,75000,164438,23135851162])
    pl.show()

    
    
if __name__=='__main__':
    formTokens()
    
        
    