# MSSTATE-DAS-Experts-List-
Repository for the development of a Django experts list for the MSSTATE Department of Arts and Sciences. 

To Run Locally
- First, make your own branch to work on, and then run locally.
- download python https://www.python.org/downloads/
- open command prompt at the directory of the github folder run
- run "python -m venv venv"
- run ".\venv\Scripts\activate"
  - if that did not work
  - cd venv
  - cd Scripts
  - run ".\activate"
- run "python -m pip install Django"
- run "python -m pip install Pillow"
- navigate to the "Django" directory
- run "py manage.py createsuperuser"
- follow the steps to create a superuser
- run "py manage.py runserver"
- navigate to 192.168.0.0:8000/admin
- login using the superuser you created
