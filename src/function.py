from constants import namelist

def get_user_name() -> str:
    """This function will ask the user for their name and return it as a string.
    
    Returns:
        str: Greeting message with the user's name.

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
    printname = f"Hello {name}! Have a great day."
    return printname

#Function looks up the name in the namelist and returns a special greeting
def lookup_name(name: str) -> bool:
    """This function will look up the name in the namelist and return a boolean indicating whether the name is in the list or not.
    
    Args:
        name (str): The name to look up.
    Returns:
        boolean: True if the name is in the namelist, False otherwise.
    """
    return name.lower() in namelist

if __name__ == "__main__":
    print(get_user_name())