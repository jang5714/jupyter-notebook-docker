#!/usr/bin/env python
# coding: utf-8

# In[20]:


import csv
import matplotlib.pyplot as plt
import random


# In[6]:


data: [] = list()
highest_temperature: [] = list()
data = csv.reader(open('data/seoul.csv', 'rt', encoding ='UTF-8'))


# In[7]:


next(data)


# In[8]:


ls = list(data)


# In[18]:


#print([i[-1] for i in ls])


# In[11]:


highest_temperature=[]
[highest_temperature.append(float(i[-1])) for i in ls if i[-1] != '']
print(f'{len(highest_temperature)} 개')


# In[12]:


plt.plot(highest_temperature, 'r') #red
plt.figure(figsize=(20, 2))


# In[13]:


high = [] #최고기온
low = [] #최저기온


# In[14]:


for i in ls:
    if i[-1] != '' and i[-2] != "":
        if 1983 <= int(i[0].split('-')[0]):
            if i[0].split('-')[1] == "02" and i[0].split('-')[2] == '14':
                high.append(float(i[-1]))
                low.append(float(i[-2]))


# In[17]:


plt.rc('font', family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.title('The temperature change graph of my birthday')
plt.plot(high, 'hotpink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()


# In[21]:


arr = []
[arr.append(random.randint(1, 1000))for i in range(13)]
plt.boxplot(arr)
plt.show()


# In[22]:


month = [[], [], [], [], [], [], [], [], [], [], [], []]
# for i in arr:
#     if i[-1] != '':
#         month[int(i[0].split('-')[1])-1].append(float(i[-1]))
[month[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in ls if i[-1] != '']
plt.boxplot(month)
plt.show()


# In[23]:



day = []
[day.append([]) for i in range(31)]
[day[int(i[0].split('-')[2]) -1].append(float(i[-1]))
     for i in ls
        if i[-1] != ''
            if i[0].split('-')[1] == '08']
plt.style.use('ggplot') # Graph Style
plt.figure(figsize=(10, 5), dpi=300) # Graph Size
plt.boxplot(day, showfliers=False) # Omit Outlier
plt.show()


# In[ ]:




