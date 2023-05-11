from os import system
import pymssql

settings = open('settings.txt', 'r', encoding='utf8')

system_params = [param[param.index('=')+1:].rstrip('\n') for param in settings.readlines()]
host,database,username,password,TABLE_ONE,TABLE_TWO = system_params

def connect_database():
    conn = pymssql.connect(server=host, user=username, password=password, database=database)
    cursor = conn.cursor()
    return cursor,conn

def close_connection(cursor,conn):
    cursor.close()
    conn.close()

def execute_sql(query):
    try: 
        cursor,conn = connect_database()
        cursor.execute(query)
        row_affected = cursor.rowcount
        conn.commit()
        return {"status": 0 , "message": row_affected}
    except Exception as error:
        return {"status":-1 , "message": str(error)}
    finally:
        close_connection(cursor,conn)