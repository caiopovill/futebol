import os
from dotenv import load_dotenv, find_dotenv
import psycopg2


class DatabaseConnector:

    connection = None

    @classmethod
    def connect(cls):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)

        con_params_local = {
            "DATABASE_HOST":os.environ.get("DATABASE_HOST"),
            'DATABASE_PORT':os.environ.get("DATABASE_PORT"),
            'DATABASE_NAME':os.environ.get("DATABASE_NAME"),
            'DATABASE_USER':os.environ.get("DATABASE_USER"),
            'DATABASE_PASSWORD':os.environ.get("DATABASE_PASSWORD")
        }
        print(con_params_local)
        db_connection = psycopg2.connect(
            host=con_params_local['DATABASE_HOST'],
            port=con_params_local['DATABASE_PORT'],
            dbname=con_params_local['DATABASE_NAME'],
            user=con_params_local['DATABASE_USER'],
            password=con_params_local['DATABASE_PASSWORD']
        )
        cls.connection = db_connection

    