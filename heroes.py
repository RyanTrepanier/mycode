#! /usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

marvelchars["Starlord"]["dancing ability"] = "awesome"
marvelchars["Hulk"]["dancing ability"] = "...destructive"
marvelchars["Mystique"]["dancing ability"] = "elegant"

marvelchars["Hulk"].update({"weakness": "his temper"})



x = input("Which character do you want to know about? (Starlord, Hulk, Mystique)").title()
y = input("Choose a character stat: (real name, powers, archenemy)").lower()

while marvelchars.get(x) is None:
    
    print("Name or stat is invalid, get it together!\n\n")
    x = input("Choose a character name: ").capitalize()
    y = input("Choose a character stat: ").lower()

print(x + "'s", y, "is", marvelchars[x].get(y, "Not a valid option, get it together.").title())
