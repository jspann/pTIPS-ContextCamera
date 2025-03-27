from zoom_builder_helpers import *
import requests
import base64
import time

## Im so sorry please dont tell anyone
ACCOUNT_ID = "SmumKuAwRtO2eaYJQvtxZg"
CLIENT_ID = "AAUOlAn2TP6tHWf2RiqgRw"
CLIENT_SECRET = "8iv1Od5Z3WIlNxaKKwhPJgICkmUgZcGA"

## RTMP Stuff. Preloaded into zoom
STREAM_URL = "rtmp://192.168.50.91/live"
STREAM_KEY = "stream"
# PAGE_URL = "zoommtg://"
PAGE_URL = "http://jspann.me/"

try:
	token = get_access_token(acct_id=ACCOUNT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
	user_id = get_user_id(access_token=token)
	meeting_id = create_meeting(user_id=user_id, access_token=token)
	time.sleep(1)
	configure_livestream(meeting_id=meeting_id, access_token=token, stream_url=STREAM_URL, stream_key=STREAM_KEY, page_url=PAGE_URL)

	print("Meeting is set up")
except requests.exceptions.HTTPError as err:
	print("API Error:", err.response.status_code)
	print(err.response.text)
