#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


df = pd.read_csv("bikeshare.csv", index_col='datetime', parse_dates=True)
df.head()


# In[25]:


df.shape


# In[26]:


df.describe()


# In[27]:


#def  a func called plot_boxplot

def plot_boxplot(df, ft):
    df.boxplot(column=[ft])
    plt.grid(False)
    plt.show()


# In[28]:


plot_boxplot(df,'temp')


# In[29]:


plot_boxplot(df,'humidity')


# In[30]:


plot_boxplot(df,'windspeed')


# In[31]:


plot_boxplot(df,'rentals')


# ## Remove Outliers

# In[32]:


def outliers(df, ft):
    Q1 = df[ft].quantile(0.25)
    Q3 = df[ft].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    ls = df.index[ (df[ft] < lower_bound) | (df[ft] > upper_bound) ]
    
    return ls


# In[33]:


#cr8 empty list to store the output indices from multiple columns 

index_list = []
for feature in ['temp','humidity','windspeed','rentals']:
    index_list.extend(outliers(df, feature))


# In[34]:


index_list


# In[35]:


# define a func remove which removes outleiers

def remove(df, ls):
    ls = sorted(set(ls))
    df = df.drop(ls)
    return df


# In[36]:


df_cleaned = remove(df, index_list)


# In[37]:


df_cleaned.shape


# In[38]:


plot_boxplot(df_cleaned,'temp')


# In[39]:


plot_boxplot(df_cleaned,'humidity')


# In[40]:


plot_boxplot(df_cleaned,'windspeed')


# In[41]:


plot_boxplot(df_cleaned,'rentals')


# In[42]:


df_cleaned.to_csv('cleandata.csv',header=True)


# In[ ]:





# In[ ]:




