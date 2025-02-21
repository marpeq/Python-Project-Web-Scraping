#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Imports necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL to scrape data from
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Sends a GET request to fetch the page content
page = requests.get(url)

# Processes the page content using BeautifulSoup
contents = BeautifulSoup(page.text, 'html')

# Finds the table containing the companies information 
companies_table = contents.find('table')

# Creates a list that holds the table headers
table_headers = []
for header in companies_table.find_all('th'):
    table_headers.append(header.text.strip())

# Creates a pandas DataFrame with the table headers as columns
df = pd.DataFrame(columns = table_headers)

# Stores each table row data as an element in the list column_data
column_data = companies_table.find_all('tr')

# Extracts data from each row (excluding headers) and adds it to the DataFrame
individual_row_data=[]

for row in column_data[1:]:
    row_data = []
    for data in row.find_all('td'):
        row_data.append(data.text.strip())
    
    position = len(df)
    df.loc[position] =  row_data


# Gets the user's home directory
home_directory = os.path.expanduser("~")

# Defines the path for saving the CSV
csv_file_path = os.path.join(home_directory, 'Documents', 'Largest_Companies_USA.csv')

# Saves the DataFrame as a CSV file without the index column
df.to_csv(csv_file_path, index=False)

