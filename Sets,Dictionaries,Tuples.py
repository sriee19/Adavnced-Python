#!/usr/bin/env python
# coding: utf-8

# # Sets

# A set is an unordered collection data type that is iterable ,mutable, and has no duplicate elements.
# Python set class represents the mathematical notion of a ste. This is based on a data structure known as a hash table

# In[1]:


# Defining an empty set


# In[3]:


set_var = set()
print(set_var)
type(set_var)


# In[4]:


print(type(set_var))


# In[5]:


set_var = {"avengers", "Endgame", "Hitman"}
print(set_var)
type(set_var)


# In[6]:


#indexing (we cannot index in a set)


# In[7]:


set_var["avengers"]


# In[8]:


#inbuilt functions in a set


# In[9]:


set_var.add("Hulk")


# In[10]:


set_var


# In[11]:


#intersectionupdate


# In[14]:


set1= {"Thor","Hulk", "Spiderman"}
set2 = {"Hulk","Spiderman","Capton"}


# In[15]:


#Difference
set2.difference_update(set1)


# In[16]:


print(set2)


# In[17]:


print(set1)


# # Dictionaries

# A dictionary is a collection which is unordered and indexed.In python dictionaries are writtern with curly brackets

# In[18]:


dic = {}


# In[19]:


type(dic)


# In[20]:


dic = {1,2,3,4,5}


# In[21]:


type(dic)


# In[22]:


# lets create a dictionary
dicts ={"car1" : "audi", "car2" : "mercedes"}


# In[23]:


type(dicts)


# In[25]:


#access the item values based on keys
dicts['car1']


# In[26]:


# we can even loop throught the dictionaries keys

for x in dicts:
    print(x)


# In[27]:


for x in dicts.items():
    print(x)


# In[28]:


for x in dicts.values():
    print(x)


# In[29]:


dicts['car3']='nano'


# In[30]:


dicts


# # Nested Dictionaries 

# In[31]:


car1_model = {'audi':1978}
car2_model={'maruthi':1950}
car3_model={'nano':2012}

car = {'car1':car1_model,'car2':car2_model,'car3':car3_model}


# In[32]:


print(car)


# In[33]:


## Accessing the items in the dictionaries

print(car['car1'])


# In[34]:


print(car['car1']['audi'])


# # Tuples

# In[35]:


# create an empty tuples


# In[36]:


my_tuple = tuple()


# In[37]:


type(my_tuple)


# In[38]:


my_tuple = ("sanjana" , "sri" , "hrithu")


# In[39]:


my_tuple[1]


# In[40]:


print(type(my_tuple))


# In[41]:


print(my_tuple)


# In[42]:


#inbuild function


# In[43]:


my_tuple.count("sanjana")


# In[44]:


my_tuple.index("sri")


# In[ ]:




