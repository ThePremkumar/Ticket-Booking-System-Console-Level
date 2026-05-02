import sqlite3

def sql_executor(query, params=None, fetch=False):
    sqliteConnection = None
    
    try:
        sqliteConnection = sqlite3.connect('movie_booking.db')
        cursor = sqliteConnection.cursor()
        print("DB Init")


        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        sqliteConnection.commit()

        # for SELECT queries
        if fetch:
            return cursor.fetchall()

    except Exception as error:
        print('Error occurred -', error)

    finally:
        # Ensure the database connection is closed
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

# sql_executor('SELECT sqlite_version();')

if __name__ == "__main__":
    # This only runs when YOU run database.py directly
    result = sql_executor('SELECT sqlite_version();', fetch=True)
    print(result)