# Import json and os for file handling.
import json
import os

# Import Colorama package to use colours in printing.
from colorama import Fore, init 

# Initializes and automatically resets text colours
init(autoreset=True)

# Function 'save_notes_json' allows functions from 'app_functions' to save new notes and changes to json file. Arguments 'notes' = list of notes to be saved, and 'filename' = path to save the notes. 'With' statement ensure file is always closed. 'W' opens the document in the write mode. 'Dump' saves notes to json file and except catch possible errors with file handling.
def save_notes_json(notes, filename="notes.json"):
    
    try:
        with open(filename, "w") as file:
            json.dump(notes, file)
            print(f"{Fore.GREEN}Changes are being made to {filename}...")
    
    except FileNotFoundError as fe:
        print(f"{Fore.RED}File not found: {fe}")
        
    except IOError as ie:
        print(f"{Fore.RED}IOError: {ie}")

    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")

# Function 'load_notes_json' allows functions in 'main' and 'app_functions' to load saved notes from json file. Argument 'filename' is the path from where to load the notes from. ' If' os.path.exist checks if 'notes.json' file exists, if so, 'with open' opens the file in 'r' read mode. Function json.load loads file into a variable called 'notes' and returns the file. Except handle errors such as FileNotFound, JSONDecodeError and 'exception' catches any other possible errors that might occur in the process. 'Else' prints a message indicating that file not exist.
def load_notes_json(filename="notes.json"):
    
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                notes = json.load(file)
                return notes 
        
        except FileNotFoundError as fe:
            print(f"{Fore.RED}File not found: {fe}")
       
        except json.JSONDecodeError as de:
            print(f"{Fore.RED}JSONDecodeError: {de}")

        except IOError as ie:
            print(f"{Fore.RED}IOError: {ie}")

        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
    else:
        print(f"{Fore.YELLOW}File {filename} does not exist.")