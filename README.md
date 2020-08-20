
## How to run the app 
- Clone to local repo
- Change directory to repo `cd BlogSite`
- Create a virtual env 

 ```
 python3 -m venv env 
 source env/bin/activate
 ```

- Install app requirements `pip install -r requirements.txt`
- Make migrations `python manage.py makemigrations`
- Then run Migrate `python manage.py migrate`
- Create user for admin `python manage.py createsuperuser`
- Run app `python manage.py runserver`




add app to installed apps in settings
snippets are reused views