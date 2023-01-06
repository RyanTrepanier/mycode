#!/usr/bin/env python3
"""Review of try and except logic | Alta3 Research"""

# Start with an infinite loop
while True:
    try:
        name = input("Enter a file name: ")
        with open(name, "w") as myFile:
            myFile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")
