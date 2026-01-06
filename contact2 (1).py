import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    print("\nAdd New Contact")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Search contact by name or phone
def search_contact(contacts):
    keyword = input("\nEnter name or phone number to search: ").strip().lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

# Update contact
def update_contact(contacts):
    phone = input("\nEnter phone number of contact to update: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            print("Enter new details (leave blank to keep old value)")
            contact["name"] = input(f"Name ({contact['name']}): ") or contact["name"]
            contact["email"] = input(f"Email ({contact['email']}): ") or contact["email"]
            contact["address"] = input(f"Address ({contact['address']}): ") or contact["address"]

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")

# Delete contact
def delete_contact(contacts):
    phone = input("\nEnter phone number of contact to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()