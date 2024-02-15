import json

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Function to save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    email = input("Enter the email: ")
    contact = {"name": name, "number": number, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}")

# Function to update a contact
def update_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            idx = int(input("Enter the index of the contact you want to update: ")) - 1
            contact = contacts[idx]
            name = input("Enter the new name (press enter to keep unchanged): ")
            number = input("Enter the new number (press enter to keep unchanged): ")
            email = input("Enter the new email (press enter to keep unchanged): ")
            if name:
                contact['name'] = name
            if number:
                contact['number'] = number
            if email:
                contact['email'] = email
            save_contacts(contacts)
            print("Contact updated successfully.")
        except (IndexError, ValueError):
            print("Invalid index.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            idx = int(input("Enter the index of the contact you want to delete: ")) - 1
            del contacts[idx]
            save_contacts(contacts)
            print("Contact deleted successfully.")
        except (IndexError, ValueError):
            print("Invalid index.")

# Main function
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
