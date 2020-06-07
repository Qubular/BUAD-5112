import requests
from lxml import objectify

NOAAurl = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/44-tavg-201807/data.xml'
NOAAdata = requests.get(NOAAurl).content
# Imported the data in Python from the NOAA website, and pulled content using
# the .content method.

template = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s/data.xml'
state = '44'
parameter = 'tavg'
year = '2018'
month = '08'
wxurl = template % (state,parameter,year,month)
print(wxurl)
# Analyzed the website url to determine proper parameter set placement, and
# built a new URL for the requested data set.

root = objectify.fromstring(NOAAdata)
# Set the lowest level NOA XML data as the root. As the data for April-August
# 2018 are in the 4th element of the data set, the print statements below 
# extract each data element as requested.

print('lallen01')
print(root.data[4].value)
print(root.data[4].mean)
print(root.data[4].departure)
print(root.data[4].lowRank)
print(root.data[4].highRank)

