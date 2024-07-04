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
        print(f"{Fore.RED} An unexpected error occurred: {e}{Fore.RESET}")
    finally:
        print(f"{Fore.GREEN}Notes have been processed for saving.{Fore.RESET}")


def load_notes_json(filename="notes.json"):
    global notes
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                notes = json.load(file)
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}File {filename} does not exist.{Fore.RESET}")


def add_note():
    global notes
    try:
        print("Type your notes. Enter each note on a new line. Type 'done' on a new line to finish:")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        while True:
            note_text = input()
            if note_text.lower().strip() == 'done':
                break
            if not note_text.strip():
                print(f"{Fore.YELLOW}Note cannot be empty. Enter your note or type 'done' to finish.{Fore.RESET}")
                continue
            notes.append((note_text.strip(), timestamp))
        if len(notes) == 0:
            raise ValueError(f"{Fore.RED}Please add at least one note.{Fore.RESET}")
        print(f"{Fore.GREEN}Notes added successfully.{Fore.RESET}")
        save_notes_json()
        view_notes()
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")


def edit_note():
    global notes
    if notes:
        view_notes()
        try:
            i = int(input("Please, enter the note index you would like to edit: "))
            if i >= 1 and i <= len(notes):
                new_note = input("Type your new note: ")
                notes[i - 1] = (new_note, datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                print(f"{Fore.GREEN}Note has been successfully edited.{Fore.RESET}")
                save_notes_json()
            else: 
                print(f"{Fore.RED}Incorrect index. Please try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please, type a valid number from (1-{len(notes)}).{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")
    else:
        print(f"{Fore.YELLOW}You don't have any notes to edit, try adding a note first.{Fore.RESET}")


def remove_note():
    global notes
    if notes:
        view_notes()
        try:
            i = int(input("Please, enter the note index you would like to remove: "))
            if i >= 1 and i <= len(notes):
                notes.pop(i - 1)
                print(f"{Fore.GREEN}Note removed successfully.{Fore.RESET}")
                save_notes_json()
            else:
                print(f"{Fore.RED}Incorrect index. Please try again.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Please, type a valid number from (1-{len(notes)}).{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")       
    else:
        print(f"{Fore.YELLOW}You don't have any notes to delete, try adding a note first.{Fore.RESET}")


def view_notes():
    global notes
    try:
        if notes:
            print(Back.YELLOW + Fore.RED + "List of notes:" + Style.RESET_ALL)
            for i,(note_text, timestamp) in enumerate(notes, start=1):
                print(f"{i}. {Fore.BLUE}{note_text} (Created at: {timestamp})")
        else:
            print(f"{Fore.YELLOW}No notes to display, try adding a note first.{Fore.RESET}")
    except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Fore.RESET}")