import requests
from bs4 import BeautifulSoup
#import lxml.html as lh
import pandas as pd

URL = 'https://www.theguardian.com/world/ng-interactive/2020/apr/16/coronavirus-map-of-the-us-latest-cases-state-by-state'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = "co-table-container")
job_elems = results.find_all('tbody', class_= "co-tbody")
print(job_elems)

state_list = []
state_elems = results.find_all('td')
for state_elem in state_elems:
    print(state_elem.text)
    state_list.append(state_elem.text)

print(state_list)

 

