import mysql.connector

def get_connection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python"
    )
    return db_connection