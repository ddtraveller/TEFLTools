# Detailed Guide: Deploying a Flask Application with PostgreSQL using Docker Compose

## Project Requirements

1. **Web Application**: A simple Flask app
2. **Database**: PostgreSQL
3. **Orchestration**: Docker Compose
4. **Networking**: Proper communication between containers
5. **Data Persistence**: Volume mounting for the database
6. **Configuration**: Environment variable usage

## Step-by-Step Guide

### 1. Create a Simple Flask Application

First, let's create our Flask application. This app will have two routes: one to display a welcome message and another to add users to our database.

```python
# app.py
from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

@app.route('/users', methods=['POST'])
def add_user():
    conn = psycopg2.connect(
        host="db",
        database="myapp",
        user="postgres",
        password="secret"
    )
    cur = conn.cursor()
    name = request.json['name']
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return f"User {name} added successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

Create a `requirements.txt` file to specify the Python dependencies:

```
Flask==2.0.1
psycopg2-binary==2.9.1
```

### 2. Create a Dockerfile for the Flask App

Now, let's create a Dockerfile to containerize our Flask application:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

### 3. Create a docker-compose.yml File

The `docker-compose.yml` file will define our multi-container application:

```yaml
version: '3'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db/myapp
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### 4. Build and Run the Application

Now, let's build and run our application using Docker Compose:

```bash
$ docker-compose up --build
```

You should see output similar to this:

```
Creating network "myapp_default" with the default driver
Building web
Step 1/6 : FROM python:3.9-slim
 ---> 254d4a8a8f31
Step 2/6 : WORKDIR /app
 ---> Using cache
 ---> 9b8f48e8dcb1
Step 3/6 : COPY requirements.txt .
 ---> Using cache
 ---> f326ae5526d1
Step 4/6 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Using cache
 ---> 7e477a2abae1
Step 5/6 : COPY app.py .
 ---> 8d6f2e8f6128
Step 6/6 : CMD ["python", "app.py"]
 ---> Running in a7e3d8461fd7
Removing intermediate container a7e3d8461fd7
 ---> 4b5a48e6bb77
Successfully built 4b5a48e6bb77
Successfully tagged myapp_web:latest
Pulling db (postgres:13)...
13: Pulling from library/postgres
...
Status: Downloaded newer image for postgres:13
Creating myapp_db_1  ... done
Creating myapp_web_1 ... done
Attaching to myapp_db_1, myapp_web_1
db_1   | The files belonging to this database system will be owned by user "postgres".
...
web_1  |  * Serving Flask app 'app' (lazy loading)
web_1  |  * Environment: production
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |    Use a production WSGI server instead.
web_1  |  * Debug mode: off
web_1  |  * Running on all addresses.
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |  * Running on http://172.18.0.3:5000/ (Press CTRL+C to quit)
```

This output shows that Docker Compose has:
1. Created a network for our application
2. Built the web service image
3. Pulled the PostgreSQL image
4. Created and started containers for both services

### 5. Test the Application

Now that our application is running, let's test it by adding a user:

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe"}' http://localhost:5000/users
```

You should see the response:

```
User John Doe added successfully!
```

If you check the Docker Compose logs, you should see a new log entry in the web service:

```
web_1  | 172.18.0.1 - - [25/Jun/2023 12:34:56] "POST /users HTTP/1.1" 200 -
```

This indicates that our POST request was successful.

## Explanation of Key Concepts

1. **Docker Compose**: Docker Compose allows us to define and run multi-container Docker applications. In our `docker-compose.yml`, we defined two services: `web` (our Flask app) and `db` (PostgreSQL).

2. **Networking**: Docker Compose automatically creates a network and connects our containers to it. This is why our Flask app can connect to the database using the hostname `db`.

3. **Volume Mounting**: In the `docker-compose.yml`, we defined a volume `postgres_data` and mounted it to `/var/lib/postgresql/data` in the `db` service. This ensures that our database data persists even if the container is stopped or removed.

4. **Environment Variables**: We used environment variables in both services:
   - In the `web` service, we set `DATABASE_URL` which could be used to configure our database connection (though in this example, we hardcoded the connection details).
   - In the `db` service, we set `POSTGRES_DB` and `POSTGRES_PASSWORD` to configure our PostgreSQL instance.

5. **Dependency Management**: The `depends_on` option in the `web` service ensures that the `db` service is started before the `web` service.

This project demonstrates a basic setup of a web application with a database using Docker. It showcases key Docker concepts including multi-container applications, networking, volume mounting, and environment variable usage.