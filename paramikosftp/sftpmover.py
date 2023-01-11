#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

def movethemfiles(sftp):
    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
         if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            try:
                sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
            except:
                print("Location does not exit! Exiting..")



def main():
    dest = input("Enter destination path:\n>")

    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username="bender", password="alta3")

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    movethemfiles(sftp)

    ## close the connections
    sftp.close() # close the connection
    t.close()

if __name__ == "__main__":
    main()
