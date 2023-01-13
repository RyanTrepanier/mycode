#!/usr/bin/env python3

import os
import paramiko

def commandissue(command_to_issue, sshsession):
    stdin, stdout, stderr = sshsession.exec_command(command_to_issue)
    return stdout.read().decode('utf-8')

def main():
    sshsession = paramiko.SSHClient()

    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    for x in our_commands:
        print(commandissue(x, sshsession))

if __name__ == "__main__":
    main()