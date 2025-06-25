class ContactBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, id_number, name, email, country=None, address=None, phone=None):
        if id_number in self.contacts:
            print("Contact Already Exists!")
            return
        
        self.contacts[id_number] ={
            "name": name,
            "email": email,
            "country": country,
            "address": address,
            "phone": phone
        }
    
    def view_contacts(self):
        for id_number, info in self.contacts.items():
            print(f'Name: {info["name"]}')
            print(f'ID: {id_number}')
            print(f'Email: {info["email"]}')
            print(f'Country: {info["country"]}')
            print(f'Address: {info["address"]}')
            print(f'Phone: {info["phone"]}')
            print("-" * 30)
        
    def delete_contact(self, id_number):
        if id_number in self.contacts:
            del self.contacts[id_number]
            print("Contact deleted successfully!")
        else:
            print("There is no contact with this ID!")

    def update_contact(self, id_number, name=None, email=None, country=None, address=None, phone=None):
        if id_number in self.contacts:
            if name:
                self.contacts[id_number]["name"] = name
            if email:
                self.contacts[id_number]["email"] = email
            if country:
                self.contacts[id_number]["country"] = country
            if address:
                self.contacts[id_number]["address"] = address
            if phone:
                self.contacts[id_number]["phone"] = phone
            
            print("Contact updated successfully!")
            return
        
        print("Contact not found!")


if __name__ == "__main__":

    book = ContactBook()

    while True:
        print("\nWelcome to contact book application!")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contact")
        print("4. Delete Contact")
        print("5. Quit")

        user_choice = input("Please choose an option: ")

        if user_choice == "5":
            break

        elif user_choice == "1":
            id_number = input("Enter Contact ID: ")
            name = input("Enter contact name: ")
            email = input("Enter contat Email: ")
            country = input("Enter contact Country: ")
            address = input("Enter contact Address: ")
            phone = input("Enter contact Phone Number: ")

            book.add_contact(id_number, name, email, country, address, phone)
        
        elif user_choice == "2":
            print("Edit msg")
            id_number = input("Enter Contact ID: ")
            name = input("Enter contact name: ")
            email = input("Enter contat Email: ")
            country = input("Enter contact Country: ")
            address = input("Enter contact Address: ")
            phone = input("Enter contact Phone Number: ")

            book.update_contact(id_number, name, email, country, address, phone)
        
        elif user_choice == "3":
            print("List of Contacts: ")
            book.view_contacts()
        
        elif user_choice == "4":
            id_number = input("Enter contact ID: ")
            book.delete_contact(id_number)
