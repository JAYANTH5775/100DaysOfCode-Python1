---
description: >-
  Given  a  string str we need to     find the  minimum  deletions  that can be
  made so that the  character  frequency of the each char is unique
---

# Minimum del to make the char freq unique



```
// Some code
from collections import * 


def minDeletions(str):

    mp = defaultdict(int)

    pq = []

    cntchar = 0 

    for i in str: 
        mp[i] +=1
    
    for it in mp:

        pq.append(mp[it])
    pq = sorted(pq)


    while len(pq) > 0:

        frequent = pq[-1]

        del pq[-1]


        if len(pq) == 0: 

            return cntchar
        if frequent == pq[-1]: 
            if frequent > 1: 

                pq.append(frequent-1)
            cntchar +=1
        pq = sorted(pq)

    return  cntchar

```
