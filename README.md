# colorbrains-api
An Api To Serve Color Information For A Machine Learning Project On Colors.


```
#### Initialize & Populate DB And Start FastApi Service
docker-compose up

#### localhost DB instance
psql -h localhost -U colorbrains -W colorbrains -p 5432
```

### .env file
```
export POSTGRES_USER={colorbrains-user}
export POSTGRES_PASSWORD={colorbrains-userpassword}
export POSTGRES_DB={colorbrains-dbname}
export POSTGRES_PORT={colorbrains-dbport}
export POSTGRES_HOST={colorbrains-dbhost}
```
