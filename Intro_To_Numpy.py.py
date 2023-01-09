#!/usr/bin/env python
# coding: utf-8

# # What is Numpy?
# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
# 
# ![py.png](attachment:py.png)
# 

# yield_of_apple=w1*temperature ,w2*rainfall,w3*humidity

# w1,w2,w3 =0.3,02,05

# ![WhatsApp%20Image%202023-01-05%20at%2010.33.24%20AM.jpeg](attachment:WhatsApp%20Image%202023-01-05%20at%2010.33.24%20AM.jpeg)

# In[3]:


kanto_temp=73
kanto_rainfall=67
kanto_humidity=43
w1=0.3
w2=0.2
w3=0.5


# In[4]:


kanto_yield_apple=kanto_temp*w1+kanto_rainfall*w2+kanto_humidity*w3
kanto_yield_apple


# In[6]:


print(f'the expected yield of apple in kanto region {kanto_yield_apple} ton per')


# In[7]:


kanto = [73,67,43]
johto = [91,88,64]
hoenn = [87,134,58]
sinnoh = [102,43,37]
unova = [69,96,70]


# In[8]:


weight = [w1,w2,w3]


# In[ ]:





# In[21]:


def crop_yield(region,weight):
    '''This functin computers crop yield of given region parameters:
    '''
    result = 0
    for x ,w in zip(region,weight):
        result+= x*w
    return result


# In[22]:


crop_yield(hoenn,weight)


# In[23]:


crop_yield(unova,weight)


# In[24]:


crop_yield(hoenn,weight)


# In[28]:


pip install numpy


# In[29]:


import numpy as np


# 

# In[31]:


import random
print(random.randint(10,20))


# In[ ]:





# In[32]:


kanto = np.array([73,67,43])


# In[33]:


kanto


# In[35]:


type (kanto)


# In[36]:


np.dot(sinnoh,weight)


# In[40]:


np.dot(kanto,weight)


# In[37]:


np.dot(hoenn,weight)


# In[39]:


(kanto *weight).sum()


# In[43]:


#python list
arr1=list(range(1000000))
arr2=list(range(1000000,2000000))
#print(arr1)
print(type(arr1))
#nymp array
arr1_np=np.array(arr1)
arr2_np=np.array(arr2)


# In[47]:


get_ipython().run_cell_magic('time', '', 'result=0\nfor x1,x2 in zip(arr1,arr2):\n    result +=x1*x2\nresult')


# In[45]:


get_ipython().run_cell_magic('time', '', 'np.dot(arr1_np,arr2_np)')


# In[48]:


climate_data=np.array([[73,67,43],
                       [91,88,64],
                       [87,134,58],
                       [102,43,37],
                       [69,96,70]])


# In[49]:


climate_data


# In[50]:


#2d array (matrix)
climate_data.shape


# In[52]:


weight


# In[53]:


#3d array
arr3 = np.array ([[[73,67,43],
                   [91,88,64],
                   [87,134,58],
                   [102,43,37],
                   [69,96,70.5]]])


# In[54]:


arr3.shape


# In[55]:


arr3.dtype


# In[56]:


np.matmul(climate_data,weight)


# In[57]:


climate_data@weight


# In[59]:


a = np.array([[ 0, 1, 2, 3],
 [ 4, 5, 6, 7],
 [ 8, 9, 10, 11]])
         b = a # no new object is created
     b is a


# In[61]:


a = np.arange(10)**3
a


# In[62]:


a[::-1]


# In[63]:


for i in a:
     print(i**(1 / 3.))


# In[76]:


c = np.array([[[ 0, 1, 2], # a 3D array (two stacked 2D arrays)
 [ 10, 12, 13]],
 [[100, 101, 102],
 [110, 112, 113]]])
print(c)


# In[67]:


c.shape
c[1, ...]
c[..., 2]


# In[71]:



b.T
array([[ 0, 1, 2, 3],
[10, 11, 12, 13],
[20, 21, 22, 23],
[30, 31, 32, 33],
[40, 41, 42, 43]])


# In[78]:


b.shape


# In[73]:


b.T.shape


# In[75]:


a = np.floor(10 * rg.random((3, 4)))


# In[80]:


import urllib.request
url='https://raw.githubusercontent.com/chidanandamurthy/dataAnalysis/main/climate.txt'
urllib.request.urlretrieve(url,'climate.txt')


# In[85]:


climate_data=np.genfromtxt('climate.txt',delimiter=',',skip_header = 1)


# In[86]:


climate_data


# In[87]:


climate_data.shape


# In[88]:


weights=np.array([0.3,0.2,0.5])


# In[90]:


yields = climate_data @ weight
yields


# In[92]:


yields.shape


# In[96]:


climate_results = np.concatenate((climate_data,yields.reshape(10000,1)),axis=1)
climate_results


# In[99]:


from numpy import savetxt
savetxt('climate_results.csv', climate_results, delimiter=',')


# In[102]:


np.zeros((3,2))


# In[103]:


np.eye(3)


# In[104]:


np.random.rand(6)


# In[105]:


np.random.rand(2,3)


# In[106]:


np.full([2,4],45)


# In[109]:


np.arange(10,90,5)


# In[110]:


np.arange(10,90,-2)


# In[111]:


np.arange(10,90,-1)


# In[112]:


np.arange(10,90,3)


# In[113]:


np.arange(10,90,9)


# In[ ]:





# In[ ]:





# In[ ]:




