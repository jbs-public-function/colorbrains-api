# colorbrains-api
An Api To Serve Color Information For A Machine Learning Project On Colors.


```
#### run the fastapi service
docker-compose run -d -p 80:80 colorbrains-api

#### startup the DB
docker-compose up

#### localhost DB instance
psql -h localhost -U colorbrains -W colorbrains -p 5432
```

### .env file
export POSTGRES_USER={colorbrains-user}
export POSTGRES_PASSWORD={colorbrains-userpassword}
export POSTGRES_DB={colorbrains-dbname}
export POSTGRES_PORT={colorbrains-dbport}
export POSTGRES_HOST={colorbrains-dbhost}
