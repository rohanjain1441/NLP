#!/usr/bin/env python
import numpy as np
import nltk
from numpy import zeros, float32                                  #importing libraries
import sys, hmmtrain
import itertools

class hmm:
    
            
    def __init__(self):
        priors, transitions, emissions, states, symbols = hmmtrain.train()
        self.priors = priors
        self.transitions = transitions
        self.emissions = emissions
        self.states = states
        self.symbols = symbols
    
 ####
    # ADD METHODS HERE
    
    def cartesian(self,arrays, out=None):                     #function to calculate cartesian product of all the tags
        
        return itertools.product(*arrays)
        
    
        
            
                
                                                                            
    def exhaustive(self):
        
        lenArray=7
        logsum=0
        flag=0
        max1=-5000000000000
        #max1=np.log2(1e-500)
        self.userSentence=raw_input("Enter a Sentence").lower()                    #stores lower case user sentence
        wordBreak=nltk.word_tokenize(self.userSentence)                             #tokenizes the words
        
                
        x=np.zeros(shape=(len(wordBreak),lenArray), dtype=object)                  #array to store words and its tags
        strearr=np.zeros(shape=(1,len(wordBreak)), dtype=object)                
        #z=np.zeros(shape=(pow(5,lenArray),5), dtype=object)
        z=np.zeros(shape=(7,len(wordBreak)), dtype=object)                          #array to store cartesian product of tags
        #z=np.zeros(shape=(pow(lenArray,len(wordBreak)),len(wordBreak)), dtype=object)
        #z=np.ndarray()
        
        i=-1
        j=-1
        
        for word in wordBreak:                         #loop for finding possible tags for each word
            i=i+1
            j=-1
            for state in self.states:                
                
                val=self.emissions[state].logprob(word)
                
                if val>=np.log2(1e-4):
                    j=j+1
                    x[i][j]=state
                    
                
        #print x     
        za=self.cartesian(x,None)                 #finds cartesian product for all tags
        #print z
        #for ia in z:
         #   print ia[0][1]
        
        
        z = [item for item in za]                         
        
        
        for u in range(0,len(z)):                     #loop for finding most probable tag for every token
            
            for chk in range(0,len(wordBreak)):
                if z[u][chk]==0:
                    flag=1                            #flag for checking if it is the first word
                
            
            if flag==0:
                
                
                logsum=0
                start=self.priors.logprob(z[u][0])
                logsum=logsum+start
                logsum=logsum+self.emissions[z[u][0]].logprob(wordBreak[0])            #calculating emmission probabaility for first token
                
                for v in range(1,len(wordBreak)+1):
                    
                    
                    #if z[u][v]!=0:
                        
                        #doing max computations.
                    
                    if v==len(wordBreak):
                        
                        if logsum>max1:
                            
                            max1=logsum
                            
                            for p in range(0,v):                
                                strearr[0][p]=z[u][p]          #array storing all probable tag sequences
                                
                    
                    
                    else:     
                        logsum=logsum+self.transitions[z[u][v-1]].logprob(z[u][v])
                        logsum=logsum+self.emissions[z[u][v]].logprob(wordBreak[v])              #calculating probabilities for other tags
                    
                        
            
            
                                                        
        print max1
        print strearr               #printing
        
            
    def decode(self, sent):
        maxstart1=-5000000000000
        maxcost=-50000000000
        logsum=0
        #self.userSentence=raw_input("Enter a Sentence").lower()
        self.userSentenceUp=sent                          #input from text file one line
        self.userSentence=sent.lower()
        wordBreak=nltk.word_tokenize(self.userSentence)             #storing lower case
        wordBreakUp=nltk.word_tokenize(self.userSentenceUp)        #storing normal case
        
        x=np.zeros(shape=(2,len(wordBreak)), dtype=object)      #forming array for storing max tags and max Viterbi path parobabilities
        counter=0
        j=0
        for word in wordBreak:                                   # loop for finding max Viterbi path probability
            maxcost=-50000000000
            if counter==0:
                counter=counter+1

                for state in self.states:
                    startCost=self.priors.logprob(state)+self.emissions[state].logprob(wordBreak[0])          #calculating probability for first word with each tag
                    if startCost>maxstart1:                            #checking for max Viterbi path probability tag
                        maxstart1=startCost
                        maxstartstate=state

                x[0][j]=maxstartstate                     #assigning max
                x[1][j]=maxstart1
                j=j+1
            
            
            else:
                for state in self.states:                        #loop for other tokens
                    cost=x[1][j-1]+self.transitions[x[0][j-1]].logprob(state)+self.emissions[state].logprob(word)
                    if cost>maxcost:
                        maxcost=cost
                        maxstate=state

                x[0][j]=maxstate
                x[1][j]=maxcost                     #assigning max tag and probability
                j=j+1
        
        for i in range(0,len(wordBreak)):
            #print wordBreak[i]#x[0][i]                         #printing 
            print "",wordBreakUp[i],"/",x[0][i],
         
        print ""   
    
                 
                
            
    def tagViterbi(self):
        f=open('E:\ASU\Intro to NLP\HW\HW2\Jain_hw2\sentences.txt','rU');         #mention the path here
        
        for self.line in f:                                          
            self.decode(self.line)                     #calling the decode function for every line in text file
            
         #   word=nltk.word_tokenize(self.line)
            
          #  for i in range(0,len(word)):
            
        
   
    ####
    


def main():
    # Create an instance
    model = hmm()
   # model.exhaustive()
    model.tagViterbi()                           #uncomment the function you wish to execute
    
    
    
if __name__ == '__main__':
    main()
