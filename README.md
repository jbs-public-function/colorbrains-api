#
# colorbrains-api
An Api To Serve Color Information For A Machine Learning Project On Colors.

`docker-compose up colorbains-api`

http://0.0.0.0:80/docs

#

# colorbrains-db

### Postgres Database to support Colorbrains API work.

`docker-compose up colorbrains-db`
 
### Connect to postgres database

#### Via host machine command line

`psql -h localhost -U colorbrains -W colorbrains -p 5450`
