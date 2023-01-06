#!/bin/env python3

spider_man = {"name": "Peter Parker", 
              "relatives": "Uncle Ben", 
              "powers": ["shoot webs", "spidey sense"], 
              "quotes": "Does whatever a spider does"}

batman = {"name": "Bruce Wayne", 
          "relatives": ["Damian", "Alfred"],
          "powers": ["money", "ninja", "detective"], 
          "quotes": "vengeance"}

marias_mom = {"name": "Ana",
              "relative": "Maria",
              "powers": "love",
              "quotes": "best mom ever <3"}

heroes = [spider_man, batman, marias_mom]

print("The superheroes names are: ", heroes[0]["name"] + ",", heroes[1]["name"] + ",", "and", heroes[2]["name"])


