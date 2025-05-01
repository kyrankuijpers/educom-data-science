from typing import List
from e_class.person2.model import Person
from e_mysql.connect import get_connection
import e_mysql.create_or_update as cu
import e_mysql.read as read
  
def read_persons(db_connection) -> List[Person]:

    results = []
    persons = []    
    results = read.read_all_from_table(db_connection, "person")

    for row in results:
        # omdat de kolomnamen van de resultaten identiek zijn aan de namen van de constructor parameters van de Person class
        # kunnen we de row dict uitpakken en als argument meegeven aan de Person constructor. 
        new_instance = Person(**row)
        persons.append(new_instance)
    
    return persons
    
def show_persons(persons: List[Person]):
    
    if not persons:
        print("No persons in list")
    else:
        for person in persons:
            print(person.__dict__)
    
    return

def create_person(db_connection, name: str, age: int, city: str):
  
    if(isinstance(name, str) and isinstance(age, int) and isinstance(city, str)):
        person = Person(name, age, city)          
        cu.insert_object_to_db(person, db_connection)
        
    else:
        result = "Error: one or more arguments have invalid type"
        
    return result

def update_person(db_connection, name: str, age: int, city: str, object_id: int):
    
    if(isinstance(name, str) and isinstance(age, int) 
       and isinstance(city, str) and isinstance(object_id, int)):
    
        person = Person(name, age, city, object_id)          
        cu.update_object_by_id(person, db_connection)
        
    else:
        result = "Error: one or more arguments have invalid type"
        
    return result

def delete_person(db_connection, object_id: int):
    
    db_cursor = db_connection.cursor()
    
    query = "DELETE FROM person WHERE id=%s"
    values = (object_id, )
    
    db_cursor.execute(query, values)
    db_connection.commit()
    affected_rows = db_cursor.rowcount
    
    db_cursor.close()
    
    if(affected_rows > 0):
        result = f"Success: deleted {affected_rows} rows"
    else:
        result = "Exception: no rows affected during deletion"
    
    return result
    
def main():
    
    db_connection = get_connection()
    #show_persons(read_persons(db_connection))
    #create_person(db_connection, 'billie', 5, 'vb'))
    #update_person(db_connection, 'billie', 5, 'vbb', '1')
    #delete_person(db_connection, 1)
    
    return

if __name__ == "__main__":
    main()
    
    

