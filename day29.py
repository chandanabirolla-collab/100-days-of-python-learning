"""
This module provides simple math operations.
It is a great example of how to use module-level docstrings.
"""

def greet_user(name):
    """
    Greets the user by their name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A friendly greeting message.
    """
    return f"Hello, {name}! Welcome back."

# Example of how to access docstrings programmatically
print(greet_user("Candy"))

# You can print the docstring using the __doc__ attribute
print(greet_user.__doc__)