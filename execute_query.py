import mysql.connector
from mysql.connector import Error
import pandas as pd

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query Succesful')
    except Error as err:
        print(f'Error: {err}')