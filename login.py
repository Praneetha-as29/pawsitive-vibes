#!/usr/bin/python3
import cgi
import csv

print("Content-type: text/html\n")  # Required for CGI

# Get form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Check login credentials
user_found = False
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[4] == username and row[5] == password:
            user_found = True
            break

if user_found:
    print("<h1>✅ Login Successful!</h1>")
    print('<a href="home.html">Go to Home</a>')
else:
    print("<h1>❌ Invalid Username or Password!</h1>")
    print('<a href="login.html">Try Again</a>')
