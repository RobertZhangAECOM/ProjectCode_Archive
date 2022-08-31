#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Package Import
# import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Input Path and set up Webdriver
# os.environ['PATH'] += r"C:\A_Programs\ProjectCode\DataScrapingTutorial\Test" # Path needs to be changed to the running folder
driver = webdriver.Chrome()
driver.get('https://route.virginhyperloop.com/') # The website link
driver.implicitly_wait(10)

# Input File
df = pd.read_csv('Input.csv') # Path needs to be modified if the input file is changed

# Validation
df_cityname = pd.read_csv('Cityname.csv', header=None)
Cities = set(list(df_cityname[0]))
Origins = set(list(df.Origin))
Destinations = set(list(df.Destination))
if Origins.issubset(Cities):
    print("The format of the Origins is correct.")
else:
    print("The format of the Origins is incorrect. Please check:")
    print(set(Origins) - set(Cities))
    exit()
Destinations.issubset(Cities)
if Origins.issubset(Cities):
    print("The format of the Destinations is correct.")
else:
    print("The format of the Destinations is incorrect.")
    print(set(Destinations) - set(Cities))
    exit()
print("-----------------------------------------------")


# Output File
with open('Output.csv', 'w') as f: # Path needs to be modified if the output file is changed

    for i in range(len(df)):

        # Find Ori/Des Input Bar
        origin = driver.find_element(By.XPATH, '//*[@id="input-console"]/div[1]/div/input')
        destination = driver.find_element(By.XPATH, '//*[@id="input-console"]/div[2]/div/input')

        # Insert the city name and Search
        origin.send_keys(df.Origin[i])
        time.sleep(0.5) # change the following time as needed
        origin.send_keys(Keys.ENTER)
        time.sleep(1)
        destination.send_keys(df.Destination[i])
        time.sleep(0.5)
        destination.send_keys(Keys.ENTER)
        time.sleep(2.5)

        # Store the result in the list
        City_List = driver.find_elements(By.CLASS_NAME, 'city-name')
        Dist_List = driver.find_elements(By.ID, 'distance')
        Mode_List = driver.find_elements(By.CLASS_NAME, 'mode-description')
        Time_List = driver.find_elements(By.CLASS_NAME, 'time-column')

        # Write to the .csv file
        if not i:
            f.write(f'ORIGIN,DESTINATION,DISTANCE(mi),')
            for j in range(len(Mode_List)):
                f.write(f'{Mode_List[j].text}(mins),')
            f.write(f'\n')
        f.write(f"{City_List[0].text},{City_List[1].text},{Dist_List[0].text.split(' ')[0]},")
        for (Mode, Time) in zip(Mode_List, Time_List[1:]): # Delete the heading for Time_List
            f.write(f"{60 * int(Time.text.split(':')[0]) + int(Time.text.split(':')[1])},")
        f.write(f'\n')
        print(f'{City_List[0].text} to {City_List[1].text} Saved')

        # Restart the search
        button = driver.find_element(By.XPATH, '//*[@id="results"]/button')
        button.click()
        time.sleep(0.5)

f.close()
print('Completed!')


# In[ ]:
