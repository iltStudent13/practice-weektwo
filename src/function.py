from constants import namelist

def get_user_name() -> str:
    """This function will ask the user for their name and return it as a string.
    
    Returns:
        str: The user's name.

    """
    initial_input = input("What is your name? ")

    if initial_input == "" or initial_input.isspace():
        print("Please enter a valid name.")
        return get_user_name()
    elif initial_input.isdigit():
        print("Please enter a string value for your name, not just numbers.")
        return get_user_name()
    elif len(initial_input.strip()) < 2:
        print("Name must be at least 2 characters long.")
        return get_user_name()
    else:
        name = initial_input.strip()
    return name

def lookup_name(name: str) -> bool:
    """This function will look up the name in the namelist and return a boolean indicating whether the name is in the list or not.
    
    Args:
        name (str): The name to look up.
    Returns:
        boolean: True if the name is in the namelist, False otherwise.
    """
    return name.lower() in namelist

def special_greeting() -> str:
    """This function will return a special greeting message if the name is in the namelist, otherwise it will return a generic greeting message.
    
    Args:Nate
        name (str): The name to look up.
    Returns:
        str: A special greeting message if the name is in the namelist, otherwise a generic greeting message.
    """
    name = get_user_name()

    if lookup_name(name):
        return f"Hello {name}! You are on the list!"
    else:
        return f"Hello {name}! Nice to meet you!"

if __name__ == "__main__":
    print(special_greeting())