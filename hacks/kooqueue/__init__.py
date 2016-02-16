import flask
import xml.etree.ElementTree as ET
from urllib.parse import unquote
import sqlite3
from hacks.kooqueue.helper import *

app = flask.Blueprint('kooqueue', __name__, template_folder='templates')

@app.route('/', methods = ['GET', 'POST'])
def home():
	params = flask.request.args
	try:
		phone_no = params['phone_no']
		message = unquote(params['message'])
		api_key = params['api_key']
	except Exception as e:
		print(e)
		response = ET.Element('response')
		ET.SubElement(response, 'message').text = 'phone_no, message and api_key parameters required'
		return kookooResponse(response)
	response = sendSms(phone_no, message, api_key)
	rootXML = ET.fromstring(response)
	print(phone_no, message, api_key)
	if 'Cannot process the request before your working start hour.' in rootXML[1].text:
		queue(phone_no, message, api_key)
	return response

def queue(phone_no, message, api_key):
	conn = sqlite3.connect(DATA_DIR + DB_FILE_NAME)
	conn.execute('CREATE TABLE IF NOT EXISTS {} (phone_no text, message text, api_key text)'.format(TABLE_NAME))
	conn.execute('INSERT INTO {} VALUES (?,?,?)'.format(TABLE_NAME), (phone_no, message, api_key))
	conn.commit()
	conn.close()

def kookooResponse(ETdata):
	return xmlResponse(xmlToString(ETdata))

def xmlResponse(xmlString):
	return xmlString, 200, {'Content-Type': 'application/xml; charset=utf-8'}

def xmlToString(ETdata):
	return ET.tostring(ETdata, encoding='utf8', method='xml')
