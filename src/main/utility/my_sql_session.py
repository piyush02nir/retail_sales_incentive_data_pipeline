import mysql.connector
from resources.dev import config


def get_mysql_connection():
    connection = mysql.connector.connect(
        host= config.host,
        user= config.user,
        password= config.password,
        database= config.database_name
    )
    return connection


# connection = mysql.connector.connect(
#     host=config.host,
#     user=config.user,
#     password=config.password,
#     database=config.database_name
# )
#
# # Check if the connection is successful
# if connection.is_connected():
#     print("Connected to MySQL database")

# cursor = connection.cursor()
#
# # Execute a SQL query
# query = "SELECT * FROM manish.testing"
# cursor.execute(query)
#
# # Fetch and print the results
# for row in cursor.fetchall():
#     print(row)
#
# # Close the cursor
# cursor.close()
#
# connection.close()
