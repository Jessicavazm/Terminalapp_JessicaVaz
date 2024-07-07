# Import Colorama package to use colours in printing.
from colorama import Fore, Back, Style, init 

# Import app_function and file_operations modules to use functions.
import app_functions as af

# Initializes and automatically resets text colours.
init(autoreset=True)

# Main function displays main menu options and asks for user's input.
def main():
    
    # 'While True' runs main menu until user types a valid input or chooses to exit. 
    # Fore.Colour add a different colour to each menu option.
    while True:
        print(f"""
            {Back.YELLOW + Fore.RED}Welcome to your very own note-taking app!!{Style.RESET_ALL}
            {Fore.WHITE}Every note is printed along an index number, date and time.
        
            {Fore.GREEN}Option 1. Add a Note
            {Fore.RED}Option 2. Edit a Note
            {Fore.CYAN}Option 3. Remove a Note
            {Fore.MAGENTA}Option 4. Remove all Notes
            {Fore.YELLOW}Option 5. View Notes
            {Fore.BLUE}Option 6. Exit
            """)
        # Each option calls a specific function. If/elif determines the program's flow. 
        # User input is stored in 'user_choice' variable and then matched to different functions.
        try:
            user_choice = input("Please choose a function by entering a number from 1 to 6: ")
        
            if user_choice == "1":
                af.add_note()
            elif user_choice == "2":
                af.edit_note()
            elif user_choice == "3":
                af.remove_note()
            elif user_choice == "4":
                af.clear_notes()
            elif user_choice == "5":
                af.view_notes()
            elif user_choice == "6":
                print(f"{Fore.CYAN}Thank you for visiting my app. Exiting the program in 3,2,1...Bye")
                break
            else:
                print(f"{Fore.RED}Invalid entry, please choose an option from 1 to 6: ")  
                                
        # Except handles KeyBoardInterrupt.
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nProgram interrupted by user, exiting in 3, 2, 1...")
            break
        # Exception handles any errors that might occur while program's execution.
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")
        # Finally informs users added notes are always saved.
        finally:
            print(f"{Fore.MAGENTA}If you have added any notes, they will be saved for the next time.")
            
# Checks if this script runs as the main function.
# If it evaluates to true, it allows to call the function by calling main().
if __name__ == "__main__":
    main()