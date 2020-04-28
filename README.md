# Project Title:
CS50 Digital Fair
Submitted by: Seeam Shahid Noor
Contact: seeamnoor@college.harvard.edu
Course: CS50 at Harvard
User Manual

# Project Description:
A web application that is an online version of the CS50 Fair. The website allows everyone to signup to get an account. After logging
in, users can:

# Features of the web-application:

a. Write a blog on their CS50 experience  
b. View all the blogs written by other CS50 students  
c. Search for a blog by using specific keywords  
d. View the profile of other CS50 students  
e. Create their own CS50 student profile card  
f. Submit their own project  
g. View every project and 'like' a Project  
h. View the leaderboard of projects based on 'likes'  

Framework used: Django (Python Framework) has been used to build this web application

# Live Project:
The deployed web application can be found here - https://cs50s90.herokuapp.com/

# Project Description:
The video description of the project can be found at: https://youtu.be/A8BNNN7_WlU

# Implementation:

The whole web application can be used using the command terminal.

# In order to get started:

a. Install python into your computer - https://realpython.com/installing-python/ 
b. Install pip - https://www.makeuseof.com/tag/install-pip-for-python/ 
c. Install virtualenv - https://docs.python-guide.org/dev/virtualenvs/

You will be requiring a few packages to run this web application on your local server. To make sure the packages doesn't cause problems with other programs your computer might run in the future, it is more efficient to install those packages while being inside virtualenv.

d. Make sure you have pip, virtualenv and python in the Path environment variable in your computer - https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path

These instructions show only how add python to path, others can be done in similar ways

# Downloading:
a. Download the project directory to your computer  
b. Open up your command terminal  
c. Activate your virtual environment  
d. Move to where the project directory is so that you are in the directory where the file 'requirements.txt' is
e. Run the command (for Windows):   pip install -r requirements.txt  
This ensures that all the packages required to run the web application locally in your server is installed inside a virtual environment

# Setting up and running (while still being in the command terminal):
a. Create a Superuser, which you will need to have admin login to your web application:   python manage.py createsuperuser
When prompted, insert the username, email and password you want to use to login as admin.  
b. Run these two commands next to ensure that your Django database has every required models to run the web application:
python manage.py makemigrations
python.manage.py migrate  
c. Finally, run the command:  python manage.py runserver  
Don't close the command terminal since the web application can only be accessed when the local server is running. Press 'ctrl + c' to quit the
server anytime.  
d. In your browser to start the website, type in:     localhost:8000  
e. The web application is ready to be used! In order to delete entries, access the admin panel be using superuser credentials at:
localhost:8000/admin

Chech DESIGN.md for technical details for the project.  
I sincerely hope you enjoy using the web application. Thank you for reading this!
