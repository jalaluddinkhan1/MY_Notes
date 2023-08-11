#!/usr/bin/env python
# coding: utf-8

# ## Fetch Data from CSV

# In[4]:


import pandas as pd
ds=pd.read_csv('titanic.csv')
ds


# # Fetch Data from Json

# In[5]:


df=pd.read_json('iris.json')
df


# # Fetch data frm api

# In[13]:


import requests

url = "https://ott-details.p.rapidapi.com/advancedsearch"

querystring = {"start_year":"1970","end_year":"2020","min_imdb":"6","max_imdb":"7.8","genre":"action","language":"english","type":"movie","sort":"latest","page":"1"}

headers = {
	"X-RapidAPI-Key": "c1b90ad041mshd92524260dd7ca3p135aecjsnbffe396f1442",
	"X-RapidAPI-Host": "ott-details.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

df=pd.DataFrame(response.json()['results'])
df


# # Web scraping

# In[23]:


from bs4 import BeautifulSoup
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage=requests.get('https://www.ambitionbox.com/list-of-companies?campaign=homepage_companies_widget',headers=headers).text
soup=BeautifulSoup(webpage)
print(soup.prettify())


# In[24]:


for i in soup.find_all('h2'):
    print(i.text.strip())


# # Web Scrap form open Website

# In[25]:


url='https://www.programiz.com/'
resp=requests.get('https://www.programiz.com/')
pf=BeautifulSoup(resp.content)
print(pf.prettify())


# In[22]:


for i in pf.find_all('h3'):
    print(i.text.strip())


# In[ ]:




