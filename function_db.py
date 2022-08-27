import psycopg2

def get_connection():
    try:
        connection=psycopg2.connect(user='postgres',
                                    host='localhost',
                                    password='root',
                                    port='5432',
                                    database='query')
        print(connection.get_dsn_parameters())
    except Exception as e:
        print('Error: ',e)
def execute_read_query(sql_query):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        data = conn.fetchall()
        print(data)
    except Exception as e:
        print('Error: ',e)
    finally:
        cursor.close()
        conn.close()

def execute_write_query(sql_query):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('sql_query')
        conn.commit()
    except Exception as e:
        print('Error: ',e)
    finally:
        cursor.close()
        conn.close()
        
        
        
        
        
        
       # gjyfftf
