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

def update_object_by_id(instance: object, db_connection):

    db_cursor = db_connection.cursor()
    
    class_name = type(instance).__name__
    table_name = class_name.lower()

    if instance.id:

        values = list(instance.__dict__.values())   
        keys_and_placeholders = []
        set_string = ""
        keys = instance.__dict__.keys()
        
        for key in keys:
            
            key_and_placeholder = f"{key}=%s"
            keys_and_placeholders.append(key_and_placeholder)
        
        set_string = ", ".join(keys_and_placeholders)

        query = f"UPDATE {table_name} SET {set_string} WHERE id={instance.id};"
        
        db_cursor.execute(query, values)      
        db_connection.commit()               
        affected_rows = db_cursor.rowcount   
        print(affected_rows)
        
        if(affected_rows > 0):
            result = f"Success: updated {affected_rows} number of rows"
        elif(affected_rows == 0):
            result = "Exception: did not update any rows. id may not exist or values may be identical"
        elif(affected_rows == -1):
            result = "Unspecified error with rowcount -1"
        
        db_cursor.close()

    else:        
        result = "Error: need id to update row in database"

    return result 

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
    #file_path = e_io.path.get_path()
    
    #insert_persons_from_json(db_connection, file_path)
    
    #person = p.Person("annie", 11, 'eden', 124)    
    #update_object_by_id(person, db_connection))

    return

if __name__ == "__main__":
    
    main()


