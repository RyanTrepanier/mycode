#!/usr/bin/env python3

import netifaces
from pprint import pprint

print(netifaces.interfaces())

interfaces = netifaces.interfaces()

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:
        print('MAC: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:
        print('Could not collect adapter information')

def getip(interface):
    ip = (netifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr']
    print(f'\nIP for {interface} is {ip}\n')

def getmac(interface):
    mac = (netifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr']
    print(f'\nMAC for {interface} is {mac}')


choice = input(f'Choose an interface: ({interfaces})')
getip(choice)
choice = input(f'Choose an interface to get their MAC address: ({interfaces}) ')
getmac(choice)
