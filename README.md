# eKoomerce
eKoomerce allows you enter Amazon India Product URLs to track the price changes and out-of-stock to in-stock changes via instant SMS notifs. If the SMS is not sent immediately, it will be queued to be sent on the following day. As this is just a completely working demo, please make sure that your phone number is not in DND and also please note that you will not receive any messages between 9pm-9am.

Visit https://goo.gl/AfmQLo to use the website.

## Functioning
- Your Amazon Product URLs are automatically saved to Firebase as you enter the values
- A cron job checks for changes in product information every minute to give near-instant notifications
- You can start following/tracing the program from flaskapp.py into eKoomerce/__init__.py for the core functionality
- Cron jobs are located under .openshift/cron/minutely for both eKoomerce and kooqueue

## How to use
- Visit the URL mentioned above to enter Amazon India Product URLs
- Enter URL in a textbox and click outside that box or elsewhere to automatically save the URLs
- For demo purposes enter https://hacks-rakheg.rhcloud.com/eKoomerce/dummyproduct in the website. It changes the price value every hour so that you can test the validity of this project.
- You'll receive SMSes between 9am-9pm and pings for changes outside this time window is queued to be sent on the following day.

## Challenges faced
- Keeping track of the price changes and product information by using URL and user mapping
- Mapping successfully verified Twitter user with their number to send SMS notifications
- Queuing unsuccessful SMSes for the following day. SMSes may not be sent due to TRAI regulations of sending the numbers from 9am-9pm.
