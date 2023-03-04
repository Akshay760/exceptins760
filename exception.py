#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1..no such element exception
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException


# In[2]:


driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(5)
element = driver.find_element("Hoo-Haa-hOO")
element.text


# In[3]:


try:
    element = driver.find_element("Hoo-Haa-hOO")
    print(element.text)
except NoSuchElementException as e:
    print("Exception Raised: ", e)
    element = driver.find_element(By.XPATH,'//a[@class="gb_p"]')
    print(element.text)
    


# In[4]:


driver.close()


# In[5]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[6]:


driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.snapdeal.com/")
delay=10
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchTextSpan')))
element = driver.find_element(By.XPATH,"//span[@class='searchTextSpan']")
element


# In[7]:


driver.close()


# In[8]:


#2..staleelementreferenceexception


# In[9]:


from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# In[10]:


driver =  webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.snapdeal.com/")
try:
    element = driver.find_element(By.XPATH,"//span[@class='searchTextSpan']")
    print(element)
except StaleElementReferenceException as e:
    print ("Exception Raise: ",e)
    print ("Refresh the page!!")
    driver.get("https://www.snapdeal.com/")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'searchTextSpan')))
    element = driver.find_element(By.XPATH,"//span[@class='searchTextSpan']")
    print(element)


# In[11]:


driver.close()


# In[12]:


#3...elementnotinteractableexception


# In[13]:


from selenium.common.exceptions import ElementNotInteractableException


# In[14]:


driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.amazon.in/")
time.sleep(5)
try:
    element=driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-previous-rounded']/span")
    element.click()
except ElementNotInteractableException as e:
    print ("Exception Raised: ", e)
    element = driver.find_element(By.XPATH,'//a[@class="a-carousel-goto-nextpage"]')
    driver.get(element.get_attribute('href'))
    


# In[15]:


from selenium.common.exceptions import SessionNotCreatedException
#sessionnotcreatedexceptions


# In[16]:


try:
    driver = webdriver.Chrome(r"chromedriver")
    driver.get('https://www.google.com/')
except SessionNotCreatedException as e:
    print("Exception Raised: ", e)
    driver = webdriver.Chrome(r"chromedrivr.exe")
    driver.get('https://www.google.com/')                        


# In[17]:


driver.close()


# In[18]:


#timeout exceptions


# In[19]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# In[21]:


driver = webdriver.Chrome(r"chromedriver.exe")
delay=10
try:
    driver.get("https://www.amazon.in/")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'a-section a-spacing-mini')))
    print(element)
except TimeoutException as e:
    print("Exception Raised: ", e)
    


# In[22]:


driver.close()


# In[23]:


#opening crome in icognito mode


# In[24]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--incognito')


# In[25]:


driver = webdriver.Chrome(r"chromedriver.exe")


# In[26]:


driver.get('https://www.google.com/')


# In[27]:


driver.close()


# In[ ]:





# In[ ]:





# In[28]:


#web scraping exceptioms handaling


# In[36]:


import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
import re
from selenium.webdriver.common.by import By
import time


# In[40]:


driver = webdriver.Chrome(r"chromedriver.exe")


# In[41]:


driver.get('https://www.naukri.com/')


# In[45]:


search_field_designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
search_field_designation.send_keys("data scientist")

search_field_location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
search_field_location.send_keys("Bangalore")

search_button=driver.find_element( By.XPATH, "/html/body/div[1]/div[6]/div/div/div[6]")
search_button.click()


time.sleep(4)


# In[47]:


job_opening_url = []
start=0
end=2
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class= "title ellipsis"]')
    for i in url:
        job_opening_url.append(i.get_attribute('href'))
    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[2]/div[3]/div/a[2]/span")    


# In[48]:


len(job_opening_url)


# In[49]:


job_opening_url


# In[52]:


JD=[]

for i in job_opening_url[0:10]:
    driver.get(i)
    time.sleep(5)
    try:
        description = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[2]')
        JD.append(description.text)
    except NoSuchElementException :
        JD.append('Not present')


# In[53]:


JD


# In[ ]:




