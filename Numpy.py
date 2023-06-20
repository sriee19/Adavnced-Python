#!/usr/bin/env python
# coding: utf-8

# # Numpy Tutorials

# Numpy is a general purpose array processing package. It provides a high performance multidimentional array object, and tools for working with these arrays. It is the fundamentals package for scientific computing with python

# In[1]:


## Initially lets import numpy

import numpy as np


# In[2]:


my_lst = [1,2,3,4,5]

arr = np.array(my_lst)


# In[3]:


type(arr)


# In[4]:


print(arr)


# In[5]:


arr.shape


# In[6]:


arr


# In[8]:


type(arr)


# In[9]:


#multinested aray

my_lst1 = [1,2,3,4,5]
my_lst2 = [2,3,4,5,6]
my_lst3 = [3,4,5,6,7]

arr = np.array([my_lst1,my_lst2,my_lst3])


# In[10]:


arr


# In[11]:


arr.shape


# In[13]:


arr.reshape(5,3)


# In[14]:


# check again the shape of the array

arr.shape


# # Indexing

# In[15]:


#Accessing the array elements


# In[16]:


arr = np.array([1,2,3,4,5,6,7,8])


# In[17]:


arr[3]


# In[18]:


arr


# In[19]:


arr[1:3:]


# In[21]:


arr = np.arange(0,10)


# In[22]:


arr


# In[23]:


#copy function

arr[3:]=100


# In[24]:


arr


# In[25]:


array = np.arange(0,10,step=2)


# In[26]:


array


# In[27]:


array[4:]=10


# In[28]:


array


# In[29]:


np.linspace(1,10,50)


# In[30]:


arr1=arr.copy()


# In[31]:


print(arr)
arr1[3:]=1000
print(arr1)


# In[32]:


arr


# In[33]:


## some conditions very useful in exploratory data analysis


# In[37]:


val=100

arr[arr<val]


# In[38]:


arr<val


# In[39]:


## create arrays and reshape


# In[40]:


np.arange(0,10).reshape(5,2)


# In[ ]:




