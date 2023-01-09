#!/usr/bin/env python3

import requests

url = "https://www.boredapi.com/api/activity/"
activity = requests.get(url).json()

print(f"Try {activity['activity']}")
