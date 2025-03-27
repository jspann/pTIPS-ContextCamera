import requests
import base64
import time


"""
"""
def get_access_token(acct_id, client_id, client_secret):
	print("===Getting access token")
	url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={acct_id}"
	credentials = f"{client_id}:{client_secret}"
	headers = {
		"Authorization": "Basic " + base64.b64encode(credentials.encode()).decode(),
		"Content-Type": "application/x-www-form-urlencoded"
	}
	response = requests.post(url, headers=headers)
	response.raise_for_status()
	token = response.json()["access_token"]
	return token

"""
Getting a user ID - shouldn't need to change this ever
"""
def get_user_id(access_token):
	url = "https://api.zoom.us/v2/users"
	headers = {"Authorization": f"Bearer {access_token}"}
	response = requests.get(url, headers=headers)
	response.raise_for_status()
	return response.json()["users"][0]["id"]

"""
Make the meeting for right now
"""
def create_meeting(user_id, access_token):
	url = f"https://api.zoom.us/v2/users/{user_id}/meetings"
	headers = {
		"Authorization": f"Bearer {access_token}",
		"Content-Type": "application/json"
	}
	payload = {
		"topic": "pTIPS Context camera",
		"type": 1,  # Instant meeting
		"settings": {
			"join_before_host": True,
			"waiting_room": False,
			"approval_type": 2
		}
	}
	response = requests.post(url, headers=headers, json=payload)
	response.raise_for_status()
	meeting = response.json()

	print("Guest URL:", meeting["join_url"])
	print()
	print("Host URL:", meeting["start_url"])
	print()
	return meeting["id"]

"""
Attach livestream info to meeting
"""
def configure_livestream(meeting_id, access_token, stream_url, stream_key, page_url):
	print("===setting up livestream")
	url = f"https://api.zoom.us/v2/meetings/{meeting_id}/livestream"
	headers = {
		"Authorization": f"Bearer {access_token}",
		"Content-Type": "application/json"
	}
	payload = {
		"stream_url": stream_url,
		"stream_key": stream_key,
		"page_url": page_url
	}
	response = requests.patch(url, headers=headers, json=payload)
	response.raise_for_status()

	return