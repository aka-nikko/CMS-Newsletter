# Content Management System - Newsletter
## Overview
* This project is a content management system written in Python language.
* The theme of the project is - Newsletter.
* It lets users sumbit and upload newsletters.

## Features
* Register and Login to the website.
* Newsletter Section - Lets users see the uploaded newsletters.
* Users :
  - Normal Users - Can see all newsletters (No Registration Required).
  - Contributors  - Can submit drafts for newsletter for approval. (Registration Required)
  - Admin - Can approve drafts and edit multiple drafts them into final draft and upload newsletter.
* CKEditor - A rich text editor with many features.

## Requirements
* [Python](https://www.python.org/downloads/)
* [VS Code (Or Any Other IDE)](https://code.visualstudio.com/download)
* Django Framework

## Installation
* Clone the repository and open with VS Code (or any other suitable IDE).
* Install Dependencies - 

  ```pip install -r requirements.txt```
  
* Create Super User Credentials-
  
  ```python manage.py createsuperuser```
* Run the following command from the cloned repo directory (where manage.py file is located)-

  ```python manage.py runserver```
* Open a web browser and type in the URL - ```127.0.0.1:8000```
* Register to the website and use the credentials to Login.

