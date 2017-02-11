# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:01:12 2017

@author: arjan
"""
#%%
def pathways(reads,d,k=1,touched=[],endlist=[]):
    
    ''' 
    Pathways by Arjan Groen.
    Pathways gives all the possible combinations of a list of strings/reads by 
    recursively going through all possible routes. 
    reads:      list of all reads
    d:          Dictionary that contains all the reads as keys. The value for each key is a
                   set of follow-up objects.
    touched:    List of reads that have been visited already. 
    k:          In some cases, the dictionary contains substrings of the reads of length k. 
    endlist:    When a pathway branch has used all reads, it is ended to the endlist.
    '''
    
    if touched == []: #initial calling of the function
        nxt = reads #all reads could be the first.
    else:
        r = touched[-1] #starting point is the last visited read.
        nxt = list(d[r[-k:]]) #look up the set possible next reads.
    for n in nxt: #iterate through the possible next reads
        if n not in touched:
            touched.append(n) #read is untouched, at to the list
            if len(touched) == len(reads): #pathway is complete
                if touched not in endlist: 
                    endlist.append(touched) #add pathway
                    touched = touched[:-1] #remove last step to look for other options
            else:
                touched,_ = pathways(reads,d,k,touched,endlist) #read is not complete, find next step            
    del nxt  #clear memory
    return touched[:-1],endlist #remove last step to find new options. 

#%%   
'''SAMPLE EXECUTION'''
    
dtest = {}
dtest["a"] = ["a","b","c"] # a can be followed by a,b,c
dtest["b"] = ["a","d","e"] # b can be followed by a,d,e
dtest["c"] = ["b","d"]
dtest["d"] = ["c","e"]
dtest["e"] = ["a","d"]
dtest["f"]=["a","e"]
testset = ["a","b","c","d","e"]

lastone,total = pathways(testset,dtest,k=1,touched=[],endlist=[])
print("Possible pathways are:  \n",total)



