import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from sqlalchemy import create_engine

from config_db import DATABASE_NAME, DATABASE_URL
from models import Base


def main():
    try:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
    except Exception:
        connection = psycopg2.connect(user='postgres', password='12345', host='localhost')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()
        cursor.execute(f'create database {DATABASE_NAME}')

        cursor.close()
        connection.close()
    finally:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
