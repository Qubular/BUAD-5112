import requests
from lxml import objectify

NOAAurl = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/44-tavg-201807/data.xml'
NOAAdata = requests.get(NOAAurl).content

template = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'
state = '44'
parameter = 'tavg'
year = '2018'
month = '08'
wxurl = template % (state,parameter,year,month)
print(wxurl)

root = objectify.fromstring(NOAAdata)

print('lallen01')
print(root.data[4].value)
print(root.data[4].mean)
print(root.data[4].departure)
print(root.data[4].lowRank)
print(root.data[4].highRank)

