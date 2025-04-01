# Python-wk-4-Assignment

How this program works:

Imports os module: This is used to extract the base name of the input file for creating the output filename.
modify_file_content function:
Takes the input and output filenames as arguments.
Error Handling (try...except): It uses a try...except block to handle potential errors during file operations.
Reading the input file:
It attempts to open the input_filename in read mode ('r').
infile.readlines() reads all lines from the file and stores them as a list in the content variable.
Modifying the content:
It initializes an empty list modified_content.
It iterates through each line in the content list.
For each line, it adds the prefix "Modified: " to it and appends the modified line to the modified_content list. (You can change this modification logic as per your requirement)
Writing to the output file:
It attempts to open the output_filename in write mode ('w'). If the file doesn't exist, it will be created. If it exists, its content will be overwritten.
outfile.writelines(modified_content) writes all the modified lines from the list to the output file.
Success Message: If the file operations are successful, it prints a confirmation message.
Error Handling (except blocks):
FileNotFoundError: Catches the error if the user-provided input file does not exist.
PermissionError: Catches the error if the script doesn't have the necessary permissions to read the input file or write to the output file.
Exception as e: Catches any other unexpected errors that might occur and prints an informative message.
if __name__ == "__main__": block:
This ensures that the code inside this block only runs when the script is executed directly (not when it's imported as a module).
Asking for filename: It prompts the user to enter the name of the file they want to process using the input() function.
Creating output filename: It creates a new filename by adding the prefix "modified_" to the base name of the input file (e.g., if the input is "my_document.txt", the output will be "modified_my_document.txt").
Calling the function: It calls the modify_file_content function with the user-provided input filename and the generated output filename.
To use this script:

Save the code as a Python file (e.g., file_modifier.py).
Run the script from your terminal or command prompt using: python file_modifier.py
The script will ask you to enter the filename. Type the name of an existing file and press Enter.
The script will then attempt to read the file, modify its content, and write it to a new file named modified_your_input_filename.txt in the same directory.
If there are any errors (file not found, permission issues, etc.), it will print an appropriate error message.