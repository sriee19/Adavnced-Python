#!/usr/bin/env python
# coding: utf-8

# # Python Data Structures and Boolean

# Boolean
# Boolean and logical operators
# lists
# comparisonoperators
# dictionaries
# tuples
# sets

# # BOOLEAN VARIABLES

# Boolean variables are the constant objects false and true
They are used to represent truth values 
# In[1]:


print(True,False)


# In[2]:


type(True)


# In[3]:


type(False)


# In[4]:


my_str='sanjana'


# In[7]:


print(my_str.capitalize())
print(my_str.isalnum())
print(my_str.isalpha())
print(my_str.islower())
print(my_str.istitle())


# In[9]:


print(my_str.endswith('a'))
print(my_str.startswith('a'))


# # Booleean and 	Logical Operators

# In[10]:


True and True


# In[11]:


True and False


# In[12]:


True or True


# In[14]:


True or False


# In[15]:


example = 'hello world'
str = 'sanjana'


# In[16]:


str.isalpha() or example.isnum()


# In[17]:


str.isalpha() and example.isnum()


# # Lists

# A list is a dtata structure in pytho that is a mutable or changable , ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as charactres between quotes, lists are defined by having values between sqyare brackets[]

# In[18]:


lst_example = []


# In[19]:


type(lst_example)


# In[20]:


lst = list()


# In[21]:


type(lst)


# In[23]:


lst = ['maths','english','science','social']


# In[24]:


len(lst)


# APPEND

# In[25]:


lst.append("tamil")


# In[26]:


lst


# In[27]:


#Indexing in list


# In[28]:


lst[2]


# In[29]:


lst[:2]


# In[30]:


lst[1:]


# In[31]:


#INSERT


# In[32]:


lst.insert(0,'Comp')


# In[33]:


lst


# In[34]:


len(lst)


# In[35]:


lst.append("scores", "subjects")


# In[36]:


# Extend Method


# In[37]:


lst = [1,2,3,4,5,6]


# In[39]:


lst.extend([7,8])


# In[40]:


lst


# In[41]:


#Various Operations that we perform on the lists


# In[42]:


lst = [1,2,3,4,5]


# In[43]:


sum(lst)


# In[44]:


#pop()method


# In[45]:


lst.pop()


# In[46]:


lst


# In[47]:


lst.pop(0)


# In[48]:


lst


# In[51]:


lst.insert(0,1)


# In[52]:


lst


# In[53]:


lst.pop(1)


# In[54]:


lst


# In[55]:


#count(): Calculates totl occurence of given element of list


# In[56]:


lst =[1,2,2,4,2,6]
lst.count(2)


# In[57]:


#len(): Calculates the length of the list


# In[60]:


len(lst)


# In[61]:


#index(): Retuens the index of the first occurence


# In[62]:


lst.index(1)


# In[63]:


#min & max


# In[64]:


min(lst)


# In[65]:


max(lst)


# In[ ]:




