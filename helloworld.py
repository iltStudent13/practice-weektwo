def get_user_name() -> str:
    """This function will ask the user for their name and return it as a string.
    
    Returns:
        str: Greeting message with the user's name.

    """
    name = str(input("What is your name? "))
        
    printname = f"Hello {name}! Have a great day."
    return printname

if __name__ == "__main__":
    print(get_user_name())