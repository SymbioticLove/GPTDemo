import json
import sys
import re

# Regular expression for email validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to validate email addresses
def is_valid_email(email):
    return re.match(email_regex, email)

# Function to apply character ignoring
def apply_character_ignoring(emails):
    modified_emails = []
    for email in emails:
        local_part, domain_part = email.split('@')
        # Remove periods only from the local part
        modified_local_part = local_part.replace(".", "")
        modified_email = f"{modified_local_part}@{domain_part}"
        modified_emails.append(modified_email)
    return modified_emails

# Function to remove duplicates
def remove_duplicates(emails):
    return list(set(emails))

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
