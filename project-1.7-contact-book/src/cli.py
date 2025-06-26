from src.contact_book import ContactBook


def safe_input(prompt: str) -> str:
    value = input(prompt)
    return value.strip() if value.strip() else None

def run_cli() -> None:
    book = ContactBook()

    while True:
        print("\nWelcome to the Contact Book!")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        elif choice == "1":
            id_number = input("Enter Contact ID: ")
            name = input("Enter name: ")
            email = input("Enter Email: ")
            country = input("Enter Country (optional): ")
            address = input("Enter Address (optional): ")
            phone = input("Enter Phone Number (optional): ")

            if book.add_contact(id_number, name, email, country, address, phone):
                print("Contact added successfully.")
            else:
                print("Contact with this ID already exists.")
        
        elif choice == "2":
            id_number = input("Enter ID to update: ")
            name = safe_input("New name (or leave blank): ")
            email = safe_input("New Email (or leave blank): ")
            country = safe_input("New Country (or leave blank): ")
            address = safe_input("New Address (or leave blank): ")
            phone = safe_input("New Phone Number (or leave blank): ")

            if not book.update_contact(id_number, name, email, country, address, phone):
                print("No contact found with this ID.")
        
        elif choice == "3":
            print(book.view_contacts())
        
        elif choice == "4":
            id_number = input("Enter ID to delete: ")
            if not book.delete_contact(id_number):
                print("No contact found with this ID.")

        else:
            print("Invalid option. Please choose 1-5.")
