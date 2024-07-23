'# Di'ak liu Práticas Docker no Gía Uza iha Mundu Reál

## Tabela husi Konteúdu
1. [Práticas Di'ak liu Docker](#docker-best-practices)
2. [Kazu Uza Docker iha Mundu Reál](#real-world-docker-usage-scenarios)

## Práticas Di'ak liu Docker

### 1. Uza Imajen Ofisiál Baze
- Hahu ho imajen ofisiál husi Docker Hub bainhira posível.
- Imajen sira-ne'e hetan manutensaun, seguru, no otimizadu ba Docker.
- Ezemplu: `FROM python:3.9-slim` la'ós husi imajen Python kustum.

### 2. Minimiza Layers
- Kombina komandos hodi redús númeru husi layers iha imajen ita-nia.
- Uza multi-liña komandos ho `&&` no `\` ba fasil le'e.
- Ezemplu:
  ```dockerfile
  RUN apt-get update && \
      apt-get install -y package1 package2 && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/*
  ```

### 3. Implementa Multi-palku Builds
- Uza multi-palku builds hodi kria imajen produsaun ki'ik liu.
- Harii artifacts iha ida palku no kopia de'it arkiu nesesáriu ba palku finál.
- Ezemplu:
  ```dockerfile
  FROM node:14 AS builder
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  RUN npm run build

  FROM nginx:alpine
  COPY --from=builder /app/build /usr/share/nginx/html
  ```

### 4. La Halao hanesan Administrador
- Uza instrusaun `USER` hodi hatudu uza-na'in la hanesan administrador.
- Kria uza-na'in no grupu iha Dockerfile se nesesáriu.
- Ezemplu:
  ```dockerfile
  RUN groupadd -r appuser && useradd -r -g appuser appuser
  USER appuser
  ```

### 5. Uza .dockerignore
- Esklui arkiu sira la nesesáriu husi kontestu harii.
- Hadia prestasaun harii no redús tamañu imajen.
- Ezemplu `.dockerignore`:
  ```
  node_modules
  npm-debug.log
  Dockerfile
  .dockerignore
  .git
  .gitignore
  ```

### 6. Tag Imajen ho Di'ak
- Uza tag ho signifikadu ba imajen ita-nia, la'ós de'it `latest`.
- Inklui informasaun versaun ka númeru harii.
- Ezemplu: `myapp:v1.2.3` ka `myapp:20210615-1`

### 7. Uza Cache Harii
- Ordena instrusaun Dockerfile husi ki'ik liu ba ki'ik liu muda.
- Fatin komandos ne'ebé menus provável muda sedu iha Dockerfile.
- Ezemplu orden:
  1. FROM
  2. WORKDIR
  3. COPY package*.json ./
  4. RUN npm install
  5. COPY . .
  6. CMD

### 8. Uza Variável Ambiente
- Parameteriza Dockerfiles no compose files ita-nia.
- Torná imajen liu tan flexível no reutilizável.
- Ezemplu:
  ```dockerfile
  ENV APP_HOME /app
  WORKDIR $APP_HOME
  ```

### 9. Implementa Health Checks
- Aumenta instrusaun HEALTHCHECK ba Dockerfile ita-nia.
- Ajuda Docker hodi determina se kontentor maka hela servisu.
- Ezemplu:
  ```dockerfile
  HEALTHCHECK CMD curl --fail http://localhost:8080 || exit 1
  ```

### 10. Halo Scan Seguransa
- Regularmente scan imajen ita-nia ba vulnerabilidade.
- Uza ferramenta hanesan Docker Security Scanning, Clair, ka Trivy.
- Integra scanning ba iha pipeline CI/CD ita-nia.

## Kazu Uza Docker iha Mundu Reál

### 1. Arquitetura Microservices