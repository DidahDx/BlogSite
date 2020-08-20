
## How to run the 
- clone to local repo
- create a virtual env 

 ```
 python3 -m venv env 
 source env/bin/activate

 ```

- Install app requirements `pip install -r requirements.txt`
- Make migrations `python manage.py makemigrations`
- Then run Migrate `python manage.py migrate`
- Run app `python manage.py runserver`



add app to installed apps in settings
snippets are reused views