import sys, os, csv 
import xml.etree.ElementTree as ElementTree
from json import load, JSONDecodeError

sys.path.append("C:\\xampp\\htdocs\\educom-data-science\\python\\modules")

from e_class import person as p

def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''

def read_file(file_path: str) -> list:
    
    file_ext = os.path.splitext(file_path)[1]
    data = []
    
    if(file_ext == ".xml"):
        
        try:            
            elements = ElementTree.parse(file_path)
            root_element = elements.getroot()
            
            for instance in root_element:        
                
                id = instance.get('id')       
                name = instance.find('Name').text
                age = instance.find('Age').text
                city = instance.find('City').text              
                
                my_dict = {"id": id, "name": name, "age": age, "city": city}
                data.append(my_dict)
         
        except ElementTree.ParseError as e:            
            print('Failed to parse XML file: ', e)  
        
    elif(file_ext == ".csv"):
        
        try:
            
            with open(file_path, mode='r') as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                for row in reader:
                    data.append(row) 
                    
        except OSError as e:
            print('Failed to read file: ', e)           
      
    elif(file_ext == ".json"):     
                
        try:
            
            with open(file_path, mode='r') as json_file:
                data = load(json_file) 
                
        except OSError as e:
            print('Failed to read from json file: ', e)
        except JSONDecodeError as e:
            print('Failed to decode json file: ', e)

    return data

def objectify(data: list[dict]) -> list:        

    objects = []    

    for row in data:
        my_object = p.Person(id=row['id'], name=row['name'], age=row['age'], city=row['city'])
        objects.append(my_object)
        
    return objects

def print_objects(objects: list):
    
    for instance in objects:
        print(instance.__dict__) 
    
    return

def main():
    
    path = get_path()
    data = read_file(path)
    objects = objectify(data)
    print_objects(objects)
    

    return
    
if __name__ == "__main__":
    main()
    
    

    

    
