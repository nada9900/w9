#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib # imports library with SHA-256 hashing algocopy
import datetime # imports library to track time
t1 = datetime.datetime.now() # start time
nonce = 1 # Starts the nonce at 1
solution = False
while solution == False: # loop until true
    ourhash = hashlib.sha256(str(nonce).encode()).hexdigest() # inputs nonce into hash function
    if ourhash[:7] == '0000000': # look for hash with 7 proceeding zeros
        solution =True # those who find the solution will have 'proved' they put in 'work'
    nonce +=1 # increase nonce by 1 and try again
t2 = datetime.datetime.now() # end time
duration = t2 - t1 # time elapsed
print ("The hash is:",ourhash)
print ("The nonce is:",nonce)    
print ("Time elapsed:",duration)


# In[2]:



while solution == False: # loop until true
    ourhash = hashlib.sha256(str(nonce).encode()).hexdigest() # inputs nonce into hash function
    if ourhash[:8] == '00000000': # look for hash with 8 proceeding zeros
        solution =True # those who find the solution will have 'proved' they put in 'work'
    nonce +=1 # increase nonce by 1 and try again
t2 = datetime.datetime.now() # end time
duration = t2 - t1 # time elapsed
print ("The hash is:",ourhash)
print ("The nonce is:",nonce)    
print ("Time elapsed:",duration)



# In[ ]:




