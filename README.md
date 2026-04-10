# Practice Week Two Repository

This repository contains a simple Python script for practicing basic programming concepts, including input validation and name lookup.

## Contents

- **src/function.py**: Contains two Python functions:
  - `get_user_name()`: Prompts the user for their name, validates the input (ensuring it's not empty, whitespace-only, purely numeric, or too short), and returns a personalized greeting message.
  - `lookup_name(name)`: Checks if a given name exists in a predefined list and returns a boolean.
- **src/constants.py**: Holds a constant list of names (`namelist`) used by the lookup function.

## Usage

Run the script to interact with the name input and greeting:

```bash
python src/function.py
```

The script will ask for your name, validate it, and display a greeting. The `lookup_name` function can be imported and used to check names against the list in `constants.py`.

Example usage in code:

```python
from src.function import lookup_name

result = lookup_name("alice")  # Returns False if not in list
```

## Getting Started

1. Clone this repository:
   ```bash
   git clone <repo-url>
   ```
2. Navigate to the directory and run the script:
   ```bash
   cd practice-weektwo
   python src/function.py
   ```

## Improvements

My branching strategy was overly simple. I'd normally break these changes into separate branches since some of them were major changes. For my commits I focused on small iterations mostly on function changes to iterate quickly.

In the future I'd plan the work better and align an appropriate amount of work into each branch so that they're sized appropriately and easier for PR reviews. I could implement a class structure to accommodate more names and maybe add some more greetings. Adding unit tests for the functions would be a good addition. An action workflow would also be good to have this run on Github Actions. Creating a dev, test and production environment would be good to test changes before going to production.

## License

This project is for educational and practice purposes only.
