# Restaurant menu

## Run in docker

* create .env like .env.dev 
```docker-compose --env-file .env up -d --build ```

## Run local 

* create env 
* setup requirements.txt  (if you use virtual env: )  
``` pip insall -r requirements.txt ```
* create .env like .env.dev 
* setup db in .env   
``` python manage.py migrate ```  
``` python manage.py runserver ```


## Tests

### run api tests 

```sudo python manage.py test api.tests```
