from storage import read_contacts, write_contacts
from util import verify_email, verify_phone, get_contact_by_name


CONTACT_FILE ="contacts.json"


def add_contact(contacts):
    first_name = input("First Name: ").lower().strip()
    last_name = input("Last Name: ").lower().strip()
    mobile_phone = input("Mobile Phone Number: ").strip()
    home_phone = input("Home Phone Number: ").strip()
    email_address = input("Email Address: ").strip()
    street_address = input("Address: ").strip()

    if not first_name or not last_name:
        print("Contact must have a first and last name.")
    elif mobile_phone and not verify_phone(mobile_phone):
        print("Invalid mobile phone number.")
    elif home_phone and not verify_phone(home_phone):
        print("Invalid home phone number.")
    elif email_address and not verify_email(email_address):
        print("Invalid email address.")
    elif get_contact_by_name(first_name, last_name, contacts):
        print("A contact with this name already exists.")
    else:
        new_contact = {
            "first_name": first_name,
            "last_name": last_name,
            "mobile_phone": mobile_phone,
            "home_phone": home_phone,
            "email_address": email_address,
            "street_address": street_address
        }
        contacts.append(new_contact)
        print("Contact Added!")
        return 
    print("You entered invalid information. Contact was not added.")

def search_for_contact(contacts):
    first_name_search = input("First Name: ").lower().strip()
    last_name_search = input("Last Name: ").lower().strip()
    matches = []
    for contact in contacts:
        first_name = contact['first_name']
        last_name = contact['last_name']

        if first_name_search not in first_name:
            continue
        if last_name_search not in last_name:
            continue 
        matches.append(contact)
    print(f"Found {len(matches)} matching contacts.")
    list_contacts(matches)


def delete_contact(contacts):
    first_name = input("First Name: ").lower().strip()
    last_name = input("Last Name: ").lower().strip()

    contact = get_contact_by_name(first_name, last_name, contacts)

    if not contact:
        print("No contact with this name exists.")
    else:
        confirm = input("Are you sure you want to delete this contact? (y/n)? ").lower()
        if confirm == "y":
            contacts.remove(contact)
            print("Contact deleted!")

def contact_string(contact):
    string = f"{contact['first_name'].capitalize()} {contact['last_name'].capitalize()}"

    for field in ['mobile_phone', 'home_phone', 'email_address', 'street_address']:
        value = contact[field]
        if not value:
            continue
        string += f"\n\t{field.capitalize()}: {value}"
    return string 

def list_contacts(contacts):
    sorted_contacts = sorted(contacts, key=lambda x: x['first_name'])


    for i, contact in enumerate(sorted_contacts):
        print(f"{i +1}. {contact_string(contact)}")
        

        

def main(contacts_path):
    print('''
    Welcome to your contact list!
    The following is a list of useable commands:      
    "add": Adds a contact.
    "delete": Deletes a contact.
    "list": Lists all contacts.
    "search": Searches for a contact by name.
    "q": Quits the program and saves the contact list.
    ''')

    contacts = read_contacts(contacts_path)

    while True:
        command = input("Type a command: ").lower().strip()
    
        if command == "add":
            add_contact(contacts)
        elif command == "delete":
            delete_contact(contacts)
        elif command == "list":
            list_contacts(contacts)
        elif command == "search":
            search_for_contact(contacts)
        elif command == "q":
            write_contacts(contacts_path, contacts)
            print("Contacts were saved successfully.")
            break 
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main(CONTACT_FILE)




