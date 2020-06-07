
import requests  
from bs4 import BeautifulSoup

html_path = 'http://publicinterestlegal.org/county-list/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(html_path, headers=headers)
html_doc = response.content
#print(response.content)
# Uncomment to verify that the new user agent pulled website HTML data.

parsed_html = BeautifulSoup(html_doc, 'lxml')
data_rows = parsed_html.find_all('tr')
# Parsed the data to find all HTML table rows, which were then placed into
# a variable for further scraping below.

all_counties = []
# Created an empty list to hold the resultant data from the for loop.
for row in data_rows:
    new_row = []
    for x in row.find_all('td'):
        new_row.append(x.text)
    all_counties.append(new_row)
# new_row holds all extracted 'td' tags, which are then placed back into
# the all_counties list.

print('lallen01')
print(len(data_rows))
print(all_counties)