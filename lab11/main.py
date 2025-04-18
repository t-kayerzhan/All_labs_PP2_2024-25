import psycopg2
from config import load_config

# 1. Pattern search functions
def pattern_by_name():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE FUNCTION search_users(pattern TEXT)
                    RETURNS TABLE(name VARCHAR, surname VARCHAR, number BIGINT)
                    AS $$
                    BEGIN
                        RETURN QUERY
                        SELECT phonebook.name, phonebook.surname, phonebook.number
                        FROM phonebook
                       WHERE phonebook.name ILIKE pattern || '%';
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()

    except Exception as error:
        print("Error creating search function:", error)

def pattern_by_surname():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE FUNCTION by_surname(pattern TEXT)
                    RETURNS TABLE(name VARCHAR, surname VARCHAR, number BIGINT)
                    AS $$
                    BEGIN
                        RETURN QUERY
                        SELECT phonebook.name, phonebook.surname, phonebook.number
                        FROM phonebook
                        WHERE phonebook.surname ILIKE pattern || '%';
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()
    except Exception as error:
        print("Error creating search function:", error)

def pattern_by_number():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE FUNCTION by_number(pattern TEXT)
                    RETURNS TABLE(name VARCHAR, surname VARCHAR, number BIGINT)
                    AS $$
                    BEGIN
                        RETURN QUERY
                        SELECT phonebook.name, phonebook.surname, phonebook.number
                        FROM phonebook
                        WHERE phonebook.number::TEXT ILIKE pattern || '%';
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()
    except Exception as error:
        print("Error creating search function:", error)

# 2. Create or Update procedure
def create_insert_procedure():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE PROCEDURE insert_or_update(
                        IN p_name TEXT,
                        IN p_surname TEXT,
                        IN p_number BIGINT
                    )
                    AS $$
                    BEGIN
                        IF EXISTS (SELECT 1 FROM phonebook WHERE phonebook.name = p_name) THEN
                            UPDATE phonebook 
                            SET number = p_number, surname = p_surname
                            WHERE phonebook.name = p_name;
                        ELSE
                            INSERT INTO phonebook(name, surname, number) VALUES (p_name, p_surname, p_number);
                        END IF;
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()
    except Exception as error:
        print("Error creating insert procedure:", error)


def insert_user():
    name = input("Name: ")
    surname = input("Surname: ")
    number = int(input("Number: "))

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_or_update(%s, %s, %s)", (name, surname, number))
                conn.commit()
                print("User inserted or updated.")
    except Exception as error:
        print("Error inserting user:", error)

# 3. Inserting many users
def inserting_users():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE PROCEDURE inserting_users(
                        IN name TEXT[], 
                        IN surname TEXT[], 
                        IN number BIGINT[], 
                        INOUT invalid_data TEXT[]
                    )
                    AS $$
                    DECLARE
                        i INT := 1;
                        bad_list TEXT[] := '{}';
                    BEGIN 
                        WHILE i <= array_length(name, 1) LOOP
                            IF number[i]::TEXT ~ '^\\d{10}$' THEN
                                CALL insert_or_update(name[i], surname[i], number[i]);
                            ELSE
                                bad_list := array_append(bad_list, name[i] || ' - ' || number[i]);
                            END IF;
                            i := i + 1;
                        END LOOP;
                        invalid_data := bad_list;  
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()

                c = int(input("How many users do you want to add?: "))
                Names = []
                Surnames = []
                Numbers = []
                for i in range(c):
                    a = input("Enter name: ")
                    b = input("Enter surname: ")
                    c = input("Enter number: ")
                    Names.append(a)
                    Surnames.append(b)
                    Numbers.append(int(c))

                invalid_data = []
                cur.execute("CALL inserting_users(%s, %s, %s, %s)", (Names, Surnames, Numbers, invalid_data))
                conn.commit()
                print("Invalid data:", invalid_data)

    except Exception as error:
        print("Error inserting multiple users:", error)

# 4. Pagination
def pagination():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE FUNCTION get_paginated_users(p_limit INT, p_offset INT)
                    RETURNS TABLE(id INT, name VARCHAR, surname VARCHAR, number BIGINT)
                    AS $$
                    BEGIN
                        RETURN QUERY
                        SELECT p.id, p.name, p.surname, p.number
                        FROM phonebook p
                        ORDER BY p.id
                        LIMIT p_limit OFFSET p_offset;
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()
                cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as error:
        print("Error in pagination:", error)

# 5. Deleting user by name or number
def delete_by_name():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE PROCEDURE delete_by_name(
                        IN p_name TEXT
                    )
                    AS $$
                    BEGIN
                        IF EXISTS (SELECT 1 FROM phonebook WHERE phonebook.name = p_name) THEN
                            DELETE FROM phonebook 
                            WHERE phonebook.name = p_name;
                        END IF;
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()

                user_name = input("Enter name to delete: ")
                cur.execute("CALL delete_by_name(%s)", (user_name,))
                conn.commit()
                print("User deleted if found.")
    except Exception as error:
        print("Error deleting user:", error)

def delete_by_number():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE OR REPLACE PROCEDURE delete_by_number(
                        IN p_number BIGINT)
                    AS $$
                    BEGIN
                        IF EXISTS (SELECT 1 FROM phonebook WHERE phonebook.number = p_number) THEN
                            DELETE FROM phonebook 
                            WHERE phonebook.number = p_number;
                        END IF;
                    END;
                    $$ LANGUAGE plpgsql;
                """)
                conn.commit()

                user_number = int(input("Enter number to delete: "))
                cur.execute("CALL delete_by_number(%s)", (user_number,))
                conn.commit()
                print("User deleted if found.")
    except Exception as error:
        print("Error deleting user:", error)

if __name__ == '__main__':
    pattern_by_name()
    pattern_by_number()
    pattern_by_surname()
    create_insert_procedure()

    while True:
        print("\nOptions:")
        print("1. Search by pattern")
        print("2. Insert or update user")
        print("3. Insert many users")
        print("4. Pagination")
        print("5. Delete user")
        print("0. Exit")
        choice = input("Select option: ")

        if choice == '1':
            opt = input("By pattern (name/surname/number): ")
            pattern = input("Enter pattern: ")
            if opt == 'name':
                config = load_config()
                with psycopg2.connect(**config) as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT * FROM search_users(%s)", (pattern,))
                        for row in cur.fetchall():
                            print(row)
            elif opt == 'surname':
                config = load_config()
                with psycopg2.connect(**config) as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT * FROM by_surname(%s)", (pattern,))
                        for row in cur.fetchall():
                            print(row)
            elif opt == 'number':
                config = load_config()
                with psycopg2.connect(**config) as conn:
                    with conn.cursor() as cur:
                        cur.execute("SELECT * FROM by_number(%s)", (pattern,))
                        for row in cur.fetchall():
                            print(row)
        elif choice == '2':
            insert_user()
        elif choice == '3':
            inserting_users()
        elif choice == '4':
            pagination()
        elif choice == '5':
            c = input("How do you wanna delete? (By name/number): ")
            if c == 'name':
                delete_by_name()
            elif c == 'number':
                delete_by_number()
        elif choice == '0':
            break
        else:
            print("Invalid option.")
