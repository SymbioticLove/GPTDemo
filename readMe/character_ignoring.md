# Character Ignoring Module

This module provides a function for applying character ignoring to email addresses.

## Function

- `apply_character_ignoring(emails)`: Removes periods from the local part of email addresses while preserving the domain part.

## Example Usage

```python
from character_ignoring import apply_character_ignoring

emails = ["example@email.com", "user.name@email.com"]
modified_emails = apply_character_ignoring(emails)
print(modified_emails)
```
