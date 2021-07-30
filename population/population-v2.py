#!/usr/bin/env python
# coding: utf-8

# In[29]:


import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[30]:


data: [] = list()
home: [] = list()
aways: object = None
result_name: str = ''


# In[31]:


#df = pd.read_csv('./data/202106_202106.population -v2.csv', encoding='UTF-8', thousands=',', index_col=0)
#df.to_csv('./data/202106_202106.population -v2.csv', sep=',', na_rep='NaN')
data = csv.reader(open('./data/202106_202106.population -v2.csv', 'rt', encoding='UTF-8'))
next(data)
data = list(data)


# In[32]:


#print(data)


# In[33]:


home = []
[home.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print(home)


# In[34]:


plt.title('Pildong Population')
plt.plot(home)


# In[35]:


np.array(home)


# In[39]:


mn = 1
result = 0
home = []
for i in data:
    if '필동' in i[0]:
        home = np.array(i[3:], dtype=int)/int(i[2])


# In[40]:


result_name=''
away= []
for i in data:
    away = np.array(i[3:], dtype=int)/ int(i[2])
    s = np.sum((home - away)**2)
    if s < mn and '필동' not in i[0]:
        mn = s
        result_name = i[0]
        result = away
aways = result


# In[41]:


plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.title('Simialr to Pildong')
plt.plot(home, label='Pildong')
plt.plot(away, label='Simialr to Pildong')
plt.legend()
plt.show()


# In[ ]:




