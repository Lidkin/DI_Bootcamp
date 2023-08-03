import psycopg2
# is to manage the database connection
def manage_connection(query, type) :
    connection = None
    try :
        connection = psycopg2.connect(
            database="exercise", #your database name
            user='postgres',
            password='1234',
            host='localhost', #or IP address
            port='5432'
        )
        with connection:
            with connection.cursor() as cursor: #it closes the transaction
                cursor.execute(query)
                if type != "select" :
                    connection.commit()
                else :
                    return cursor.fetchall()
    except Exception as e :
        print(e)
    finally :
        if connection != None:
            connection.close() #need to specificaly closed the connection