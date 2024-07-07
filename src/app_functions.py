# Import Datetime to display date and time notes were created
import datetime

# Import Colorama package to use colours in printing
from colorama import Fore, Back, Style, init 

# Import file_operations module to use it's functions
import file_operations as fo

# Initializes and automatically resets text colours
init(autoreset=True)

# Initialise the list
notes = []

# Function 'add_note' allows users to add notes to note app. Saved notes are stored in a variable called 'notes'. Number of notes are stored in variable called 'initial_count' which will determine if there's a new note to save to note app.
def add_note():
    notes = fo.load_notes_json()
    initial_count = len(notes)
    # Try contains a message on how to add a new note or exit to main menu. Variable 'timestamp' stores current date and time.
    try:
        print(f"{Fore.GREEN}Enter each note on a new line. Type 'done' to finish or 'exit' to cancel: ")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        # Input is stored in variable called 'i'. 'If' condition checks if 'i' value is equal to 'done' or 'exit' which ends the loop. 'If not' checks if note is empty and if it evaluates to true it prompts user to type something or type 'exit' to go back to main menu. 'Else' is only executed if the above are not true, it adds notes to note app with timestamp.
        while True:
            i = input()
            if i.lower().strip() in ['done', 'exit']:
                break
            if not i.strip():
                print(f"{Fore.YELLOW}Note cannot be empty. Enter content for the note. Type 'done' to finish or 'exit' to cancel: ")
                continue
            else:
                notes.append((i.strip(), timestamp))
        # 'If' checks if new notes were added, if so it prints a confirmation message, save and displays notes. 'Else' is executed if no notes were added to app.
        if len(notes) > initial_count:
            fo.save_notes_json(notes)
            print(f"{Fore.GREEN}Notes have been added successfully.")
            view_notes()
        else:
            print(f"{Fore.YELLOW}No notes were added.")
    # except covers 'ValueError' and any other possible errors it might occur in the program execution.
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")


# Function 'edit_notes' allows users to edit a note using an index number. Existing notes are stored in variable 'notes'.
def edit_note():
    notes = fo.load_notes_json()
    # 'If not' first checks if note app is empty, if so it prompts the user to add a note first. 'Return' ends the function since there's no notes to edit.
    if not notes:
        print(f"{Fore.YELLOW}You don't have any notes to edit, try adding a note first.")
        return
    # Function 'view_'notes is called displaying all saved notes.
    view_notes()
    # Loop 'while True' runs until user types a valid input or chooses to exit program.
    
    while True:
        i = input(f"{Fore.GREEN}Please, type the note index you would like to edit or type 'exit' to cancel: ").strip()
        if i.lower() == "exit":
            break

        # User input is converted to int. 'If' checks if input is within the range. If condition evaluates to true, it proceeds to ask user to type new note content which is stored in variable new_note. 'If new_note' updates the note with timestamp and displays a confirmation message. Function 'save_notes_json' updates json file and 'view_notes' displays updated notes to user. 'Else' keeps the loops running and prompts user to type a non empty note. 'ValueError' catches wrong input values and 'Exception' catches any other possible error that might occur.
        try:
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            i = int(i)
            if i >= 1 and i <= len(notes):
                new_note = input(f"{Fore.GREEN}Type your new note and press enter to save: ").strip()
                if new_note:
                    notes[i - 1] = (new_note.strip(), timestamp)
                    fo.save_notes_json(notes)
                    print(f"{Fore.GREEN}Note has been successfully edited.")
                    fo.save_notes_json(notes)
                    view_notes()
                    break

                else:
                    print(f"{Fore.YELLOW}Note cannot be empty. Please enter content for the note when selecting an index to edit.")
                    continue
                    
            else:
                print(f"{Fore.RED}Incorrect index. Please try again.")
        except ValueError:
                print(f"{Fore.RED}Invalid input, type a valid number from (1-{len(notes)}).")

        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
    


# Function 'remove_note' allows users to delete a specific note using it's index number. First, saved notes are stored in variable called 'notes'. 'If not' condition checks if note app is empty, if it evaluates to true, it prompts the user to add a note first. 'Return' ends the function since note app is empty and it can't proceed to remove a note.
def remove_note():
    notes = fo.load_notes_json()
    
    if not notes:
        print(f"{Fore.YELLOW}You don't have any notes to remove, try adding a note first.")
        return
    # Function 'view_notes' displays saved notes to users
    view_notes()
    # Loop 'while True' keeps running until user's input is valid or user decides to exit. User input is converted to 'int' and input is within the range, 'pop' function deletes note and prints a confirmation message. Function 'save_notes' makes new changes to json file and function view_notes displays updated note list. 'Else' statement is executed if user input is out of the valid range. 'ValueErrors' catches wrong input values and 'Exception' catches any other possible error that might occur in the process.
    try:
        while True:
            i = input(f"{Fore.GREEN}Please, type the note index you would like to remove or type 'exit' to cancel: ").strip()
            if i.lower() == "exit":
                break
            try:
                i = int(i)
                if i >= 1 and i <= len(notes):
                    notes.pop(i - 1)
                    fo.save_notes_json(notes)
                    print(f"{Fore.GREEN}Note has been successfully removed.")
                    view_notes()
                    break
                else:
                    print(f"{Fore.RED}Incorrect index, please double check index next to note.")
            except ValueError:
                print(f"{Fore.RED}Invalid input, type a valid number from (1-{len(notes)}).")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")


# Function clear_notes allows users to delete all notes at once. Saved notes are stored in variable 'notes'. 'If not' first checks if note app is empty, if it evaluates to true, it prompts the user to add a note first. User input is stored in variable 'i'. Loop 'while True' runs until user confirms they want to go ahead with function or chooses cancel and go back to main menu. 'Else' statement is printed if user types invalid input when asked if they want to proceed. 'Exception' catches any errors that might occur in process execution.
def clear_notes():
    notes = fo.load_notes_json()

    if not notes:
        print(f"{Fore.YELLOW}Your notebook is empty, try adding a note first.")
        return

    while True:
        i = input(f"{Fore.RED}Are you sure you want to delete all notes? This action cannot be undone. Type 'yes' to confirm or 'no' to cancel: ").strip().lower()

        try:
            if i == "yes":
                notes.clear()
                fo.save_notes_json(notes)
                print(f"{Fore.GREEN}All notes have been cleared.")
                return  
            elif i == "no":
                print(f"{Fore.GREEN}No action has been done. Exiting to main menu...")
                return  
            else:
                print(f"{Fore.YELLOW}Invalid option, please try again.")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
    

# Function 'view_notes 'allows users to view saved notes. 'If not' first checks if note app is empty, if it evaluates to true, it prompts users to first add a note. 'Try' block prints each item in the list of notes, enumerating notes from 1 instead of default value 0. 'Exception' catches any error that might occur in the process.
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