#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[9]:


def plot_show():
    plt.title('plotting')
    plt.plot([10, 20, 30, 40])


# In[10]:


plot_show()


# In[11]:


def plot_two_list_show():
    plt.title('plotting')
    plt.plot([1,3,3,4], label='asc', color='blue', linestyle='--')
    plt.plot([12, 43, 25, 15],label ='bid', color='r', ls=':')
    plt.legend()


# In[12]:


plot_two_list_show()


# In[8]:


def scatter():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label ='circle')
    plt.plot([10, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()


# In[13]:


scatter()


# In[ ]:




