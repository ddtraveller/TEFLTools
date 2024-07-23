Títulu: Halo Deploy aplikasaun Flask iha Kubernetes ho Docker: Guia Komprehensivu

1. Rekézitu
- Docker instaladu iha ita-nia mákina lokal
- Konjuntu Kubernetes estabelese (bisa uza Minikube ba dezenvolvimentu lokal)
- kubectl konfiguradu atu komunika ho ita-nia konjuntu

2. Kria aplikasaun Flask simples

Liu hosi primeiru, ami kria aplikasaun Flask báziku:

```python
# app.py
husi flask importa Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Kubernetes!"

se __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

3. Kria Dockerfile

Oinsá, kria Dockerfile iha direktóriu hanesan:

```dockerfile
HUSI python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

Mós, kria arkivu `requirements.txt`:

```
Flask==2.0.1
```

4. Harii no Manda Imajen Docker

Harii imajen Docker:

```bash
docker build -t ita-nia-username-dockerhub/flask-k8s:v1 .
```

Manda imajen ba Docker Hub (ka ita-nia registu konteiner preferidu):

```bash
docker push ita-nia-username-dockerhub/flask-k8s:v1
```

5. Kria Kubernetes Deployment YAML

Kria arkivu ho naran `flask-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-app
        image: ita-nia-username-dockerhub/flask-k8s:v1
        ports:
        - containerPort: 5000
```

6. Kria Kubernetes Service YAML

Kria arkivu ho naran `flask-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  selector:
    app: flask-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer
```

7. Halo Deploy ba Kubernetes

Aplika Deployment:

```bash
kubectl apply -f flask-deployment.yaml
```

Aplika Servisu:

```bash
kubectl apply -f flask-service.yaml
```

8. Verifika Deployment

Hare se pods la'o:

```bash
kubectl get pods
```

Ita tenki hare pods tolu la'o ba ita-nia aplikasaun Flask.

Hare servisu:

```bash
kubectl get services
```

Ita tenki hare ita-nia `flask-service` lista.

9. Aksesu ba aplikasaun

Se ita uza Minikube, ita bele hetan URL husi ita-nia servisu ho:

```bash
minikube service flask-service --url
```

Se ita uza provedor nuvem, servisu tipo LoadBalancer sei fornese IP esternal. Ita bele hetan ida ne'e ho:

```bash
kubectl get services
```

Hare IP esternal husi ita-nia `flask-service`.

10. Eskala aplikasaun

Atu eskala aplikasaun, ita bele modifika 'replicas' iha deployment YAML no reaplika, ka uza komandu kubectl scale:

```bash
kubectl scale deployment flask-app --replicas=5
```

11. Update aplikasaun

Atu update ita-nia aplikasaun:

1. Halo mudansa ba ita-nia aplikasaun Flask
2. Harii imajen Docker foun ho tag foun:
   ```bash
   docker build -t ita-nia-username-dockerhub/flask-k8s:v2 .
   docker push ita-nia-username-dockerhub/flask-k8s:v2
   ```
3. Update deployment:
   ```bash
   kubectl set image deployment/flask-app flask-app=ita-nia-username-dockerhub/flask-k8s:v2
   ```

12. Hamoos