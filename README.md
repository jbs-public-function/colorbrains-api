# colorbrains-api
An Api To Serve Color Information For A Machine Learning Project On Colors.

# colorbrains-db

### Postgres Database to support Colorbrains API work.

`docker-compose up`

### Connect to postgres database

#### Via Running Container

`$> docker ps`
```
CONTAINER ID   IMAGE             COMMAND                  CREATED              STATUS              PORTS                    NAMES
{container id}   postgres:latest   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5450->5432/tcp   colorbrains-db
```

`docker exec -it {container id} /bin/bash`

`$> psql -U colorbrains`

#### Via host machine command line

`psql -h localhost -U colorbrains -W colorbrains -p 5450`
