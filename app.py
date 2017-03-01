# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
from geolocation.main import GoogleMaps
import requests,json
import datetime
import numpy as np
import csv
from itertools import izip


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET'])
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/home', methods=['POST'])
def hello():
    email=request.form['youremail']
    return render_template('home.html', name=email)


    
@app.route('/qwe', methods=['POST'])
def qwe():
	#name= request.form['uname']
	#print "Hi"
	address=request.form['addr']
	google_maps = GoogleMaps(api_key='AIzaSyBCCeBBAs_GOkEphWvfpdw0VaeR-SrH-F4') 

	location = google_maps.search(location=address) # sends search to Google Maps.
	my_location = location.first()
	#print(my_location.lat)
	#print(my_location.lng)
	url = "https://api.darksky.net/forecast/63ba9bb3c3e8270e19c1f1b27a81d090/" + str(my_location.lat) + "," + str(my_location.lng)
	#print url
	r = requests.get(url)
	parseString = json.loads(r.text)

	current= parseString['currently']
	t= parseString['hourly']
	list1=t['data']
	curr= parseString['currently']
	#print curr

	tem= curr['temperature']
	currsum= curr['summary']
	wind= (25/11)*curr['windSpeed']
	#print tem
	#print wind
	temp=[]
	summary=[]
	time=[]
	hum=[]
	f= current['time']
	#print f
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
	#print len(temp)
	#print len(summary)
	#print time
	with open('static/some.csv', 'wb') as csvfile:
		w = csv.writer(csvfile)
		writer = csv.DictWriter(csvfile, fieldnames = ["date","value", "summary"], delimiter = ',')
		writer.writeheader()
		w.writerows(izip(date1, temp, summary))

	with open('static/past.csv', 'wb') as file:
		w = csv.writer(file)
		writer = csv.DictWriter(file, fieldnames = ["date","value"], delimiter = ',')
		writer.writeheader()
		w.writerows(izip(date2,temp1))

	return render_template('result.html', tem= tem, wind= wind, currsum=currsum)

@app.route('/link2')
def click2():
	return render_template('past.html')
	pass
@app.route('/link')
def click():
	return render_template('abc.html')

	

# Run the app :)
if __name__ == '__main__':
  app.run(port=5002)
