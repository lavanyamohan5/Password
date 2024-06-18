# Password
a simple password generator using python
# Password Generator

A simple password generator application built using Python's Tkinter library. This application allows users to input and display passwords in a masked format.

## Features

- Password input field with masked characters
- Button to generate and display the entered password

## Prerequisites

- Python 3.x
- Tkinter (comes pre-installed with standard Python distribution)

## Installation

1. Ensure Python 3.x is installed on your machine.
2. Clone the repository or download the script file.

## Usage

1. Run the script using Python:
    ```bash
    python password_generator.py
    ```

2. A window titled "password generator" will open.

3. Use the input field to enter your password:
    - **Password Field**: Type your password, which will be masked with asterisks (`*`).

4. Click the "generate password" button to display the entered password:
    - **Password Display**: The entered password will be shown in a label below the button in an unmasked format.

## Script Breakdown

- **Imports**:
    - `tkinter` for GUI components

- **Main Window Setup**:
    - `window` to initialize the main window

- **Entry Widget**:
    - `entry` for password input with masked characters

- **Button Function**:
    - `password()`: Retrieves the entered password from the entry widget and sets it to the `password_var` variable.

- **Button**:
    - `generate_button` to trigger the password display function

- **Label**:
    - `password_label` to display the entered password in an unmasked format

## Error Handling

- The script does not include specific error handling, as it assumes valid input will be provided by the user.

## License

This project is licensed under the MIT License.
