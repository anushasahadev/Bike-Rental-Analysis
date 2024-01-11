#!/usr/bin/env python
# coding: utf-8

# ### Exploratory Data Analysis 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("bikeshareda.csv", index_col='datetime', parse_dates=True)


# In[4]:


dfc = df.copy()


# In[5]:


dfc.head()


# In[6]:


dfc.info()


# In[7]:


dfc.describe()


# # Distribution of Variables

# In[12]:


sns.set_style('whitegrid')


plt.figure(figsize=(12, 6))
ax1 = sns.histplot(df['temp'], bins=28, kde=True, color="skyblue")
ax1.set_title('Distribution Graph for Actual Temperature', fontsize=20)
ax1.set_xlabel('Variable temp', fontsize=15)
ax1.set_ylabel('Density of Probability', fontsize=15)
ax1.tick_params(labelsize=12)
sns.despine()
plt.show()


# In[13]:


sns.set_style('whitegrid')


plt.figure(figsize=(12, 6))
ax2 = sns.histplot(df['atemp'], bins=28, kde=True, color="lightcoral")
ax2.set_title('Distribution Graph for "Feels Like" Temperature', fontsize=20)
ax2.set_xlabel('Variable atemp', fontsize=15)
ax2.set_ylabel('Density of Probability', fontsize=15)
ax2.tick_params(labelsize=12)
sns.despine()
plt.show()


# In[15]:


sns.set(style="whitegrid")  


plt.figure(figsize=(12, 7))
ax = sns.histplot(df['humidity'], bins=30, kde=True, color="skyblue")


ax.set_title('Distribution Graph', fontsize=20)
ax.set_xlabel('Variable humidity', fontsize=15)
ax.set_ylabel('Density of Probability', fontsize=15)


ax.tick_params(labelsize=12)


sns.despine()

plt.show()  # Display the plot


# In[17]:


sns.set(style="whitegrid")  

plt.figure(figsize=(12, 7))
ax = sns.histplot(dfc['windspeed'], bins=20, kde=True)


ax.set_title('Distribution Graph', fontsize=20)
ax.set_xlabel('Variable windspeed', fontsize=15)
ax.set_ylabel('Density of Probability', fontsize=15)


ax.set_xlim(0, 60)


ax.tick_params(labelsize=12)


sns.despine()

plt.show() 


# In[20]:


sns.set(style="whitegrid") 


plt.figure(figsize=(12, 7))
ax = sns.histplot(dfc['rentals'], bins=20, kde=True, stat="density", color="skyblue")


ax.set_title('Distribution Graph', fontsize=20)
ax.set_xlabel('Variable rentals', fontsize=15)
ax.set_ylabel('Density of Probability', fontsize=15)


ax.tick_params(labelsize=12)


sns.despine()


ax.set(yticklabels=[])
ax.set_ylabel('')

plt.show()  


# In[23]:


sns.set(style="whitegrid")  
plt.figure(figsize=[12,6])


colors = ["springgreen", "lightcoral", "lightskyblue", "goldenrod"]


plt.figure(figsize=(10, 6))
plt.bar(x=df['season'].value_counts().keys(), 
        height=df['season'].value_counts(), 
        color=colors)

plt.xlabel('Number of Season', fontsize=15)
plt.ylabel('Number of Observations', fontsize=15)
plt.xticks(ticks=[1, 2, 3, 4], labels=['Spring', 'Summer', 'Fall', 'Winter'], fontsize=12)

plt.show()


# In[27]:


colors = ["lightcoral", "lightskyblue"]

holiday_counts = dfc['holiday'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(x=holiday_counts.index, height=holiday_counts.values, color=colors)

plt.xticks(ticks=holiday_counts.index, labels=['No', 'Yes'], fontsize=12)

plt.xlabel('Feature - holiday', fontsize=15)
plt.ylabel('Number of observations', fontsize=15)
plt.title('Holiday Distribution', fontsize=15)

plt.show()


# In[28]:


colors = ["lightcoral", "lightskyblue"]


workingday_counts = dfc['workingday'].value_counts().sort_index()


plt.figure(figsize=(7, 6))
plt.bar(x=workingday_counts.index, height=workingday_counts.values, color=colors)


plt.xticks(ticks=workingday_counts.index, labels=['Holiday', 'Day is neither weekend nor holiday'], fontsize=12)


plt.xlabel('Feature - workingday', fontsize=15)
plt.ylabel('Number of observations', fontsize=15)
plt.title('Working Day Distribution', fontsize=15)


plt.show()
plt.show()


# In[30]:


colors = ["springgreen", "lightcoral", "lightskyblue", "goldenrod"]

weather_counts = dfc['weather'].value_counts().sort_index()

plt.figure(figsize=(9, 5))
plt.bar(x=weather_counts.index, height=weather_counts.values, color=colors)


plt.xticks(ticks=weather_counts.index, labels=['Condition-1', 'Condition-2', 'Condition-3', 'Condition-4'], fontsize=12)


plt.xlabel('Feature - weather', fontsize=15)
plt.ylabel('Number of observations', fontsize=15)
plt.title('Weather Conditions Distribution', fontsize=15)


plt.show()


# # Bivariate Analysis for Target Variable (rentals)

# In[31]:


palette = ["springgreen", "lightcoral", "lightskyblue", "goldenrod"]

plt.figure(figsize=(8, 7))
sns.boxplot(x='season', y='rentals', data=dfc, palette=palette)
plt.xlabel('Seasons', fontsize=15)
plt.ylabel('Number of Bike Rentals', fontsize=15)
plt.title('Bike Rentals Based on Season Feature', fontsize=15)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Winter', 'Spring', 'Summer', 'Fall'])
plt.show()


# In[33]:


palette = ["springgreen", "lightcoral", "lightskyblue", "goldenrod"]

plt.figure(figsize=(10, 7))
sns.boxplot(x='hour', y='rentals', data=dfc, palette=palette*2) 
plt.xlabel('Hourly', fontsize=15)
plt.ylabel('Number of Bike Rentals', fontsize=15)
plt.title('Bike Rentals Based on Hour Feature', fontsize=15)
plt.show()


# In[34]:


palette = ["springgreen", "lightcoral", "lightskyblue", "goldenrod"]
plt.figure(figsize=(10, 7))
sns.boxplot(x=dfc.index.month, y='rentals', data=dfc, palette=palette*3)  
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Bike Rentals', fontsize=15)
plt.title('Bike Rentals on Monthly Basis', fontsize=15)
plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
plt.show()


# In[35]:


dfc.corr()


# In[38]:


from matplotlib.colors import LinearSegmentedColormap


df_corr = df.corr()


colors = ["#abcdef", "#fedcba"]  


cmap = LinearSegmentedColormap.from_list("custom_cmap", colors, N=100)


plt.figure(figsize=(15, 10))
sns.heatmap(df_corr, annot=True, cmap=cmap)
plt.show()


# In[ ]:




