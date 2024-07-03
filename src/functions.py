notes = []
def add_note():
    note = input("Type your note to be added to the note-taking app: ")
    notes.append(note)
    print("Your note has been successfully added.")

def edit_note():
    view_notes()
    if notes:
        i = int(input("Please, enter the note index you would like to edit: "))
        if i >= 1 and i <= len(notes):
            new_note = input("Type your new note: ")
            notes[i - 1] = new_note
            print("Note has been successfully edited.")
        else: 
            print("Incorrect index, try again")
    else:
        print("You don't have any notes to edit, try adding a note first.")

def remove_note():
    view_notes()
    if notes:
        i = int(input("Please, enter the note index you would like to remove: "))
        if i >= 1 and i <= len(notes):
            notes.pop(i - 1)
            print("Note removed successfully.")
        else:
            print("An error occurred, try again")
    else:
        print("You don't have any notes to delete, try adding a note first")
        
def view_notes():
    if notes:
        print("List of notes: ")
        for i,note in enumerate(notes, start=1):
            print(f"{i}.{note}")
    else:
        print("No notes to display.")