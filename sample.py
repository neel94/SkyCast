from geolocation.main import GoogleMaps
import requests,json
import datetime
import time
import numpy as np
import csv
from itertools import izip



address = "Atlanta"

google_maps = GoogleMaps(api_key='AIzaSyBCCeBBAs_GOkEphWvfpdw0VaeR-SrH-F4') 

location = google_maps.search(location=address) # sends search to Google Maps.
my_location = location.first()
print(my_location.lat)
print(my_location.lng)
url = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng)
print url
r = requests.get(url)
parseString = json.loads(r.text)
current= parseString['currently']
f= current['time']
print f
temp1= []
time1= []
date2=[]

f= f-(365*24*60*60)
url1 = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng) + "," + str(f)
s= requests.get(url1)
p= json.loads(s.text)
c1= p['currently']
temp1.append(c1['temperature'])
time1.append(c1['time'])

f= f-(365*24*60*60)
url2 = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng) + "," + str(f)
s2= requests.get(url2)
p2= json.loads(s2.text)
c2= p2['currently']
temp1.append(c2['temperature'])
time1.append(c2['time'])

f= f-(365*24*60*60)
url3 = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng) + "," + str(f)
s3= requests.get(url3)
p3= json.loads(s3.text)
c3= p3['currently']
temp1.append(c3['temperature'])
time1.append(c3['time'])

f= f-(365*24*60*60)
url4 = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng) + "," + str(f)
s4= requests.get(url4)
p4= json.loads(s4.text)
c4= p4['currently']
temp1.append(c4['temperature'])
time1.append(c4['time'])

f= f-(365*24*60*60)
url5 = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng) + "," + str(f)
s5= requests.get(url5)
p5= json.loads(s5.text)
c5= p5['currently']
temp1.append(c5['temperature'])
time1.append(c5['time'])



for i in time1:
	date2.append(datetime.datetime.fromtimestamp(int(i)).strftime('%B-%Y'))

#print temp1
#print date2
t= parseString['hourly']

list1=t['data']
curr= parseString['currently']
#print curr

tem= curr['temperature']
currsum= curr['summary']
wind= curr['windSpeed']
#print tem
#print wind

#print list1

temp=[]
summary=[]
time=[]
hum=[]



for i in list1:
	temp.append(i['temperature'])
for i in list1:
	time.append(i['time'])
for i in list1:
	summary.append(i['summary'])
for i in list1:
	hum.append(i['humidity'])

#item= [t['data'][i] for i in  ]
date1=[]
for i in time:
	date1.append(datetime.datetime.fromtimestamp(int(i)).strftime('%m-%d %H %p'))
#print temp
#print len(summary)

with open('some.csv', 'wb') as csvfile:
	w = csv.writer(csvfile)
	writer = csv.DictWriter(csvfile, fieldnames = ["date","value","summary"], delimiter = ',')
	writer.writeheader()
	w.writerows(izip(date1, temp, summary))

with open('past.csv', 'wb') as file:
	w = csv.writer(file)
	writer = csv.DictWriter(file, fieldnames = ["date","value"], delimiter = ',')
	writer.writeheader()
	w.writerows(izip(date2,temp1))




#print date1
 # returns all locations.
