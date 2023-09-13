# Email Validation Module

This module provides a function for validating email addresses using regular expressions.

## Function

- `is_valid_email(email)`: Validates an email address using a regular expression pattern.

## Example Usage

```python
from email_validation import is_valid_email

email = "example@email.com"
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
```
