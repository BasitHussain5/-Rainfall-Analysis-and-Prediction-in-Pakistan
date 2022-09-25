#!/usr/bin/env python
# coding: utf-8

# # Topic: Rainfall Analysis and Prediction in Pakistan
# 

# import libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


# In[2]:


data = pd.read_csv("Rainfall_1901_2016_PAK.csv")


# In[3]:


data


# In[4]:


data.shape


# In[5]:


data.columns


# In[6]:


data.rename(columns = {'Rainfall - (MM)':'Rainfall-(mm)',' Year':'Year'}, inplace = True)


# In[7]:


data.columns


# In[8]:


data


# # Analysis and Visualize Rainfall by Stacked Bar Graph

# In[9]:


x = (input("Enter the range of year i.e 2000-2016: "))
year = x.split("-")

if int(year[0]) < 1901 or int(year[1]) > 2016:
    print("Invalid Year")
else:
    plt.figure(figsize=(15, 8))
    graph = px.bar(data.loc[(data.Year >= int(year[0]))].loc[(data.Year <= int(year[1]))], x = "Year", 
    y = "Rainfall-(mm)",hover_name = 'Month',color = 'Month',title = 'Rainfall During {} to {}'.format(year[0], year[1]))
    graph.show()


# # Analysis and Visualize Rainfall Using Animation Bar

# In[10]:


x = (input("Enter the range of year i.e 2000-2016: "))
year = x.split("-")

if int(year[0]) < 1901 or int(year[1]) > 2016:
    print("Invalid Year")
else:
    graph = px.bar(data.loc[(data.Year >= int(year[0]))].loc[(data.Year <= int(year[1]))], x = "Year", 
    y = "Rainfall-(mm)", color = 'Month', title = 'Rainfall During {} to {} using Animation'.format(year[0], year[1]), 
    animation_frame = "Year", animation_group = "Month", log_x = True, range_x = [int(year[0]),int(year[1])], range_y=[0,400])
    graph.show()


# # Analysis and Visualize Rainfall Using Animation Bar months

# In[11]:


x = (input("Enter the range of year i.e 2000-2016: "))
year = x.split("-")

if int(year[0]) < 1901 or int(year[1]) > 2016:
    print("Invalid Year")
else:
    graph = px.bar(data.loc[(data.Year >= int(year[0]))].loc[(data.Year <= int(year[1]))], x = "Year", y = "Rainfall-(mm)", 
    color = 'Month', title = 'Rainfall During {} to {} using Animation'.format(year[0], year[1]), animation_frame = "Month", 
    animation_group = "Year", log_x = True, range_x = [int(year[0]),int(year[1])], range_y=[0,200])
    graph.show()


# # Comaparison of rainfall 

# In[12]:


month_check = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month = input("Enter the name of the month: ")
month = month.capitalize()

x = (input("Enter the range of year i.e 2000-2016: "))
year = x.split("-")

if month not in month_check:
    print("Invalid month name!")
elif int(year[0]) < 1901 or int(year[1]) > 2016:
    print("Invalid Year")
else:
    var = data[{'Year','Rainfall-(mm)','Month'}].loc[(data.Year >= int(year[0]))].loc[(data.Year <= int(year[1]))].loc[(
    data.Month == month)]
    graph = px.line(var, x = 'Year', y = 'Rainfall-(mm)', color = 'Month', range_x = [int(year[0])-1, int(year[1])+1], text
    = 'Rainfall-(mm)', title = 'Rainfall in month {} during Year {} to {}'.format(month, year[0],year[1]))
    graph.update_traces(texttemplate = '%{text:.4s}', textposition='top center')
    graph.show()
    
    plt.figure(figsize=(15,6))
    sns.barplot(x=data["Year"].loc[(data.Year >=int(year[0]))].loc[(data.Year <=int(year[1]))].loc[(data.Month ==month)],
    y=data["Rainfall-(mm)"]).set_title('Rainfall in month {} during Year {} to {}'.format(month, year[0],year[1]))


# # Number of Percent Rainfall during a range of Year

# In[13]:


x = (input("Enter the range of year i.e 2000-2016: "))
year = x.split("-")

if int(year[0]) < 1901 or int(year[1]) > 2016:
    print("Invalid Year")
else:
    var = data[{'Rainfall-(mm)','Year'}].loc[(data.Year >= int(year[0]))].loc[(data.Year <= int(year[1]))]
    figer = px.pie(var, values = 'Rainfall-(mm)', color ='Year', names ='Year', labels = 'Year', width = 800, height = 600, hole = 0, title = 'Number of percentage Rainfall Year during {} to {}'.format(year[0],year[1]))
    figer.show()
    


# # Monthly Rainfall in Pakistan During 1901 to 2016

# In[14]:


data = pd.read_csv("Rainfall_1901_2016_PAK.csv")
data.rename(columns = {'Rainfall - (MM)':'Rainfall-(mm)',' Year':'Year'}, inplace = True)

var = data.groupby([data.Month]).mean()['Rainfall-(mm)']

fig = px.bar(var,y ='Rainfall-(mm)', title = 'Monthly Rainfall in Pakistan During 1901 to 2016', category_orders = 
{"Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", 
"December"]},
color_discrete_sequence = px.colors.qualitative.D3)
fig.update(layout = dict(title = dict(x = 0.5)))
fig.show()


# # Season wise Rainfall in Pakistan During 1901 to 2016

# In[15]:


data = pd.read_csv("Rainfall_1901_2016_PAK.csv")
data.rename(columns = {'Rainfall - (MM)':'Rainfall-(mm)',' Year':'Year'}, inplace = True)

winter=data.query('Month=="December" or Month=="January" or Month=="February"').groupby([data.Year]).mean()['Rainfall-(mm)']
spring=data.query('Month=="March"or Month=="April"').groupby([data.Year]).mean()['Rainfall-(mm)']
summer=data.query('Month=="May" or Month=="June" or Month=="July" or Month=="August"or Month=="September"').groupby([data.Year]).mean()['Rainfall-(mm)']
Autumn=data.query('Month=="October" or Month=="November"').groupby([data.Year]).mean()['Rainfall-(mm)']

data=pd.DataFrame({ 'Winter': winter, 'Spring': spring,'Summer': summer, 'Autumn': Autumn })
y=data.mean()
x=data.columns
fig = px.bar(x=x,y=y,color=x,title='Season wise Rainfall in Pakistan')
fig.update(layout=dict(title=dict(x=0.5)))
fig.show()


# In[16]:


data = pd.read_csv("Rainfall_1901_2016_PAK.csv")
data.rename(columns = {'Rainfall - (MM)':'Rainfall-(mm)',' Year':'Year'}, inplace = True)
data_yearly= data.groupby('Year')['Rainfall-(mm)'].mean().reset_index()
data_yearly


# # Rainfall Line Graph of Pakistan During 1901 to 2016

# In[17]:



plt.figure(figsize=(36, 10), dpi=80,)
plt.plot(data_yearly.Year,data_yearly["Rainfall-(mm)"])


# In[ ]:




