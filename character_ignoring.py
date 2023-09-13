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
