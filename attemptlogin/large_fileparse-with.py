#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Solution to Customization 01"""

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0 # total times we see pattern, "-] Authorization failed"
get = 0
post = 0
failips = []

# open the file for reading
with open("/home/student/mycode2/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:

        if "GET" in line:
            get += 1
        if "POST" in line:
            post += 1
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            ip = line.split()[-1]
            failips.append(ip)
            with open("errors.txt", "a") as errorfile:
                errorfile.write(line + "\n")

# display the number of failed log in attempts
print("The number of failed log in attempts is", loginfail)

# display the number of successful log in attempts
print("The number of POSTs is", post, "and GETs is", get)



