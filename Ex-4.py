#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import seaborn as sns


# In[5]:


df=pd.read_csv("supermarket.csv")
df


# In[7]:


df.info()


# In[30]:


df.isnull().info()


# In[27]:


df.boxplot()


# In[12]:


df["Quantity"].value_counts()


# In[13]:


df["Gender"].value_counts()


# In[20]:


df["Customer type"].value_counts()


# In[14]:


sns.countplot(x="Quantity",data=df)


# In[15]:


sns.countplot(x="Gender",data=df)


# In[16]:


sns.displot(df["gross margin percentage"])


# In[17]:


sns.displot(df["Total"])


# In[19]:


sns.displot(df["Tax 5%"])


# In[25]:


sns.displot(df["Customer type"])


# In[21]:


sns.countplot(x="Customer type",data=df)


# In[23]:


sns.countplot(x="Gender",hue="Customer type",data=df)


# In[26]:


pd.crosstab(df["Gender"],df["Customer type"])


# In[32]:


pd.crosstab(df["Payment"],df["Customer type"])


# In[ ]:


df.drop


# In[29]:


df.corr()


# In[33]:


df.drop("gross margin percentage",axis=1,inplace=True)


# In[34]:


sns.heatmap(df.corr(),annot=True)


# In[ ]:


df.drop("Cabin",axis=1,inplace=True)

