import requests

BACKEND_URL = "http://localhost:8080/api/events"

def send_event(data):
    try:
        requests.post(BACKEND_URL, json=data, timeout=1)
    except:
        print("Failed to send event")