# Import colorama to print in colours
from colorama import Fore, Back, Style, init 
# Import Datetime to display date and time notes were created
import datetime
# Import json and os for file handling and file storage.
import json
import os

# Initializes and automatically resets text colours
init(autoreset=True)

# Initialise the list
notes = []

# Function adds user notes to json file
def save_notes_json(filename="notes.json"):
    try:
        with open(filename, "w") as file:
            json.dump(notes, file)
    except Exception as e:
        print(f"{Fore.RED} An unexpected error occurred: {e}")

# 'If' and 'os' checks if file exists and loads user's notes from json file.
def load_notes_json(filename="notes.json"):
    global notes
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                notes = json.load(file)
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
    else:
        print(f"{Fore.YELLOW}File {filename} does not exist.")

# Function asks for user notes(input) and adds notes to json file. 
def add_note():
    global notes
    try:
        print(f"{Fore.GREEN}Type your notes. Enter each note on a new line. Type 'done' on a new line to finish:")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        while True:
            note_text = input()
            if note_text.lower().strip() == 'done':
                break
            if not note_text.strip():
                print(f"{Fore.YELLOW}Note cannot be empty. Enter your note or type 'done' to finish.")
                continue
            notes.append((note_text.strip(), timestamp))
        if len(notes) == 0:
            raise ValueError(f"{Fore.RED}Please add at least one note.")
        print(f"{Fore.GREEN}Notes have been added successfully.")
        save_notes_json()
        view_notes()
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")

# Function gives the users access to edit notes using index number and prompts users to first add a note in case they haven't added any notes yet. Error handling catches ValueErrors and any possible errors.
def edit_note():
    global notes
    if notes:
        view_notes()
        try:
            i = int(input("Please, enter the note index you would like to edit: "))
            if i >= 1 and i <= len(notes):
                new_note = input("Type your new note: ")
                notes[i - 1] = (new_note, datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                print(f"{Fore.GREEN}Note has been successfully edited.")
                save_notes_json()
            else: 
                print(f"{Fore.RED}Incorrect index. Please try again.")
        except ValueError:
            print(f"{Fore.RED}Please, type a valid number from (1-{len(notes)}).")
            
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
    else:
        print(f"{Fore.YELLOW}You don't have any notes to edit, try adding a note first.")

# Function gives the users access to remove notes using index number and prompts users to first add a note in case they haven't added any notes yet. Error handling catches ValueError and any possible errors.
def remove_note():
    global notes
    if notes:
        view_notes()
        try:
            i = int(input("Please, enter the note index you would like to remove: "))
            if i >= 1 and i <= len(notes):
                notes.pop(i - 1)
                print(f"{Fore.GREEN}Note removed successfully.")
                save_notes_json()
            else:
                print(f"{Fore.RED}Incorrect index. Please try again.")
        except ValueError:
            print(f"{Fore.RED}Please, type a valid number from (1-{len(notes)}).")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")       
    else:
        print(f"{Fore.YELLOW}You don't have any notes to delete, try adding a note first.")

# Function allows users to view notes if any and prompts user to add notes if they haven't added any note. Error handling catches any possible errors.
def view_notes():
    global notes
    try:
        if notes:
            print(Back.YELLOW + Fore.RED + "List of notes:" + Style.RESET_ALL)
            for i,(note_text, timestamp) in enumerate(notes, start=1):
                print(f"{i}. {Fore.BLUE}{note_text} (Created at: {timestamp})")
        else:
            print(f"{Fore.YELLOW}You don't have any notes to view, try adding a note first.")
    except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")