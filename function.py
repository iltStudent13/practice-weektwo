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
    else:
        name = initial_input.strip()
    printname = f"Hello {name}! Have a great day."
    return printname

if __name__ == "__main__":
    print(get_user_name())