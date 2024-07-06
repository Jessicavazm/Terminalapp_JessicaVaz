# Note-Taking App

## Git Repo
[Access my project in GitHub](https://github.com/Jessicavazm/Terminalapp_JessicaVaz.git)

## Dependencies
Dependencies used to run the application includes:
- colorama==0.4.6
- iniconfig==2.0.0
- packaging==24.1

## How you can use the app, list of features
In this part, I will detail how to use the app, and describe features of the `note-taking` app.

Once the app is open, it prints a welcome message and an important information about notes. Each notes is printed with a index which will be used for editing and removing a note. All notes are printed with current date and time when they were created.

Main menu contains 6 different options that are printed in different colours to help with visibility and to add styling. Package 'colorama' is used through the whole program and it's listed on requirements.txt file.

```
How colorama is used in the note app:

Green colour: Used when asking for user input and to print confirmation messages when a function was executed successfully.
Yellow colour: Used for printing messages that indicates function can't be executed and prompts user to do something for function to work.
Red colour: Used to print Errors messages that program came across while running.
```

```
Number 1: User can add a note
Number 2: User can edit a note
Number 3: User can remove a note
Number 4: User can remove all notes
Number 5: User can view notes
Number 6: User can exit the program
```

- Option number 1 (Add note):
    - With this feature, user is able to add notes to the note-taking application. User can choose to add an individual note or add multiple notes. 'Function_add' note first calls 'load_notes_json' and stores all saved notes to a variable called 'notes'. Variable 'initial_count' stores the number of items in the 'notes' list. 

    - 'Print' function displays message that prompt the user to type each note in a single line and once they finish type 'done' on a new line to save notes to note app or type 'exit' to cancel and go back to main menu. Variable 'timestamp' receives the value of current day/time which is acquired by importing datetime built-in module from Python's Library.

    - Program enters a 'while True' loop. Variable 'i' is assigned the value of user input. 'If' condition checks if 'i' value is 'done' or 'exit' and if condition matches, the function ends. 'If not' inverts the condition boolean value, so if the string is empty this statement will evaluate to true and the message will indicate note can't be an empty note and prompt the user to type content for the note. 'Continue' keeps the loop running. 'Else' condition evaluates to true if none of the conditions above were executed it uses the 'append' function to add 'note_text' and 'timestamp' variables to 'notes' list.

    - 'If' uses comparison operation '>' to check if number of items in 'notes' list is greater than 'initial_count' value, if condition evaluates to true, it calls the function 'save_notes_json' to add notes to json file and prints a message confirming that notes have been successfully added to note app.
    Function 'view_notes' is called to allow users to see the update note list. If none of the conditions above evaluate to true, 'else' is called to indicate to user that no notes were added. 

    - except 'ValueError' is called when the function receives a attribute with the wrong value.
    - except 'Exception' catches any possible error that might occur in the program's execution.

- Option number 2 (Edit note):
    - Function 'edit_note' first calls 'load_note_json' and stores existing notes in variable 'notes'. 'If not' checks if note app has any notes to edit. If it evaluates to true, it displays a message that indicates the note app is empty and prompts the user to first add a note. 'Return' ends the function since it can't proceed. If condition evaluates to false, 'view_notes' function is called and displays existing notes for user. 
    
    - Loop 'while True' runs until user types a valid input or chooses to exit the program. User input is stored in variable called 'i'. 'If' checks if 'i' value is == to 'exit' and if it evaluates to true, the loops ends. Variable 'timestamp' receives the value of current day and time. Variable 'i' is converted to integer and assigned new value. 'If' checks if user input is within the valid range => 1 and <= len(notes),if it evaluates to true, 'else' statement will be printed indicating incorrect index. If condition evaluates to true, user is asked to type new content for note and changes are stored in variable 'new_note'. 'If' new_note verifies the 'new_note' is not an empty string and updates the note with new content and new date/time. Function 'save_notes_json' is called to update json file. Function 'print' displays a message confirming the process has been successful and loop is ended. If new_note hasn't been executed, else statement prints a message indicating note cannot be empty, and it continue the loop.

    - Except 'ValueError' catches wrong input values and 'exception' catches any other possible error that might occur in the program's execution.
    
- Option number 3(Remove note)
    - Function 'remove_note' first calls function 'load_notes_json' from file_operation module and assigns value variable 'notes'. 'If not' checks if 'notes' is empty, if it evaluates to true it prompts the user to add a note first and 'return' ends the function and goes back to main mene otherwise function 'view_notes' is called and displays list of notes.
    
    - Loop 'while True' runs until user enters a valid input or decides to exit. User input is stored in variable 'i'. If first checks if 'i' value equals to 'exit', condition becomes true and program breaks the execution. 'I' converts user input to integer and assign values back to variable 'i'. If 'i' is =>1 and <= items in the notes list , function 'pop' removes note using (i - 1) -1 is necessary note items are displayed with index 1 instead of 0. Function 'save_notes_json' is called to update changes and afterwards a confirmation message is displayed and function 'view_notes' is called so user can see changes made to their note app. Program exits to main function after this. 'Else' statement is called if the statement above wasn't called and index number was out of the range, it displays a message indicating to user index number is wrong and to check index which is displayed next to printed notes.
    
    - 'ValueError' catches wrong values passed to function and 'exception' catches any possible error that might occur in the execution process.

- Option number 4 (Clear all notes):
    - Function allows user to delete all notes at once. Function 'clear_note' first calls function 'load_notes_json' from file_operation module and assigns value variable 'notes'. 'If not' checks if note app is empty, if it evaluates to true it indicates to user notebook is empty and prompts user to add a note first. 'Return' ends the function since it cannot proceed.

    - Function 'clear' erases all of the content from variable 'notes'. Afterwards it calls function 'save_notes_json' and updates changes to json file. Function 'print' displays a message confirming the process has been successful.

- Option number 5 (View Notes):
    - Function view_notes first calls function 'load_notes_json' from file_operation module and assigns value variable 'notes'. 'If not' checks if note app is empty, if it evaluates to true, it displays a message indicating the app is empty and it prompts the user to add a note first. 'Return' ends the function since it cannot proceed.

    - 'For' and 'in' iterates over each item in the list 'notes' and it assigns each item with an index number starting from number 1. Print function prints all notes stored in the variable notes along date/time and index number.

    - 'Exception' catches any possible error that might occur in the process.

- Option number 6 (Exit):
    - This option lets user exit the program, it prints a message thanking the user for visiting the app.

### File handling functions
'Save_note_json' and 'load_notes_json' imports built in modules (json and os) from Python library to handle file operations.

- Function 'save_note_json' opens the file in write mode and save all changes to file using function 'dump.json'. 'With' statements makes sure the file is close after changes are done and it prints a message confirming changes to json file. 

- Except catches errors in the execution of the progress.
    - FileNotFoundError: program couldn't find the json file.
    - IOError: Errors that occur during Input/Output operations.
    - Exception: catches any other errors that might occur.


- Function 'load_notes_json' checks if the specified file exists. 'If' os.path.exist evaluates to true, 'with open' try to open the file in reading mode. Content from json file is stored in variable 'notes' and 'return' returns the notes content.

- Except catches errors in the execution of the progress.
    - FileNotFoundError: program couldn't find the json file.
    - JSONDecodeError: Invalid json data
    - IOError: Errors that occur during Input/Output operations.
    - Exception: catches any other errors that might occur.
    

