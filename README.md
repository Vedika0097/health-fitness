## Features: 

- `Up-to-date Dependencies`, Best practices
- Desing: Material
- Extended User Profile 
- (optional) API Generator
- (optional) Celery
- (optional) OAuth Github, Google
- (optional) CI/CD for Render
- (optional) Docker

<br />

## Start Project with Docker

> In case the starter was built with Docker support, here is the start up CMD:

```bash
$ docker-compose up --build
```

Once the above command is finished, the new app is started on `http://localhost:5085`

<br />

## Manual Build 

> Download/Clone the sources  

```bash
$ git clone https://github.com/Vedika0097/health-fitness.git
$ cd health-fitness
```

<br />

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> `Set Up Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> `Start the App`

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

> `Run celery`

```bash
$ celery -A core worker --concurrency 2 -l info
```

> `Execute celery tasks`

```bash
$ python manage.py shell

# Shell commands
>> from home.tasks import add
>> result = add.delay(5, 6)
>> result.get()
11  # output
```

<br />
