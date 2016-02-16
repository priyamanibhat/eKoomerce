import sqlite3
from hacks.kooqueue.helper import *
import time

'''
This cron_job.py is being called from a cron file located at .openshift/cron/hourly/send_msgs.cron
'''

H = int(time.strftime('%H'))
print('Hour:', H)
if H!=23 and H!=0: # compensates for the time zone
	print('exiting...')
	exit()

print('Sending SMSes...')
conn = sqlite3.connect(DATA_DIR + DB_FILE_NAME)
for row in conn.execute('SELECT * FROM ' + TABLE_NAME):
	sendSms(*row)

conn.execute('DELETE FROM ' + TABLE_NAME)
conn.commit()
conn.close()
