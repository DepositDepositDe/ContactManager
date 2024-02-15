Contact Management System Documentation
Introduction

This document serves as the documentation for the Contact Management System developed in Python. The system allows users to perform basic CRUD operations (Create, Read, Update, Delete) on a list of contacts. Contacts are stored in a JSON file, and the program provides a simple command-line interface for interaction.
Features

    Add new contacts with name, phone number, and email.
    View all existing contacts.
    Update details of existing contacts.
    Delete contacts.
    Contacts are persisted across sessions by saving them to a JSON file.

Requirements

    Python 3.x
    json module (standard library)

Usage

    Download or clone the Python script contact_management_system.py.
    Ensure you have Python installed on your system.
    Run the script using the command python contact_management_system.py.
    Follow the on-screen instructions to interact with the Contact Management System.

Functions
load_contacts()

    Description: Loads contacts from a JSON file.
    Parameters: None.
    Returns: List of contacts.

save_contacts(contacts)

    Description: Saves contacts to a JSON file.
    Parameters:
        contacts: List of contacts to be saved.
    Returns: None.

add_contact(contacts)

    Description: Allows users to add a new contact.
    Parameters:
        contacts: List of contacts.
    Returns: None.

view_contacts(contacts)

    Description: Displays all contacts stored in the system.
    Parameters:
        contacts: List of contacts.
    Returns: None.

update_contact(contacts)

    Description: Allows users to update an existing contact.
    Parameters:
        contacts: List of contacts.
    Returns: None.

delete_contact(contacts)

    Description: Allows users to delete a contact.
    Parameters:
        contacts: List of contacts.
    Returns: None.

main()

    Description: Main function to drive the program flow.
    Parameters: None.
    Returns: None.

Example Usage

python

if __name__ == "__main__":
    main()

Sample Workflow

    User runs the script.
    The program loads existing contacts (if any) from the JSON file.
    The program displays a menu with options to add, view, update, or delete contacts.
    User selects an option and provides necessary inputs.
    The program executes the chosen operation and updates the contact list accordingly.
    If the user chooses to exit, the program saves the updated contact list to the JSON file and terminates.

Conclusion

The Contact Management System provides a straightforward solution for managing contacts efficiently. It leverages file I/O operations and JSON serialization to ensure data persistence and offers a user-friendly interface for interacting with the contact list. This system can be easily extended to incorporate additional features or integrate with other applications.
