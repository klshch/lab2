#!/usr/bin/python3

import cgi
import html
import http.cookies
import os

form = cgi.FieldStorage()

try:
    name = form.getfirst("name", default=" ")
    lastname = form.getfirst("lastname", default=" ")
    name = html.escape(name)
    lastname = html.escape(lastname)

    gender = form.getvalue("gender", default=" ")

    interests = ["painting", "music", "dancing", "photo", "reading"]
    interests_checkbox = {}
    for interest in interests:
        value_choice = form.getvalue(interest, default="off")
        interests_checkbox[interest] = value_choice
    

except Exception as e:
    print(f"Content-type:text/html\r\n\r\n")
    print(f"Error: {str(e)}")


print("Content-type:text/html\r\n\r\n")

template_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}

        .content {{
            text-align: left;
            padding: 30px;
            border: 3px solid darkred;
        }}
    </style>
</head>
<body>
    <div class="content">
        <h1>About you</h1>
        Your name is {name} {lastname}.
        <br>
        Your gender is {gender}.
        <br>
        Your interests: {', '.join([interest for interest, value in interests_checkbox.items() if value == 'on'])}.
        <br>
        <br>
        <b>Thank you for filling out the form!</b>
        <br>
    </div>
</body>
</html>
"""

print(template_html)
