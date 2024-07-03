import datetime
import json
import os

notes = []

def save_notes_json(filename = "notes.json"):
    with open(filename, "w") as file:
        json.dump(notes, file)

def load_notes_json(filename = "notes.json"):
    global notes
    if os.path.exists(filename):
        with open (filename, "r") as file:
            notes = json.load(file)

def add_note():
    global notes
    try: 
        note_text = input("Type your note to be added to the note-taking app: ")
        if not note_text.strip():
            raise ValueError ("Note cannot be empty, please type a text")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        note = (note_text, timestamp)
        notes.append(note)
        print("Your note has been successfully added")
        save_notes_json()
        view_notes()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

def edit_note():
    global notes
    view_notes()
    if notes:
        try:
            i = int(input("Please, enter the note index you would like to edit: "))
            if i >= 1 and i <= len(notes):
                new_note = input("Type your new note: ")
                notes[i - 1] = (new_note, datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                print("Note has been successfully edited")
                save_notes_json()
            else: 
                print("Incorrect index, try again")
        except ValueError:
            print("Type a valid number from 1 to 5 options.")
    else:
        print("You don't have any notes to edit, try adding a note first")

def remove_note():
    global notes
    view_notes()
    if notes:
        try:
            i = int(input("Please, enter the note index you would like to remove: "))
            if i >= 1 and i <= len(notes):
                notes.pop(i - 1)
                print("Note removed successfully")
                save_notes_json()
            else:
                print("An error occurred, try again")
        except ValueError:
            print("Type a valid number from 1 to 5 options.")       
    else:
        print("You don't have any notes to delete, try adding a note first")
        
def view_notes():
    global notes
    if notes:
        print("List of notes: ")
        for i,(note_text, timestamp) in enumerate(notes, start=1):
            print(f"{i}.{note_text} (Created at: {timestamp})")
    else:
        print("No notes to display.")