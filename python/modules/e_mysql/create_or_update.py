# -*- coding: utf-8 -*-
import sys
import mysql.connector 
from typing import List

sys.path.append("C:\\xampp\\htdocs\\educom-data-science\\python\\modules")

import e_io
from e_mysql.connect import get_connection
from e_class import person as p

def add_or_update_person_to_db(person: p.Person, db_connection) -> p.Person:

    db_cursor = db_connection.cursor()
    
    if person.id:
        query = "UPDATE person SET name=%s, age=%s, city=%s WHERE id=%s"
        values = [person.name, person.age, person.city, person.id]
    else:
        query = "INSERT INTO %s (name, age, city) VALUES (%s, %s, %s)"
        values = [person.name, person.age, person.city]

    db_cursor.execute(query, values)      
    db_connection.commit()       
    affected_rows = db_cursor.rowcount     
    db_cursor.close()

    return affected_rows

def insert_object_to_db(instance: object, db_connection) -> object:

    db_cursor = db_connection.cursor()
    
    class_name = type(instance).__name__
    table_name = class_name.lower()

    instance_dict = instance.__dict__
    instance_keys = instance_dict.keys()
    instance_values = list(instance_dict.values())

    #Remove the id key     
    item_index = 0
    has_id = False

    for item in instance_dict.items():
        if item[0] == "id":
            id_index = item_index
            has_id = True
            break
        else:
            item_index += 1

    keys = [key for key in instance_keys if key != "id"]
    
    #Remove the id value
    values = []
    
    if has_id:
        for i in range(len(instance_values)):
            if i != id_index:
                values.append(instance_values[i])        
    else:
        values = instance_values        

    key_string = ", ".join(keys)
    placeholders = ", ".join(["%s" for value in values])
    
    query = f"INSERT INTO {table_name} ({key_string}) VALUES ({placeholders});"
    db_cursor.execute(query, values)      
    db_connection.commit()       
    affected_rows = db_cursor.rowcount     
    db_cursor.close()

    return affected_rows

def insert_persons_from_json(db_connection, file_path):
    
    persons_dict = e_io.read_data.read_file(file_path)
    
    db_cursor = db_connection.cursor()    
    
    query = "INSERT INTO person (name, age, city) VALUES (%(name)s, %(age)s, %(city)s)"
    values = persons_dict
    
    db_cursor.executemany(query, values)      
    db_connection.commit()       
    affected_rows = db_cursor.rowcount     
    db_cursor.close()

    return affected_rows


def main():
    
    db_connection = get_connection()
    file_path = e_io.path.get_path()
    
    person = p.Person("annie", 11, 'ede', 101)    
    affected_rows = insert_object_to_db(person, db_connection)

    return

if __name__ == "__main__":
    
    main()


