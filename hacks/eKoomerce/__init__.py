import bs4
import requests
import flask

app = flask.Blueprint('eKoomerce', __name__, template_folder='templates')

@app.route('/')
def home():
	return flask.render_template('eKoomerce_account.html')




'''a='selling-price'

In [2]: import bs4, requests

In [3]: resp = requests.get('http://www.flipkart.com/united-colors-benetton-solid-men-s-polo-t-shirt/p/itmeeptfqsfyu6hz').text

In [4]: soup = bs4.BeautifulSoup(resp)

In [5]: soup.find('span', {'class': 'selling-price'})
Out[5]: <span class="selling-price omniture-field" data-evar48="719" data-omnifield="eVar48">Rs. 719</span>

In [6]: soup.find('span', {'class': 'selling-price'}).text
Out[6]: 'Rs. 719'
'''
