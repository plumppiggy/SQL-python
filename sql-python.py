from cmath import exp
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

pw = "Coding76!"
db = "Library"

connection = create_db_connection("localhost", "root", pw, db)

# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print('Database created successfully')
#     except Error as err:
#         print(f'Error {err}')

# create_database_query = 'CREATE DATABASE library'
# create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query Succesful')
    except Error as err:
        print(f'Error: {err}')

create_book_table = """
CREATE TABLE books (
    book_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    author VARCHAR(40) NOT NULL,
    dor DATE,
    category VARCHAR(40) NOT NULL,
);
"""

create_author_table = """
CREATE TABLE author (
    author_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(40) NOT NULL
);
"""

create_member_table = """
CREATE TABLE member (
    member_id INT NOT NULL PRIMARY KEY,
    name VARCHAR(40),
    limit_ INT
);
"""

create_current_loan_table = """
CREATE TABLE currentLoan (
    member_id INT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    loan_date DATE,
    due_date DATE
);
"""

create_history_table = """
CREATE TABLE history (
    member_id INT NOT NULL PRIMARY KEY,
    book_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE
);
"""
##execute_query(connection, create_author_table)
##execute_query(connection, create_member_table)
##execute_query(connection, create_current_loan_table)
##execute_query(connection, create_history_table)

execute_query(connection, '')
execute_query(connection, create_book_table)


pop_books = """
INSERT INTO books VALUES
(1, 'Harry Potter', 'JK' , '2000-01-01' , 1),
(2, 'The Great Gatsby', 'F. Scott Fitzgerald' , '1999-01-01' , 1),
(3, 'War and Peace', 'Leo Tolstoy' , '1967-01-01' , 1)
"""
execute_query(connection, pop_books)

