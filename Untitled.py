#!/usr/bin/env python
# coding: utf-8

# In[4]:



print("hello")


# In[5]:


import pandas
data = pandas.read_csv('1._Regression_-_Module_-_(Housing_Prices)[1].csv')
data.head()
# gives first 5 rows


# In[8]:


data.info()
# gives all info about dataset


# In[9]:


data.dtypes
# gives us datatyes or variable type involved in dataset 


# In[10]:


data.describe()
# gives description about all numerical values for descriptive analysis
# i.e count,mean,SD,max etc


# In[11]:


data['Sale Price'].mean()
# gives the mean value for sale price column


# In[16]:


data['Sale Price'].max()
# gives the max value for sale price column


# In[15]:


data['Sale Price'].min()
# gives the min value for sale price column


# In[22]:


data['Sale Price'].quantile(.25)
# gives the quantile value (1,2 & 3) for sale price column


# In[17]:


data['Sale Price'].std()
# gives the standard deviation value for sale price column


# In[24]:


data['Condition of the House'].unique()
# gives us all unique strings for Condition of the House column


# In[27]:


import numpy as np
np.std(data['Sale Price'])
# calculating SD using numpy


# In[28]:


np.std(data['Sale Price']) - data['Sale Price'].std()
# diffrence in calculation of SD by numpy std() and inbuilt std()


# In[29]:


np.std(data['Sale Price'],ddof=1) - data['Sale Price'].std()
# now we will get both same by specifying degree of freedom ddof = 1


# In[30]:


dir(np)
# list of function in numpy library

