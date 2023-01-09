#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons
import json


def devicereboot(ips):
    for ip in ips:
        print(f"Connecting to.. {ip} REBOOTING NOW!")


# function to push commands
def commandpush(devicecmd):  # decivecmd==dict

    for ip in devicecmd.keys():  # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}')  # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {mycmds}')
            # we'll learn to write cod that sends cmds to device here
    return None

# start main script
def main():
    """called at runtime"""

    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)  # decode the JSON from the file to pythonic data
    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher")  # welcome message

    ## get data set
    print("\nData set found\n")  # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd)  # call function to push commands to devices
    devicereboot(devicecmd.keys())

# call our main function
main()
