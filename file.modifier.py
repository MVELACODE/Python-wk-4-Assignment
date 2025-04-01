import os

def modify_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        modified_content = []
        for line in content:
            modified_content.append(f"Modified: {line}")

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Successfully read '{input_filename}' and wrote the modified content to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read or write to the specified file(s).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the name of the file you want to process: ")
    output_file = f"modified_{os.path.basename(input_file)}"  # Create a new filename

    modify_file_content(input_file, output_file)