#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    if farm['name'] == 'NE Farm':
        print(farm['agriculture'])


farm = input("\nChoose a farm: (NE Farm, W Farm, or SE Farm)")
farm = farm.lower()
for f in farms:
    if f['name'].lower() == farm:
        print(f['agriculture'])



farm = input("\nChoose another farm: (NE Farm, W Farm, or SE Farm)")
farm = farm.lower()
plants = ['carrots', 'celery']
for f in farms:
    if f['name'].lower() == farm:
        for ag in f['agriculture']:
            if ag not in plants:
                print(ag, sep=" ")
