from app_functions import add_note, edit_note, remove_note, view_notes, notes

def main_function():
    while True:
        print("""
            Welcome to your very own note-taking app
        
            1. Add a Note
            2. Edit a Note
            3. Remove a Note
            4. View Notes
            5. Exit
            """)

        user_choice = input("Kindly select a number (1-5) to proceed: ")
        
        if user_choice == "1":
            add_note()
        elif user_choice == "2":
            edit_note()
        elif user_choice == "3":
            remove_note
        elif user_choice == "4":
            view_notes()
        elif user_choice == "5":
            print("Exiting the program")
            break
        else:
            print("An error occurred, please try again.")

main_function()