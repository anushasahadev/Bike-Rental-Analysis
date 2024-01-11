#!/usr/bin/env python
# coding: utf-8

# ### Processed Data File Conversion
# #### Contains Normalization-Dummy Variables added & finally converted to 'cleanprocessedata.csv' file

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("cleandata.csv", index_col='datetime', parse_dates=True)
df.head()


# In[3]:


df['windspeed'] = df['windspeed'] / df['windspeed'].max()
df['humidity'] = df['humidity'] / df['humidity'].max()
col = ["temp", "atemp"]
df[col] = (df[col]-df[col].min())/(df[col].max()-df[col].min())
df


# In[4]:


dummy_season = pd.get_dummies(df.season, prefix='season')
dummy_season.sample(n=10,random_state = 12)


# In[5]:


dummy_weather = pd.get_dummies(df.weather, prefix='weather')
dummy_weather.sample(n=10, random_state = 12)


# In[6]:


dummy_hour = pd.get_dummies(df.hour, prefix='hour')
dummy_hour.sample(n=10, random_state = 12)


# In[7]:


df = pd.concat([df, dummy_hour], axis=1)
df = pd.concat([df, dummy_weather], axis=1)
df = pd.concat([df, dummy_season], axis=1)
df.head(10)


# In[8]:


df.drop(['hour','season','weather','atemp','casual','registered'], axis = 1, inplace=True)
df.head(20)


# In[9]:


df.columns


# # Convert To CSV Code

# In[10]:


df.to_csv("cleanprocessed_data.csv",header=True)


# In[11]:


X = df[['holiday', 'workingday', 'temp', 'humidity', 'windspeed',
        'hour_0', 'hour_1', 'hour_2', 'hour_3', 'hour_4', 'hour_5', 'hour_6',
       'hour_7', 'hour_8', 'hour_9', 'hour_10', 'hour_11', 'hour_12',
       'hour_13', 'hour_14', 'hour_15', 'hour_16', 'hour_17', 'hour_18',
       'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23', 'weather_1',
       'weather_2', 'weather_3', 'weather_4', 'season_1', 'season_2',
       'season_3', 'season_4']]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




