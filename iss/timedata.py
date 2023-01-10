#!/usr/bin/env python3

import reverse_geocoder as rg
import datetime
import requests

URL = "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json()
    print("CURRENT LOCATION OF THE ISS: ")
    print(f"Timestamp: {datetime.datetime.fromtimestamp(resp['timestamp'])}")
    print(f"Lon: {resp['iss_position']['longitude']}")
    print(f"Lat: {resp['iss_position']['latitude']}")
    coords = (resp['iss_position']['latitude'], resp['iss_position']['longitude'])
    result = rg.search(coords, verbose=False)
    print(f"City/Country: {result[0]['name']}, {result[0]['cc']}")

if __name__ == "__main__":
    main()
