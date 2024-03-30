#File Creation:
#Create a Python script (file_handling_assignment.py) that does the following:
#Creates a new text file named "my_file.txt" in write mode ('w').
#Write at least three lines of text to the file, including a mix of strings and numbers.

try:
    # Created a text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # three lines with a mix of strings and numbers
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 3.14\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File creation completed.\n")

#File Reading and Display:
#Enhance your script to read the contents of "my_file.txt" and display them on the console.

try:
    # Opens "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        contents = file.read()
        # Display the contents on the console
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("\nFile reading completed.\n")


#File Appending:
#Modify the script to open "my_file.txt" in append mode ('a').
#Append three additional lines of text to the existing content.
#Error Handling:
#Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).
try:
    # Opens "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Access denied.")
finally:
    print("File appending completed.")
    

