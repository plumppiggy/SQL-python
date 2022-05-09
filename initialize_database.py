import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_db_connection(host_name, user_name, user_password, db_name):
    ## close any exisiting connections
    connection = None

    try:
        connection = mysql.connector.connect(
            host=host_name, 
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('My SQL data base connection successful')
    except Error as err:
        print(f'Error: {err}')

    ## return a connection object
    return connection

pw = "Coding76!" ## password for root user
db = "Library" ## database name

connection = create_db_connection("localhost", "root", pw, db)
