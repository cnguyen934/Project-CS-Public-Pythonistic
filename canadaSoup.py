import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import csv

# Scraping table data

url_data = 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html?topic=tilelink'

page = requests.get(url_data)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', class_='table table-striped table-bordered table-hover')

canada_list = []
for row in table.find_all('tr'):
    province_list = []
    for cell in row.find_all('td'):
        province_list.append(cell.text)
    canada_list.append(province_list)   

print(canada_list)

data_file = "canadaData.csv"

try:

    with open(data_file, 'w') as wFile:
        writer = csv.writer(wFile)
        writer.writerow(["Province", "Confirmed Cases", "Probable Cases", "Deaths"])
        writer.writerows(canada_list)
                   
except OSError:
    print("Cannot open", data_file)
