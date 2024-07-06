# Import Datetime to display date and time notes were created
import datetime

# Import Colorama package to use colours
from colorama import Fore, Back, Style, init 

# Import file_operations module to use it's functions
import file_operations as fo

# Initializes and automatically resets text colours
init(autoreset=True)

# Initialise the list
notes = []

# Function asks for user notes(input) and adds notes to json file. 
def add_note():
    notes = fo.load_notes_json()
    initial_count = len(notes)

    try:
        print(f"{Fore.GREEN}Enter each note on a new line. Type 'done' to finish or 'exit' to cancel: ")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        
        while True:
            note_text = input()
            if note_text.lower().strip() == 'done':
                break
            elif note_text.lower().strip() == "exit":
                break
            if not note_text.strip():
                print(f"{Fore.YELLOW}Note cannot be empty. Enter each note on a new line. Type 'done' to finish or 'exit' to cancel: ")
                continue
            notes.append((note_text.strip(), timestamp))
        
        if len(notes) > initial_count:
            print(f"{Fore.GREEN}Notes have been added successfully.")
            fo.save_notes_json(notes)
            view_notes()
        else:
            print(f"{Fore.YELLOW}No notes were added.")
    
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")


# Function gives the users access to edit notes using index number and prompts users to first add a note in case they haven't added any notes yet. Error handling catches ValueErrors and any possible errors.
def edit_note():
    notes = fo.load_notes_json()
    
    if not notes:
        print(f"{Fore.YELLOW}You don't have any notes to edit, try adding a note first.")
        return

    view_notes()

    try:
        while True:
            i = input(f"Please, type the note index you would like to edit or type 'exit' to cancel: ").strip()
            if i.lower() == "exit":
                break
            try:
                i = int(i)
                if 1 <= i <= len(notes):
                    new_note = input("Type your new note and press enter to save: ").strip()
                    if new_note:
                        notes[i - 1] = (new_note, datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                        print(f"{Fore.GREEN}Note has been successfully edited.")
                        fo.save_notes_json(notes)
                        view_notes()
                    else:
                        print(f"{Fore.RED}Note cannot be empty.")
                    break
                else:
                    print(f"{Fore.RED}Incorrect index. Please try again.")
            except ValueError:
                print(f"{Fore.RED}Invalid input, type a valid number from (1-{len(notes)}).")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")

 

# Function gives the users access to remove notes using index number and prompts users to first add a note in case they haven't added any notes yet. Error handling catches ValueError and any possible errors.
def remove_note():
    notes = fo.load_notes_json()
    
    if not notes:
        print(f"{Fore.YELLOW}You don't have any notes to remove, try adding a note first.")
        return

    view_notes()

    try:
        while True:
            i = input("Please, type the note index you would like to remove or type 'exit' to cancel: ").strip()
            if i.lower() == "exit":
                break
            try:
                i = int(i)
                if 1 <= i <= len(notes):
                    notes.pop(i - 1)
                    print(f"{Fore.GREEN}Note has been successfully removed.")
                    fo.save_notes_json(notes)
                    view_notes()
                    break
                else:
                    print(f"{Fore.RED}Incorrect index. Please try again.")
            except ValueError:
                print(f"{Fore.RED}Invalid input, type a valid number from (1-{len(notes)}).")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")



def clear_notes():
    notes = fo.load_notes_json()
    
    if not notes:
        print(f"{Fore.YELLOW}Your notebook is empty, try adding a note first.")
        return

    try:
        notes.clear()
        print(f"{Fore.GREEN}All notes have been cleared.")
        fo.save_notes_json(notes)
        
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")
    

# Function allows users to view notes if any and prompts user to add notes if they haven't added any note. Error handling catches any possible errors.
def view_notes():
    notes = fo.load_notes_json()
    
    if not notes:
        print(f"{Fore.YELLOW}You don't have any notes to view, try adding a note first.")
        return

    try:
        print(Back.YELLOW + Fore.RED + "List of notes:" + Style.RESET_ALL)
        for i,(note_text, timestamp) in enumerate(notes,start=1):
            print(f"{Fore.YELLOW}{i}{Fore.RESET}. {note_text} (Created at: {timestamp})")
        
    except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")