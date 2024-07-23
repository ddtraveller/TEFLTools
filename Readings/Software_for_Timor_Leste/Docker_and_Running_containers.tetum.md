'# Halo no Interaksi ho Docker Containers: Guia Prátika

## Tabela Husi Konteúdu
1. [Introduksaun](#introduksaun)
2. [Halo Docker Container](#halo-docker-container)
3. [Aksesu ba Shell husi Container ne'ebé Halo ona](#aksesu-ba-shell-husi-container-ne'ebé-halo-ona)
4. [Modu Diferente atu Halo Containers](#modu-diferente-atu-halo-containers)
5. [Interaksi ho Containers](#interaksi-ho-containers)
6. [Interaksi Avansadu ho Container](#interaksi-avansadu-ho-container)
7. [Konklusaun](#konklusaun)

## 1. Introduksaun

Docker containers oferese ambiente ne'ebé leves, portátil ba halo aplikasaun. Guia ne'e sei orienta ita liu husi prosesu halo Docker container, aksesu ba nia shell, no buka modu diferente atu halo interaksi ho containers. Ami sei uza simples Nginx web server container hanesan ezemplu.

## 2. Halo Docker Container

Hahu husi halo básiku Nginx container:

```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

Komandu ne'e halo tuir mai:
- `-d`: Halo container iha modu ne'ebé lahatene (iha antesedente)
- `-p 8080:80`: Mapeia portu 8080 husi host ba portu 80 iha container
- `--name my-nginx`: Naran container "my-nginx"
- `nginx`: Espesifika imajen atu uza (iha kazu ida ne'e, imajen Nginx foun liu)

Hafoin halo komandu ida ne'e, ita tenke haree string naruk ida, ne'ebé mak hanesan ID container. Ita bele verifika katak container halo tiha ona ho:

```bash
docker ps
```

Ita tenke haree "my-nginx" container iha lista.

## 3. Aksesu ba Shell husi Container ne'ebé Halo ona

Atu aksesu shell husi container ne'ebé halo ona, uza `docker exec` komandu:

```bash
docker exec -it my-nginx /bin/bash
```

Komandu ida ne'e:
- `exec`: Halo komandu iha container ne'ebé halo ona
- `-it`: Oferece terminal interativu
- `my-nginx`: Especifica naran container
- `/bin/bash`: Komandu atu halo (iha kazu ida ne'e, hahú Bash shell)

Ohin ita iha laran container! Ita bele halo komandu, navega iha sistema ficheiro, no halo interaksi ho ambiente container. Ezemplu:

```bash
ls /etc/nginx
cat /etc/nginx/nginx.conf
```

Atu sai husi shell container, de'it hakerek `exit`.

## 4. Modu Diferente atu Halo Containers

### 4.1 Halo iha Foreground

Laiha modu hatene, ita bele halo container iha foreground:

```bash
docker run --rm -p 8080:80 nginx
```

Bandeira `--rm` automaticamente hasai container bainhira sei. Ne'e útil ba container temporáriu.

### 4.2 Halo ho Variável Ambiental

Ita bele pasa variável ambiental ba container:

```bash
docker run -d -p 8080:80 -e NGINX_HOST=example.com -e NGINX_PORT=80 nginx
```

### 4.3 Halo ho Volumes

Monta diretória lokal ba container:

```bash
docker run -d -p 8080:80 -v /local/path:/usr/share/nginx/html nginx
```

Ne'e monta `/local/path` husi ita nia host ba `/usr/share/nginx/html` iha container.

### 4.4 Halo ho Konfigurasaun Rede

Kria rede ida personalizadu no halo container iha ne'ebé:

```bash
docker network create my-network
docker run -d --network my-network --name my-nginx nginx
```

## 5. Interaksi ho Containers

### 5.1 Haree Log Container

Atu haree log husi container:

```bash