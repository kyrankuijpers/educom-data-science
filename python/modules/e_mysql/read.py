# -*- coding: utf-8 -*-
import sys
import mysql.connector 
from typing import List

sys.path.append("C:\\xampp\\htdocs\\educom-data-science\\python\\modules")

from e_class import person as p

def get_connection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python"
    )
    return db_connection

def get_data_as_object_list(db_connection, table) -> List[object]:
    # Door buffered=True kunnen we door de resultaten heen loopen zonder eerst de hele resultatenset op te halen via db_cursor.fetchall()
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    query = "SELECT * FROM % s" % table
    db_cursor.execute(query)
    objects = []

    for row in db_cursor:
        # omdat de kolomnamen van de resultaten identiek zijn aan de namen van de constructor parameters van de Person class
        # kunnen we de row dict uitpakken en als argument meegeven aan de Person constructor. 
        new_instance = p.Person(**row)
        objects.append(new_instance)

    db_cursor.close()
    
    return objects

def read_all_from_table(db_connection, table) -> List[dict]:
    # Door buffered=True kunnen we door de resultaten heen loopen zonder eerst de hele resultatenset op te halen via db_cursor.fetchall()
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    
    query = f"SELECT * FROM `{table}`"
    
    db_cursor.execute(query)      
    results = [row for row in db_cursor]
    db_cursor.close()
    
    return results

def main():
    
    db_connection = get_connection()
    objects = get_data_as_object_list(db_connection, "person")
    dicts = read_all_from_table(get_connection(), "person")
    
    return

if __name__ == "__main__":
    main()


