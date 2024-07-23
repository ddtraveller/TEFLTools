'Loron 10: Previsualizasaun Docker Orchestration no Kursu Remata

## Tabela Konaba Konteúdu
1. [Introdusaun](#introdusaun)
2. [Lisao 19: Introdusaun ba Orkestrasaun Container (Kubernetes Previsualizasaun)](#lisao-19-introdusaun-ba-orkestrasaun-container-kubernetes-previsualizasaun)
3. [Lisao 20: Prátika Di'ak no Uzu Docker iha Mundu Real](#lisao-20-pratika-diak-no-uzu-docker-iha-mundu-real)
4. [Projetu Final: Halo Deploy ba Aplikasaun Containerizada](#projetu-final-halo-deploy-ba-aplikasaun-containerizada)
5. [Konklusaun](#konklusaun)

## 1. Introdusaun

Ha'u hamosu iha loron ikus husi amia-nia kursu Docker, ita sei esplora pasu tuir mai iha containerization: orkestrasaun. Mós sei reviza prátika di'ak ba uzu Docker iha situasaun mundu real no uza ita-nia koñesimentu hodi halo testu ho projetu ikus. Loron ida ne'e serbi hanesan ponte entre uzu básiku Docker no téknika jestaun container avansadu liu.

## 2. Lisao 19: Introdusaun ba Orkestrasaun Container (Kubernetes Previsualizasaun)

### 2.1 Orkestrasaun Container ne'ebé saida?

Orkestrasaun container refere ba aranju automatiku, koordenasaun, no jestaun husi software containers. Ha'u hamosu aplikasaun sira aumenta iha kompleksidade no eskala, jestaun husi container individuál sai difisil. Ferramenta orkestrasaun rezolve problema ida ne'e liuhosi fornese:

- Deployment automatiku no eskala husi containers
- Balansu Karga
- Deskoberta Servisu
- Alokasaun Rekursu
- Monitorizasaun Saúde no Auto-Kura

### 2.2 Introdusaun ba Kubernetes

Kubernetes (K8s) mak plataforma orkestrasaun container ne'ebé popular liu. Originálmente Google nian, agora Cloud Native Computing Foundation mak tau matan ba.

Koñesimentu Xave Kubernetes:
- **Pods**: Unidade mínima ne'ebé bele halo deploy iha Kubernetes, konsiste husi ida ka liu container.
- **Servisus**: Forma abstratu hodi expoe aplikasaun ne'ebé funsiona iha grupu pods.
- **Deployment**: Deskreve estadu dezijádu ba Pods no ReplicaSets.
- **Namespaces**: Cluster virtuál sira ne'ebé apoiadu husi cluster fíziku hanesan.

### 2.3 Arquitetura Bázika Kubernetes

Kubernetes uza arquitetura mestre-nó:
- **Mestre Nó**: Kontrola cluster
  - API Server: Front-end ba painel kontrolu Kubernetes
  - Scheduler: Atribui servisu ba nó sira
  - Controller Manager: Kontrola estadu sistema
  - etcd: Loja valor-chave distribuídu ba dadus cluster
- **Nó Traballadór**: Halo funsiona traballu container ne'ebé atual
  - Kubelet: Garante katak containers halao iha pod ida
  - Kube-proxy: Mantein regra rede iha nó sira
  - Container Runtime: Software ne'ebé responsável ba halao containers (exemplu, Docker)

### 2.4 Ezemplu Simples Kubernetes

Iha ne'e ezemplu báziku ida husi Deployment Kubernetes:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Ficheiru YAML ida ne'e deskreve Deployment ne'ebé kria replika tolu husi container Nginx.

## 3. Lis