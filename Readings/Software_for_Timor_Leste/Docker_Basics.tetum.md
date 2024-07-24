'# Guia Komprehensivu ba Docker

## Tabela Husi Konteudu
1. [Introdusaun ba Containerization no Docker](#introdusaun-ba-containerization-no-docker)
2. [Istória husi Docker no nia Relasaun ho LXC](#istoria-husi-docker-no-nia-relasaun-ho-lxc)
3. [Imajen Docker no Konteiner](#docker-images-no-konteiner)
4. [Báziku Dockerfile](#baziku-dockerfile)
5. [Komandu Docker no Siklu Vida Konteiner](#komandu-docker-no-siklu-vida-konteiner)
6. [Networking Docker](#networking-docker)
7. [Volume Docker no Persisténsia Dadus](#volume-docker-no-persistensia-dadus)
8. [Docker Compose](#docker-compose)
9. [Prátika Di'ak no Seguransa Docker](#pratika-diak-no-seguransa-docker)
10. [Konkluzaun](#konkluzaun)

## 1. Introdusaun ba Containerization no Docker

### Saida mak Containerization?

Containerization mak forma leví husi virtualizasaun ne'ebé permite ita atu halai aplikasaun sira no sira nia dependénsia iha prosesu ida-ne'ebé izola rekursu. Konteiner sira mak pakote ne'ebé bele halao, ne'ebé inklui hotu-hotu presiza atu halai software ida, inklui kódigu, runtime, ferramenta sistema, biblioteka, no konfigurasaun.

Benefísiu importante husi containerization inklui:
- Konsisténsia iha ambiente sira ne'ebé la hanesan
- Efisiénsia no utilizasaun rekursu ne'ebé hadi'a
- Deployment no skalamentu ne'ebé lais
- Izolamentu no seguransa

### Introdusaun ba Docker no nia Arkitetura

Docker mak plataforma open-source ne'ebé automatiza deployment, skalamentu, no jestaun husi aplikasaun liuhusi containerization. Nia fornese maneira padraun atu halao kódigu, simplifika prosesu atu kria, deploy, no halai aplikasaun.

Arkitetura Docker konsiste husi:
1. **Motor Docker**: Nukleu husi Docker, responsável ba kria no halai konteiner.
2. **Kliente Docker**: Maneira prinsipál ne'ebé uza-na'in interaje ho Docker liuhusi linha komandu.
3. **Daemon Docker**: Servisu iha background ne'ebé jere objetu Docker hanesan imajen, konteiner, rede, no volume.
4. **Registry Docker**: Repositóriu ba armazena no distribui imajen Docker.

### Instala Docker

Atu instala Docker iha ita-nia komputadór:

1. Vizita website ofisiál Docker: https://www.docker.com/get-started
2. Download versaun ne'ebé apropriadu ba ita nia sistema operasaun (Windows, macOS, ka Linux).
3. Tuir instrusaun instalasaun ne'ebé fornese ba ita nia OS.
4. Verifika instalasaun liuhusi halao `docker --version` iha ita nia terminal ka command prompt.

## 2. Istória Docker no nia Relasaun ho LXC

### Origem husi Docker

Docker kria husi Solomon Hykes hanesan projetu internál iha kompañia ida naran dotCloud, ne'ebé fornese Plataforma-hanesan-Servisu. Projetu hahu iha 2013 no inisiálmente kria ho baze iha teknolojia LXC (Linux Containers).

### LXC no nia Papél

LXC (Linux Containers) mak metodu virtualizasaun iha nível sistema operasaun atu halao sistema Linux sira-ne'ebé izoladu barak iha anfitriun ida. Nia uza funsaun izolasaun rekursu kernel hanesan cgroups no namespaces kernel atu kria konteiner sira.

Karaterístika importante husi LXC:
- Alternativa leví ba mákina virtual tomak
- Uza kernel husi sistema anfitriun
- F

'husi Docker Hub ka ita-nia rasik imajen personalizadu.
   - Exemplu: `FROM python:3.9-slim`

2. `WORKDIR`:
   - Defini diretoriu servisu ba instrusaun sira tuir mai iha Dockerfile.
   - Se diretoriu la ezisti, nia sei kria.
   - Hanesan ho hakotu `cd` iha shell.
   - Exemplu: `WORKDIR /app`

3. `COPY` ka `ADD`:
   - Kopia dokumentu sira husi komputador nian ba imajen.
   - `COPY` simples liu no preferidu iha kazu barak.
   - `ADD` iha karakterístika sira seluk, hanesan extrai automaticamente ficheiro tar no suporta URLs.
   - Exemplu: `COPY . /app` ka `ADD http://example.com/file.tar.gz /tmp/`

4. `RUN`:
   - Executa komandu iha kapa foun iha leten husi imajen atual.
   - Uza atu instala pakote sira, executa skript sira, ka halo aksaun sira ne'ebé presiza ba prepara imajen.
   - Kada instrusaun `RUN` kria kapa foun iha imajen.
   - Exemplu: `RUN pip install --no-cache-dir -r requirements.txt`

5. `ENV`:
   - Defini variável ambiente iha imajen.
   - Variável sira-ne'e sei kontinua bainhira konteiner halao husi imajen.
   - Útil ba defini konfigurasaun ka informasaun kona-ba dalan.
   - Exemplu: `ENV DEBUG=false`

6. `EXPOSE`:
   - Informa Docker katak konteiner sei rona iha portu rede espesífiku iha tempu execusaun.
   - La publika portu duni; nia funsiona nudar dokumentasaun.
   - Ita sei presiza uza `-p` bainhira halao konteiner atu publika portu sira.
   - Exemplu: `EXPOSE 80`

7. `CMD`:
   - Fornese valor padrãu ba konteiner ne'ebé halao.
   - Iha bele iha de'it instrusaun ida CMD iha Dockerfile.
   - bele troka iha tempu execusaun.
   - Uza barak liu ba halao aplikasaun.
   - Exemplu: `CMD ["python", "app.py"]`

8. `ENTRYPOINT`:
   - Konfigura konteiner ne'ebé sei halao hanesan programa.
   - Hanesan ho CMD, maibé difisil liu atu troka iha tempu execusaun.
   - Uza barak liu ho CMD.
   - Exemplu: `ENTRYPOINT ["python"]`

9. `ARG`:
   - Defini variável ne'ebé uzuáriu sira bele pasa iha tempu harii.
   - Disponível de'it durante tempu harii imajen, la iha konteiner ne'ebé halao.
   - bele troka iha tempu harii imajen uza `--build-arg`.
   - Exemplu: `ARG VERSION=latest`

10. `VOLUME`:
    - Kria pontu montajen no marka nudar volume ne'ebé monta husi liur.
    - Útil ba dadus persistente ka partilhado.
    - Volume sira preferidu liu duke uza filesystem ba dadus persistente.
    - Exemplu: `VOLUME /data`

11. `LABEL`:
    - Aumenta metadadus ba imajen.
    - Par valor-chave ne'ebé bele uza atu organiza imajen sira ka aumenta informasaun.
    - bele hare uza komandu `docker inspect`.
    - Exemplu: `LABEL version="1.0" description="This is my Docker image"`

12. `USER`:
    - Defini naran uzuáriu ka UID atu uza bainhira halao imajen.
    - Influensia permisaun ba instrusaun sira tuir mai no bainhira halao konteiner sira.
    - Importante ba seguransa atu evita halao prosesu sira

'Volume ida:
```bash
docker executa -d -v volume-hau-nian

## 7. Docker Volumes no Persistência Dadus (kontinua)

Halo executa konteiner ho volume ida:
```bash
docker executa -d -v volume-hau-nian:/app/dadus --naran konteiner-hau-nian nginx
```

Komandu ida ne'e kria konteiner ida no monta volume `volume-hau-nian` ba diretóriu `/app/dadus` iha konteiner.

## 8. Docker Compose

Docker Compose mak feramenta ida ba define no halo executa aplikasaun Docker ho konteiner barak. Nia uza arkivu YAML atu konfigura servisu aplikasaun, rede, no volume.

### Estrutura Arkivu Docker Compose

Eis deskrisaun detalhadu ba komponente hotu-hotu iha `docker-compose.yml`:

1. `versaun`:
   - Hatudu versaun husi formatu arkivu Docker Compose.
   - Versaun diferente suporta karaterístika diferente.
   - Ezemplu: `versaun: '3.8'`

2. `servisu`:
   - Hatudu konteiner sira ne'ebé harii aplikasaun ita-nian.
   - Kada servisu pratikamente maka konteiner ida iha aplikasaun ita-nian.
   - Servisu sira bele kria husi Dockerfile ka husi registry.
   - Ezemplu:
     ```yaml
     servisu:
       web:
         harii: .
         portu:
           - "5000:5000"
     ```

3. `harii`:
   - Hatudu konfigurasaun ba harii imajen konteiner.
   - Bele diretóriu ida ne'ebé iha Dockerfile, ka konfigurasaun detalhadu.
   - Opsaun sira inklui Dockerfile personalizadu, argumentu ba harii, no seluk tan.
   - Ezemplu:
     ```yaml
     harii:
       kontestu: ./dir
       dockerfile: Dockerfile-alternate
       argumentu:
         VERSAUN: 1.0
     ```

4. `imajen`:
   - Hatudu imajen atu hahu konteiner.
   - Bele imajen lokal ka husi registry hanesan Docker Hub.
   - Ezemplu: `imajen: "redis:alpine"`

5. `portu`:
   - Halo hodi konteiner nia portu bele asesu husi anfitriun.
   - Formatu hanesan `ANFITRIUN:KONTEINER`.
   - Bele hatudu protokolu TCP/UDP.
   - Ezemplu:
     ```yaml
     portu:
       - "3000"
       - "8000:8000"
       - "49100:22/tcp"
     ```

6. `volume`:
   - Monta dalan anfitriun ka volume ho naran ba konteiner.
   - Bele uza ba dadus persistente ka atu fahe dadus entre konteiner sira.
   - Suporta tipu montajen no opsaun sira.
   - Ezemplu:
     ```yaml
     volume:
       - /var/lib/mysql
       - ./cache:/tmp/cache
       - volume-dadus:/var/lib/dadus
     ```

7. `ambiente`:
   - Hatama variável ambiente ba konteiner.
   - Bele lista ka mapa.
   - Variável sira iha ne'e sei sobrepasa sira iha Dockerfile.
   - Ezemplu:
     ```yaml
     ambiente:
       - DEBUG=1
       DB_HOST: mysql
     ```

8. `depende ba`:
   - Hatudu dependénsia entre servisu sira.
   - Garante katak servisu dependente sira hahu antes servisu ida-ne'e.
   - La hein servisu dependente sira "prontu", de'it hahu.
   - Ezemplu:
     ```yaml
     depende ba:
       - db
       - redis
     ```

9. `rede`:
   - Hatudu rede sira ne'ebé tenke servisu partisipa.
   - Bele uza hodi izola servisu sira ka grupu servisu sira.
   - Rede sira bele define iha nível topu husi ark