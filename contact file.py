import json

CONTACTS_FILE = "contacts.json"

# Load existing contacts
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"{name}: {details['Phone']}")
    else:
        print("No contacts found.")

# Search for a contact
def search_contact():
    query = input("Enter name or phone number to search: ")
    contacts = load_contacts()
    for name, details in contacts.items():
        if query == name or query == details["Phone"]:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return
    print("Contact not found.")

# Update contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

# Delete contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

# Main Menu
def contact_book():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Contact Book program
contact_book()
