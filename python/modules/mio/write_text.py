import sys

def write_content(content: str) -> bool:
    path = get_path()
    
    try:
        with open(path, mode='a') as file:
            file.write(content)
            return True
    except OSError as e:
        print('Failed to write to file: ', e)
        return False

def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''

def get_content() -> str:
    try:
        return sys.argv[2]
    except IndexError:
        return ''

def main():
    content = get_content()
    success = write_content(content)
    if success:
        print('Written text to file', get_path())
    else:
        print('Failed to write text to file', get_path())

if __name__ == "__main__":
    main()