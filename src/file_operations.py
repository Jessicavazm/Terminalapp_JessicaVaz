import json
import os

from colorama import Fore, Back, Style, init 

# Function adds notes to json file
def save_notes_json(notes, filename="notes.json"):
    
    try:
        with open(filename, "w") as file:
            json.dump(notes, file)
            print(f"{Fore.GREEN}Changes have been saved to file. {filename}")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")

# 'If' and 'os' checks if file exists and loads user's notes from json file.
def load_notes_json(filename="notes.json"):
    
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                notes = json.load(file)
                return notes 
        
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
    else:
        print(f"{Fore.YELLOW}File {filename} does not exist.")