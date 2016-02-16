import os
import requests

app_url = 'https://hacks-rakheg.rhcloud.com/kooqueue/'
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR')
TABLE_NAME = 'messages'
DB_FILE_NAME = 'queuedmsgs.db'

def sendSms(phone_no, message, api_key):
	msgUrl = 'https://www.kookoo.in/outbound/outbound_sms.php'
	payload = {'phone_no': phone_no, 'message': message, 'api_key': api_key}
	return requests.get(msgUrl, params= payload).text
