#!/usr/bin/env python3

import csv
import paramiko

def main():
    with open("creds.csv", "r") as file1:
        for row in csv.reader(file1):
            mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
            sshsession = paramiko.SSHClient()
            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print(f"Connecting to... {row[0]} @{row[1]}")
            sshsession.connect(hostname=row[1], username=row[0], pkey=mykey)
            sshsession.exec_command("touch /home/" + row[0] + "/goodnews.everyone")
            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + row[0])
            with open("results.log", "a") as results:
                results.write(sessout.read().decode('utf-8'))
            sshsession.close()
        print("Output for ls command is in results.log")


main()
