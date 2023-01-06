#!/usr/bin/env python3

dracula = open("dracula.txt", "r")
count = 0
for line in dracula:
    if "vampire" in line.lower():
        print(line)
        with open("vampytimes.txt", "a") as vamps:
            vamps.write(line)
        count += 1
dracula.close()



