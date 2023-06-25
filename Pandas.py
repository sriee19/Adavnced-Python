#!/usr/bin/env python
# coding: utf-8

# # Pandas Tutorial

#    Pandas is an open source , easy-to use data structures and data nalysus tools 

# In[2]:


# import pandas 

import pandas as pd
import numpy as np


# In[7]:


# playing with data frames

df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['column1','column2','column3','column4'])


# In[8]:


df.head()


# In[ ]:


## df.to_csv('Test1.csv')


# In[9]:


## Accessing the elements

df.loc['Row1']


# In[10]:


## Check the type

type(df.loc['Row1'])


# In[11]:


df.iloc[:,:]


# In[12]:


## Take the elements from the Column2

df.iloc[:,1:]


# In[13]:


#convert Dataframes into array

df.iloc[:,1:].values


# In[14]:


df['column1'].value_counts()


# In[15]:


df=pd.read_csv('mercedesbenz.csv')


# In[16]:


df.head()


# In[17]:


df.info()


# In[18]:


df.describe()


# In[19]:


#Get the unique category counts

df['X0'].value_counts()


# In[20]:


df[df['y']>100]


# In[21]:


df.corr()


# In[22]:


df['X11'].value_counts()


# In[23]:


lst_data=[[1,2,3],[3,4,np.nan],[5,6,np.nan],[np.nan,np.nan,np.nan]]


# In[24]:


df=pd.DataFrame(lst_data)


# In[25]:


df.head()


# In[27]:


## HAndling Missing Values

##Drop nan values

df.dropna(axis=0)


# In[28]:


df.dropna(axis=1)


# In[29]:


df = pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])


# In[30]:


df.head()


# In[31]:


df2=df.reindex(['a','b','c','d','e','f','g','h'])


# In[32]:


df2


# In[33]:


df2.dropna(axis=0)


# In[34]:


pd.isna(df2['one'])


# In[35]:


df2['one'].notna()


# In[37]:


df2.fillna(0)


# In[38]:


df2['one'].values


# In[39]:


df2['two'].values


# In[40]:


### Reading different data sources with the help of pandas


# # CSV

# In[41]:


from io import StringIO , BytesIO


# In[42]:


data = ('col1,col2,col3\n'
              'x,y,1\n'
              'a,b,2\n'
              'c,d,3')


# In[43]:


type(data)


# In[44]:


pd.read_csv(StringIO(data))


# In[46]:


## Read from specific columns

df = pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3'])


# In[47]:


df.to_csv('Test.csv')


# In[48]:


## Specifying columns data types

data = ('a,b,c,d\n'
       '1,2,3,4\n'
       '5,6,7,8\n'
       '9,10,11')


# In[49]:


print(data)


# In[50]:


df = pd.read_csv(StringIO(data),dtype = object)


# In[51]:


df


# In[52]:


df['a'][1]


# In[53]:


df = pd.read_csv(StringIO(data),dtype={'b':int,'c':np.float,'a':'Int64'})


# In[54]:


df


# In[55]:


df['a'][1]


# In[56]:


## check the datatype

df.dtypes


# In[57]:


## Index columns and training delimiters

data = ('index,a,b,c\n'
       '4,apple,bat,5.7\n'
       '8,orange,cow,10')


# In[58]:


pd.read_csv(StringIO(data),index_col=0)


# In[59]:


data = ('index,a,b,c\n'
       '4,apple,bat\n'
       '8,orange,cow')


# In[60]:


pd.read_csv(StringIO(data))


# In[61]:


pd.read_csv(StringIO(data),index_col=False)


# In[63]:


## Combining usecols and index_col

data = ('a,b,c\n'
       '4,apple,bat\n'
       '8,orange,cow')


# In[64]:


pd.read_csv(StringIO(data),usecols=['b','c'],index_col=False)


# In[65]:


## Quoting and Escape Characters¶. Very useful in NLP

data = 'a,b\n"hello, \\"Bob\\", nice to see you",5'


# In[66]:


pd.read_csv(StringIO(data),escapechar='\\')


# In[67]:


## URL to CSV

df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')


# In[68]:


## Read Json to CSV


# In[69]:


Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
pd.read_json(Data)


# In[70]:


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)


# In[71]:


df.head()


# In[72]:


# convert Json to csv


# In[73]:


df.to_csv('wine.csv')


# In[74]:


# convert Json to different json formats

df.to_json(orient="index")


# In[75]:


df.to_json(orient="records")


# # Reading HTML content

# In[76]:


url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dfs = pd.read_html(url)


# # Reading Excel Files

# In[77]:


de_excel=pd.read_excel('Excel_Sample.xlsx')


# In[78]:


de_excel.head()

