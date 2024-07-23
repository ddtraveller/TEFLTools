'# Gia Detalladu: Harii Flask Aplikasaun ho PostgreSQL uza Docker Compose

## Rekizitus Projetu

1. **Aplikasaun Web**: Flask aplikasaun simples
2. **Baza Dadus**: PostgreSQL
3. **Orkestrasaun**: Docker Compose
4. **Networking**: Komunikasaun ne'ebé di'ak entre konteiner sira
5. **Persistensia Dadus**: Monta volume ba baza dadus
6. **Konfigurasaun**: Uza variavel ambiente

## Gia Pasu-husi-Pasu

### 1. Kria Flask Aplikasaun Simples

Primeiru, ami kria Flask aplikasaun. Aplikasaun ida ne'e sei iha dalan rua: ida atu hatudu mensajen boas-vindas no ida seluk atu aumenta uza-na'in sira ba baza dadus ami nian.

```python
# app.py
from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Ola, Docker!"

@app.route('/users', methods=['POST'])
def add_user():
    conn = psycopg2.connect(
        host="db",
        database="myapp",
        user="postgres",
        password="segredo"
    )
    cur = conn.cursor()
    naran = request.json['name']
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return f"Uza-na'in {name} aumenta ho suksesu!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

Kria `requirements.txt` arkivu atu espesifika dependensia Python nian:

```
Flask==2.0.1
psycopg2-binary==2.9.1
```

### 2. Kria Dockerfile ba Flask Aplikasaun

Agora, ami kria Dockerfile atu konteineriza Flask aplikasaun ami nian:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

### 3. Kria docker-compose.yml Arkivu

`docker-compose.yml` arkivu sei define aplikasaun multi-konteiner ami nian:

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
      - POSTGRES_PASSWORD=segredo
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### 4. Harii no Halao Aplikasaun

Agora, ami harii no halao aplikasaun ami nian uza Docker Compose:

```bash
$ docker-compose up --build
```

Ita tenke haree output hanesan ne'e:

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
db_1   | The files belonging to this database