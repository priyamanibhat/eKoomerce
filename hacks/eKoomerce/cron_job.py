import requests
import json
import bs4
from urllib.parse import *
from hacks.eKoomerce.config import *

dbUrl = 'https://ekoomerce.firebaseio.com/'

users = requests.get(dbUrl + 'user.json', params={'auth': db_admin_secret}).json()
for user in users:
	for url in users[user]['url']:
		try:
			soup = bs4.BeautifulSoup(requests.get(url).text, 'lxml')
			price = soup.find('span', {'class':'a-size-medium a-color-price'}).text.strip()
			qurl = ''.join(map(lambda x:'%'+hex(ord(x))[2:], url))
			#qurl = quote(url).replace('/', '%2f').replace('.', '%2e')
			oldData = requests.get(dbUrl + 'url/' + qurl + '.json', params={'auth': db_admin_secret})
			print('oldData', oldData, bool(oldData))
			print('oldText', oldData.text, bool(oldData.text))
			print('oldjson', oldData.json(), bool(oldData.json()))
			oldData=oldData.json()
			if oldData:
				oldPrice=oldData['price']
				if oldPrice!=price:
					requests.get('https://hacks-rakheg.rhcloud.com/kooqueue/', params=dict(phone_no=user['phone_no'], api_key=kookoo_api_key, message='Your chosen Amazon product\'s price changed from Rs.{} to Rs.{}. {}'.format(oldPrice, price, shortUrl(url))))
			requests.post(dbUrl + 'url/' + qurl + '.json', params={'auth': db_admin_secret}, data=json.dumps({'price':price}))
		except:
			print(url, qurl)
			import traceback
			traceback.print_exc()

def shortUrl(longUrl):
	return requests.post('https://www.googleapis.com/urlshortener/v1/url',
						 params= {'key': urlshortener_apikey},
						 data= '{{ "longUrl": "{}" }}'.format(longUrl),
						 headers= {'Content-Type': 'application/json'}).json()['id']
