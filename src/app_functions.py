from colorama import Fore, Back, Style, init
import datetime
import json
import os

init(autoreset=True)

notes = []

def save_notes_json(filename="notes.json"):
    try:
        with open(filename, "w") as file:
            json.dump(notes, file)
    except Exception as e:
        print(f"{Fore.RED}Unexpected error occurred: {e}.{Fore.RESET}")
    finally:
        print(f"{Fore.GREEN}Notes have been processed for saving.{Fore.RESET}")

def load_notes_json(filename="notes.json"):
    global notes
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                notes = json.load(file)
        except Exception as e:
            print(f"{Fore.RED}Unexpected error occurred: {e}.{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}File {filename} does not exist.{Fore.RESET}")

def add_note():
    global notes
    try: 
        note_text = input("Type your note to be added to the note-taking app: ")
        if not note_text.strip():
            raise ValueError (f"{Fore.RED}Note cannot be empty, please type a text.{Fore.RESET}")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        note = (note_text, timestamp)
        notes.append(note)
        print("{Fore.GREEN}Your note has been successfully added.{Fore.RESET}")
        save_notes_json()
        view_notes()
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error occurred: {e}.{Fore.RESET}")

def edit_note():
    global notes
    view_notes()
    if notes:
        try:
            i = int(input("Please, enter the note index you would like to edit: "))
            if i >= 1 and i <= len(notes):
                new_note = input("Type your new note: ")
                notes[i - 1] = (new_note, datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                print(f"{Fore.GREEN}Note has been successfully edited.{Fore.RESET}")
                save_notes_json()
            else: 
                print(f"{Fore.RED}Incorrect index, please try again.The index is displayed next to each note.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please, type a valid number (1-{len(notes)}).{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}You don't have any notes to edit, try adding a note first.{Fore.RED}")

def remove_note():
    global notes
    view_notes()
    if notes:
        try:
            i = int(input("Please, enter the note index you would like to remove: "))
            if i >= 1 and i <= len(notes):
                notes.pop(i - 1)
                print("{Fore.GREEN}Note removed successfully.{Fore.RESET}")
                save_notes_json()
            else:
                print(f"{Fore.RED}An error occurred, try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Type a valid number from 1 to 5 options.{Fore.RESET}")       
    else:
        print(f"{Fore.YELLOW}You don't have any notes to delete, try adding a note first.{Fore.RESET}")

def remove_note():
    global notes
    view_notes()
    if notes:
        try:
            i = int(input("Please, enter the note index you would like to remove: "))
            if i >= 1 and i <= len(notes):
                notes.pop(i - 1)
                print(f"{Fore.GREEN}Note removed successfully.{Fore.RESET}")
                save_notes_json()
            else:
                print(f"{Fore.RED}An error occurred, try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Type a valid number from 1 to {len(notes)} options.{Fore.RESET}")       
    else:
        print(f"{Fore.YELLOW}You don't have any notes to delete, try adding a note first.{Fore.RESET}")
        
def view_notes():
    global notes
    if notes:
        print(Back.YELLOW + Fore.RED + "List of notes:" + Style.RESET_ALL)
        for i,(note_text, timestamp) in enumerate(notes, start=1):
            print(f"{i}. {Fore.BLUE}{note_text} (Created at: {timestamp})")
    else:
        print(f"{Fore.YELLOW}No notes to display.{Fore.RESET}")