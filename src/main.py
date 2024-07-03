from app_functions import load_notes_json,save_notes_json,add_note, edit_note, remove_note, view_notes, notes
from colorama import Fore, Back, Style, init
import datetime
import json
import os 

init(autoreset=True)

def main():
    load_notes_json()
    while True:
        print(f"""
            {Fore.YELLOW}Welcome to your very own note-taking app!!{Fore.RESET}
            Every note is printed along an index number, date e time.
        
            {Fore.GREEN}1. Add a Note{Fore.RESET}
            {Fore.RED}2. Edit a Note{Fore.RESET}
            {Fore.CYAN}3. Remove a Note{Fore.RESET}
            {Fore.MAGENTA}4. View Notes{Fore.RESET}
            {Fore.BLUE}5. Exit{Fore.RESET}
            """)
        try:
            user_choice = input(f"{Fore.GREEN}Kindly, select a function (1-5) to proceed: {Fore.RESET}")

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
                print(f"{Fore.GREEN}Invalid number, please choose an option from 1 to 5: {Fore.RESET}")
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nProgram interrupted by user, exiting in 3, 2, 1..{Fore.RESET}")
            break
        except Exception as e:
            print(f"{Fore.RED}Unexpected error occurred {e}{Fore.RESET}")

save_notes_json()

if __name__ == "__main__":
    main()

