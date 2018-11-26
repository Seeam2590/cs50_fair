Project Title: CS50 Digital Fair
Submitted by: Seeam Shahid Noor
Contact: seeamnoor@college.harvard.edu
Course: CS50 at Harvard
Design Manual

Project Description: A web application that is an online version of the CS50 Fair. The website allows everyone to signup to get an account. After logging
in, users can:

Features of the web-application:
a. Write a blog on their CS50 experience
b. View all the blogs written by other CS50 students
c. Search for a blog by using specific keywords
d. View the profile of other CS50 students
e. Create their own CS50 student profile card
f. Submit their own project
g. View every project and 'like' a Project
h. View the leaderboard of projects based on 'likes'

Framework used: Django (Python Framework) has been used to build this web application
Reason for usage: Since the entire web-application can be built using Python, it is convenient.
A lot of the features of the web application can be easily implemented via Django and its 'applications' feature.
Django also has built-in database management features which ensures database management by writing Python codes instead of SQL.
Finally, Django (which uses SQLite database by default) can also switch to PostgreSQL database which can be used for more complicated web applications
with more data.

Live Project: The deployed web application can be found here - https://cs50s90.herokuapp.com/
Reason for usage: Heroku was used to host the web application because it can easily deploy Django web applications and for free.

Inside the project (Structure and reason for chosen structure):
The main directory consists of the following things:

a. *4 app folders* (I chose to divide all the features into 4 separate apps to make development easier):
  1. account - The application which takes care of user logging and authentication
  2. blog - The application which control everything related to CS50 blogs
  3. idea - The application which control everything related to CS50 projects
  4. people - The application which control everything related to students of CS50

b. media folder - Contains all the images the database stores
c. static folders - Contains all the static files the html pages use
d. git and gitignore files - These files allow the local folder to be pushed to git (if the project had multiple collaborators) or to Heroku
    (when it needs to be deployed)
e. README and DESIGN md files - Manuals for users and design description and instructions
f. manage.py - This python file takes care of major functions the web applications does
g. requirements.txt, Procfile, runtime.txt - These files ensure that the web application can be run on other computers and on Heroku smoothly
h. *cs50s90 folder* - This folder has some key files: settings.py in particular is used to connect with databases, Heroku, register new applications
  and maintain static and media files
i. db.sqlite3 - This is the database file. SQLite3 database was used since it comes as default in Django and can be easily used or deployed by Heroku (Heroku uses a PostgreSQL database be default)

Inside the *folders*:
a. url.py file - Each folder has its separate URL pattern to make it easy to organize every feature
b. views.py - Each folder has its separate views file to make it easy to design the functions that implement a feature
c. templates - Each folder has its separate templates folder with html pages that helps to keep track of the multiple html pages used and to use it
appropriately for a given feature implemented by a specific application  
d. base.html in cs50s90 folder - This base.html is used in every other html page making the other pages less complicated to write or edit since the
common code to be written in each page is taken care of.

These were the reason behind the design decisions made in the creation of this web application. Thank you for reading this!
