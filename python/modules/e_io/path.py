import sys

def get_path() -> str:
    try:
        return sys.argv[1]
    except Exception as e:
        print("Error, could not get path:", e)
        return ''

