import re

# Regular expression for email validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to validate email addresses
def is_valid_email(email):
    return re.match(email_regex, email)
