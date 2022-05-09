from initialize_database import connection
from execute_query import execute_query

pop_books = """
INSERT INTO books VALUES
(1, 'Harry Potter', 'JK' , '2000-01-01' , 'Fiction'),
(2, 'The Great Gatsby', 'F. Scott Fitzgerald' , '1999-01-01' , 'Fiction'),
(3, 'War and Peace', 'Leo Tolstoy' , '1967-01-01' , 'Fiction');
"""
##execute_query(connection, pop_books)

pop_members = """
INSERT INTO member VALUES
(1, 'Elysia', 3),
(2, 'Ethan', 2),
(3, 'Dave', 2),
(4, 'Sejal', 2);
"""

##execute_query(connection, pop_members)

pop_author = """
INSERT INTO author VALUES
(1, 'JK'),
(2, 'Leo Tolstoy'),
(3, 'F. Scott Fitzgerald');

"""

execute_query(connection, pop_author)

