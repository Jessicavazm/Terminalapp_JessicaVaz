# Note-Taking App

## Git Repo
[Access my project in GitHub](git@github.com:Jessicavazm/Terminalapp_JessicaVaz.git)

## Dependencies
Colorama = 0.4.6
Pytest

## How you can run the app

## How you can use the app, list of features
Once the apps open, it welcomes you and ask to type a number 1-5 correspondent to the function you like to proceed.

- Number 1: User can add a note
- Number 2: User can edit a note
- Number 3: User can remove a note
- Number 4: User can view notes
- Number 5: User can exit the program

``` 
Feature number 1: With this feature, user is able to add notes to the application, notes are taken individually, in case user wants to add two notes, user needs choose option number 1, then type the note and re-do the process again to add another note. When `add_note` function is called, it first asks user for note input which will be stored in variable called `note_text`. IF not operator and strip function will evaluate if the `note_text` is empty, if it evaluates to true, it will raise a `ValueError`, and direct the user to enter a non-empty note.

Variable `note` will take the value of `note_text` and `timestamp` which is a variable that uses package datetime from the Python Library to display current day and time and function `append` will add `note` variable to `notes` list. 

If user types a valid value and the process is successful, user will see the message "Your note has been successfully added".Function `save_notes_json` will be called to save notes to Json file and function `view_notes` will be also called to display `notes` list, allowing user to see added notes. Each note is displayed with index number, note content, date and time note was created. 

Try and Except were used to handle errors, try contains the block of code that might result in an error, in this case contains the `add_note` function and user input, except contains block of codes that should be executed in case an error occurs.
- `exception ValueError` catches and stores exceptions of `ValueErrors` in variable `ve` which is display in the print function.
- `exception Exception` will be executed for any other error which is not `ValueError`.



Option number 2: 

Option number 3:

Option number 4:

Option number 5: