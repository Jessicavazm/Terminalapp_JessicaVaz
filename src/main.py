from app_functions import add_note, edit_note, remove_note, view_notes, notes
import datetime
BLUE = "\033[34m"
RESET = "\033[0m"

def main():
    while True:
        print(f"""
            {BLUE}Welcome to your very own note-taking app!!{RESET}
            Every note is printed along an index number used to edit or delete notes.
        
            1. Add a Note
            2. Edit a Note
            3. Remove a Note
            4. View Notes
            5. Exit
            """)
        try:
            user_choice = input("Kindly select a number (1-5) to proceed: ")

            if user_choice == "1":
                add_note()
            elif user_choice == "2":
                edit_note()
            elif user_choice == "3":
                remove_note()
            elif user_choice == "4":
                view_notes()
            elif user_choice == "5":
                print("Exiting the program in 3,2,1...")
                break
            else:
                print("Invalid input, please choose an option from 1 to 5")
        except KeyboardInterrupt:
            print("Program interrupted by user, exiting in 3,2,1..")
        except Exception as e:
            print(f"Unexpected error occurred {e}")

if __name__ == "__main__":
    main()

