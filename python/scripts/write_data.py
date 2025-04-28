import sys, csv, os
import xml.etree.ElementTree as ElementTree
from json import dump
from typing import List
import person as p

def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return '' 

############################ XML ################################

def write_people_to_xml(file_path: str, persons: List[p.Person]):
    xml_string = get_persons_xml_string(persons)

    try:
        with open(file_path, mode='w') as xml_file:
            xml_file.write(xml_string)

    except OSError as e:
        print('Failed to write to XML file: ', e)


def get_persons_xml_string(persons: List[p.Person]) -> str:
    root_element = ElementTree.Element('ArrayOfPerson')
    for person in persons:
        person_element = add_person_element(person, root_element)
        add_person_children(person, person_element)

    xml_string = ElementTree.tostring(root_element, encoding="unicode", xml_declaration=True)
    return xml_string


def add_person_element(person: p.Person, root_element):
    person_element = ElementTree.SubElement(root_element, 'Person')
    person_element.set("id", str(person.id))
    
    return person_element
    
    
def add_person_children(person: p.Person, person_element):
    name_element = ElementTree.SubElement(person_element, "name")
    age_element = ElementTree.SubElement(person_element, "age")
    city_element = ElementTree.SubElement(person_element, "city")
    
    name_element.text = person.name
    age_element.text = str(person.age)
    city_element.text = person.city

############################ CSV ################################

def write_csv(file_path: str, objects: list[object]) -> bool:

    if len(objects) < 1:
        print('List empty: nothing to write')
        return False

    try:
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            
            first_object = objects[0]
            field_names = first_object.__dict__.keys()
            writer.writerow(field_names)

            for object in objects:
                row = object.__dict__.values()
                writer.writerow(row)
            return True

    except OSError as e:
        print('Failed to write to CSV file: ', e)
    
    return False

############################# JSON ################################

def write_json(file_path: str, items: list) -> bool:
    try:
        with open(file_path, mode='w') as json_file:
            dump(items, json_file)
        return True
    except OSError as e:
        print('Failed to write to json file: ', e)

    return False

def main():
    
    persons = [p.Person(1, "Reese", 51, "Brooklyn"), p.Person(2, "Steve", 49, "Saskatchewan")]
    
    file_path = get_path()
    
    file_ext = os.path.splitext(file_path)[1]
    
    if(file_ext == ".xml"):
        
        write_people_to_xml(file_path, persons)       
        
    elif(file_ext == ".json"):
        
        serialized = []
        
        for person in persons:
            serialized.append(person.to_dict())
        
        write_json(file_path, serialized)
        
    elif(file_ext == ".csv"):
    
        write_csv(file_path, persons) 
        
    else:
        
        print("failed to write to file with extension % s" % file_ext)
    
    return 

##############################

if __name__ == "__main__":
    main()
    

