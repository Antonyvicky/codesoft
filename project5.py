class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the book.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, contact_name, new_contact):
        for contact in self.contacts:
            if contact.name == contact_name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address

    def delete_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact.name != contact_name]

def main():
    contact_book = ContactBook()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Found Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No contacts found.")
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(name, new_contact)
            print("Contact updated.")
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()