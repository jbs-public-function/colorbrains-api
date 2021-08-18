import os
from dataclasses import dataclass

import psycopg2


@dataclass
class DbAssistant:
    dbname: str=os.getenv('POSTGRES_DB')
    user: str=os.getenv('POSTGRES_USER')
    password: str=os.getenv('POSTGRES_PASSWORD')
    port: int=int(os.getenv('POSTGRES_PORT'))
    host: str=os.getenv('POSTGRES_HOST')

    @property
    def connection_kwargs(self):
        return dict(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port,
            host=self.host,
            )

    @property
    def connection(self):
        return psycopg2.connect(**self.connection_kwargs)
