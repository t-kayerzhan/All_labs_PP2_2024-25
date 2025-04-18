import psycopg2
from config import load_config

def create_table():
    params = load_config()

    create_command = ("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        number BIGINT UNIQUE NOT NULL
    )
    """
    )

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(create_command)
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    create_table()
