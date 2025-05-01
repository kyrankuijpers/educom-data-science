import sys

def get_file_contents(path) -> str:
    try:
        # "with" zorgt ervoor dat het bestand correct wordt afgesloten
        with open(path, mode='r') as file:
            return file.read()
    except OSError as e:
        print('Failed to open file', e)
    except Exception as e:
        print('Error', e)
        
def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''
        
def main():
    path = get_path()
    file_contents = get_file_contents(path)
    print(file_contents)

# dit is de standaard wijze in Python om je main() functie aan te roepen als je een script start
if __name__ == "__main__":
    main()
    