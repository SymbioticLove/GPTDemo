# Duplicate Removal Module

This module provides a function for removing duplicates from a list of email addresses.

## Function

- `remove_duplicates(emails)`: Removes duplicate email addresses from a list.

## Example Usage

```python
from duplicate_removal import remove_duplicates

emails = ["example@email.com", "user.name@email.com", "example@email.com"]
unique_emails = remove_duplicates(emails)
print(unique_emails)
```