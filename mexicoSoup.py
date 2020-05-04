import requests
from bs4 import BeautifulSoup
import re
import csv

URL = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Mexico'
page = requests.get(URL)
mexicoData = open("mexicoData.csv", 'w')
mexicoData.close()
state_list = []

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'mw-content-text')
results_table = results.find('table', class_ = 'wikitable')
state_elems = results_table.find_all('tr')

def scrapeMexico():
    for state_elem in state_elems:
        if (state_elem.find('a') and state_elem.find('a').has_attr('title')):
            state_title = state_elem.find('a')['title']
            td_list = state_elem.find_all('td')
            state_cases = re.sub('<|t|d|>|/', '', str(td_list[0]))
            state_deaths = re.sub('<|t|d|>|/', '', str(td_list[2]))
            state_list.append([state_title, state_cases, state_deaths])
    mexicoToCSV()

def mexicoToCSV():
    with open("mexicoData.csv", 'w', newline = '') as fileCases:
        covid_writer = csv.writer(fileCases)
        for state in state_list:
            covid_writer.writerow([state[0], state[1], state[2]])
    mexicoData.close()

if __name__ == '__main__':
    scrapeMexico()
