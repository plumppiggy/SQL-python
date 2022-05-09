import mysql.connector
from mysql.connector import Error
import pandas as pd
from execute_query import execute_query
from initialize_database import connection

create_book_table = """
CREATE TABLE books (
    book_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    author VARCHAR(40) NOT NULL,
    dor DATE,
    category VARCHAR(40) NOT NULL
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
execute_query(connection, create_author_table)
execute_query(connection, create_member_table)
execute_query(connection, create_current_loan_table)
execute_query(connection, create_history_table)
execute_query(connection, create_book_table)