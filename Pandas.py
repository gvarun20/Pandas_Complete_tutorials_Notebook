#!/usr/bin/env python
# coding: utf-8

# # what is pandas ?
# pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license
# 

# In[7]:


import pandas as pd


# In[2]:


pd. __version__


# In[7]:


df = pd.read_excel("C:\\Users\\Abhishek kumar\\Downloads\\Student Data.xlsx")
df


# In[1]:


df =pd.read_csv('datamusic.csv')


# In[6]:


italy_covid_url='https://raw.githubusercontent.com/chidanandamurthy/dataAnalysis/main/italy-covid-daywise.csv'
urlretrieve(italy_covid_url,'italy_covid_daywise.csv')


# In[4]:


from urllib.request import urlretrieve


# In[10]:


covid_df=pd.read_csv('italy_covid_daywise.csv')
covid_df


# In[11]:


covid_df.shape


# In[12]:


#infois used to fetch the number of dtypes
covid_df.info()


# In[13]:


''''Descriptive statistics include those that summarize the central
tendency, dispersion and shape of a
dataset's distribution, excluding ``NaN`` values.'''
covid_df.describe()


# In[16]:


covid_df.shape


# In[ ]:





# In[19]:


col=covid_df.columns
col


# In[25]:


covid_data_dict={
    'data': ['2020-08-30','2020-08-31','2020-09-01','2020-09-02','2020-09-03'],
    'new_cases': [1444,1365,996,975,1326],
    'new_death': [1,4,6,8,6],
    'new_test': [533541,42583,54395,None,None]
}


# In[26]:


covid_data_dict['new_cases']


# In[27]:


covid_df['new_cases']


# In[28]:


covid_df['new_cases'][246]


# In[29]:


covid_df['new_test']


# In[31]:


df=pd.DataFrame({'col one' :[100,200],'col two':[100,200]})
df


# In[35]:


import numpy as np
pd.DataFrame(np.random.rand(4,8))


# In[36]:


df.rename(columns = {'test':'TEST'}, inplace = True)


# In[37]:


covid_df['new_cases'][246]


# In[38]:


covid_df.new_cases


# In[41]:


covid_df.new_deaths


# In[42]:


df['col one']


# In[43]:


cases_df=covid_df[['date','new_cases']]
cases_df


# In[44]:


covid_df_copy=covid_df.copy()


# In[45]:


covid_df_copy


# In[46]:


covid_df.compare(covid_df_copy)


# In[48]:


covid_df_copy.equals(covid_df)


# In[49]:


covid_df==covid_df_copy


# In[50]:


covid_df.loc[243]


# In[54]:


#update_df = df.drop(['new_case', 'new_test'])


# In[59]:


covid_df.head(7)


# In[60]:


covid_df.tail(9)


# In[62]:


covid_df.sample(8)


# In[63]:


covid_df.at[0,'new_tests']


# In[65]:


type(covid_df.at[0,'new_tests'])


# In[66]:


total_cases =covid_df.new_cases.sum()
total_deaths =covid_df.new_deaths.sum()


# In[67]:


print(f'The number of reported cases is{total_cases}and the number of reported death is{total_deaths}')


# In[69]:


death_rate =covid_df.new_deaths.sum()/covid_df.new_cases.sum()


# In[71]:


print('the over all reported death rate in italy is{:.2f}%',death_rate*100)


# In[ ]:





# In[75]:


high_new_cases = covid_df.new_cases >1000
high_new_cases


# In[76]:


covid_df[high_new_cases]


# In[78]:


covid_df[covid_df.new_cases>1000].shape


# In[80]:


positive_rate


# In[82]:


high_ratio_df=covid_df.new_cases/covid_df.new_tests>positive_rate


# In[ ]:


covid_df.sort_values('new_test',assending=False)


# In[83]:


covid_df.at[172,'new_cases']=(covid_df.at[171,'new_cases']+covid_df.at[173,'new_cases'])/2


# In[86]:


covid_df.loc[172].new_cases


# In[87]:


covid_df.date


# In[88]:


covid_df['date']=pd.to_datetime(covid_df.date)


# In[89]:


covid_df['date']


# In[90]:


covid_df['year']=pd.DatetimeIndex(covid_df.date).year
covid_df['month']=pd.DatetimeIndex(covid_df.date).month
covid_df['day']=pd.DatetimeIndex(covid_df.date).day
covid_df['weekday']=pd.DatetimeIndex(covid_df.date).weekday


# In[92]:


covid_df


# In[93]:


covid_df_may = covid_df[covid_df.month == 5]

covid_df_may_metrics =covid_df_may[['new_cases','new_deaths','new_tests']]


covid_may_totals =covid_df_may_metrics.sum()


# In[94]:


covid_may_totals


# In[95]:


covid_df_may_metrics


# In[96]:


covid_df_may


# In[96]:


covid_df_may


# In[96]:


covid_df_may


# In[97]:


covid_df[covid_df.month == 5][['new_cases','new_deaths','new_tests']].sum()


# In[98]:


covid_df.new_cases.mean()


# In[99]:


covid_df[covid_df.weekday==6].new_cases.mean()


# GROUPING AND AGGREGATION

# In[100]:


covid_df.groupby('month')[['new_cases','new_deaths','new_tests']].sum()


# In[117]:


url ='https://raw.githubusercontent.com/chidanandamurthy/dataAnalysis/main/locations.csv'
urlretriver(url ,locations.csv)
locations_df = pd.read_csv('locations.csv')


# In[110]:


import pandas as pd
locations_df = pd.read_csv('locations.csv')
locations_df


# In[111]:


locations_df[locations_df.location == "Italy"]


# In[115]:


url1 = 'https://raw.githubusercontent.com/chidanandamurthy/dataAnalysis/main/locations.csv'
urlretrieve(url1,'locations.csv')


# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




