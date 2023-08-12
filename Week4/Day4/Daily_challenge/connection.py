import psycopg2

def manage_connection(query, type, values=None):
    connection = None
    try:
        connection = psycopg2.connect(
            database = 'web_API_to_DB',
            user = 'postgres',
            password = '1234',
            host = 'localhost',
            port = '5432'
        )
        with connection:
            with connection.cursor() as cursor:
                if type != 'select':
                    cursor.execute(query, values)
                    connection.commit()
                else:
                    cursor.execute(query)
                    return cursor.fetchall()    
    except Exception as e:
        print(e)
    finally:
        if connection != None:
            connection.close()        
