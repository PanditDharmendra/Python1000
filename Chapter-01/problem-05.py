import os

def list_directory_contents(path='.'):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
path_to_list = '/python'

# Example usage with a specified path
list_directory_contents(path_to_list)
# Example using with the current directory
list_directory_contents('.')