import json
import sys
from email_validation import is_valid_email
from character_ignoring import apply_character_ignoring
from duplicate_removal import remove_duplicates

# Main program
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Check if a JSON file argument is provided
        input_filename = sys.argv[1]
        
        try:
            with open(input_filename, "r") as json_file:
                user_input = json.load(json_file)
        except FileNotFoundError:
            print(f"File '{input_filename}' not found. Provide a valid JSON file.")
            sys.exit(1)
    else:
        # Read user input from STDIN
        print("Enter email addresses (one per line), type 'done' when finished:")
        user_input = []
        while True:
            email = input()
            if email.lower() == "done":
                break
            if is_valid_email(email):
                user_input.append(email)
            else:
                print(f"Invalid email address: {email}")

    # Apply character ignoring
    modified_emails = apply_character_ignoring(user_input)

    # Remove duplicates
    unique_emails = remove_duplicates(modified_emails)

    # Print the unique email addresses
    for email in unique_emails:
        print(email)
