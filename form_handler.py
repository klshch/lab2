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

    print(f"Set-Cookie: name={name};")
    print(f"Set-Cookie: lastname={lastname};")
    

except Exception as e:
    print(f"Content-type:text/html\r\n\r\n")
    print(f"Error: {str(e)}")


cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name_cookie = cookie.get("name").value
lastname_cookie = cookie.get("lastname").value

count_cookie = int(cookie.get("count_cookie").value) if "count_cookie" in cookie else 0
count_cookie += 1

print(f"Set-Cookie: count_cookie={count_cookie};")

if "delete_cookies" in form:
    print("Set-Cookie: name_cookie=" "; expires=Thu, 01 Jan 1970 00:00:00 GMT;")
    print("Set-Cookie: lastname_cookie=" "; expires=Thu, 01 Jan 1970 00:00:00 GMT;")
    print("Set-Cookie: count_cookie=" "; expires=Thu, 01 Jan 1970 00:00:00 GMT;")


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
        <br>
        <br>
        <h2>From cookie:</h2>
        Name - {name_cookie} Lastname - {lastname_cookie} 
        <br>
        Number of submitted forms: {count_cookie}
        <br>
        If you want you can delete all cookies: 
        <br>
        <form action=" " method="post">
            <input type="hidden" name="delete_cookies" value="1">
            <input type="submit" value="Delete">
        </form>
    </div>
</body>
</html>
"""

print(template_html)
