# Importing app_function module to use functions
import app_functions as af
# Import colorama for text colour, datetime for displaying date and time for each note, json and os for file handling.
from colorama import Fore, Back, Style, init
import datetime 
import json
import os 

# Initializes and automatically resets text colours
init(autoreset=True)

# Main function displays initial message and function menu. Main function calls functions from app_functions to create and run the app. While loop keeps displaying menu until user decides to exit program, if/elif/else statements controls the flow of the program and try/except handles errors during the execution of the program and avoids program from breaking down. 
def main():
    af.load_notes_json()
    while True:
        print(f"""
            {Back.YELLOW + Fore.RED}Welcome to your very own note-taking app!!{Style.RESET_ALL}
            {Fore.WHITE}Every note is printed along an index number, date and time.
        
            {Fore.GREEN}Option 1. Add a Note
            {Fore.RED}Option 2. Edit a Note
            {Fore.CYAN}Option 3. Remove a Note
            {Fore.MAGENTA}Option 4. View Notes
            {Fore.BLUE}Option 5. Exit
            """)
        try:
            user_choice = input("Please choose a function by entering a number from 1 to 5: ")

            if user_choice == "1":
                af.add_note()
            elif user_choice == "2":
                af.edit_note()
            elif user_choice == "3":
                af.remove_note()
            elif user_choice == "4":
                af.view_notes()
            elif user_choice == "5":
                print(f"{Fore.CYAN}Exiting the program in 3,2,1...Bye")
                break
            else:
                print(f"{Fore.RED}Invalid entry, please choose an option from 1 to 5: ")
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nProgram interrupted by user, exiting in 3, 2, 1...")
            break
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
        finally:
            print (f"{Fore.MAGENTA}Thank you for visiting my app!!")
            
# This runs the 'main' function if the name of the script is main.py
if __name__ == "__main__":
    main()