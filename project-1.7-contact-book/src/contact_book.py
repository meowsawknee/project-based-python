import json
import os
from typing import Optional, Dict
from prettytable import PrettyTable


class ContactBook:
    """
    Manages a simple contact book using in-memory dictionary.
    Supports CRUD operations and persistent storage via JSON.
    """

    def __init__(self, filename: str = "contacts.json") -> None:
        """Initializes an empty contact book and loads from file if available."""
        self.filename = filename
        self.contacts: Dict[str, Dict[str, Optional[str]]] = {}
        self.load_contacts_from_file()

    def load_contacts_from_file(self) -> None:
        """Loads contacts from a JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.contacts = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Warning: Could not load contacts file. Starting with empty contact book.")

    def save_contacts_to_file(self) -> None:
        """Saves the current contacts dictionary to a JSON file."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.contacts, file, indent=4) # indent=4  # makes the JSON output nicely formatted and human-readable
        except IOError:
            print("Error: Could not save contacts to file.")

    def add_contact(
        self,
        id_number: str,
        name: str,
        email: str,
        country: Optional[str] = None,
        address: Optional[str] = None,
        phone: Optional[str] = None
    ) -> bool:
        """
        Adds a new contact to the contact book if ID is unique.
        Returns True if added, False if contact exists.
        """
        if id_number in self.contacts:
            print("Contact Already Exists!")
            return False

        self.contacts[id_number] = {
            "name": name,
            "email": email,
            "country": country,
            "address": address,
            "phone": phone
        }
        self.save_contacts_to_file()
        return True

    def view_contacts(self) -> str:
        """
        Returns a string table of all contacts.
        """
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Email", "Country", "Address", "Phone"]

        for id_number, info in self.contacts.items():
            table.add_row([
                id_number,
                info["name"],
                info["email"],
                info["country"],
                info["address"],
                info["phone"]
            ])

        return str(table)

    def delete_contact(self, id_number: str) -> bool:
        """
        Deletes a contact by ID. Returns True if successful, False if ID not found.
        """
        if id_number in self.contacts:
            del self.contacts[id_number]
            self.save_contacts_to_file()
            print("Contact deleted successfully!")
            return True

        print("There is no contact with this ID!")
        return False

    def update_contact(
        self,
        id_number: str,
        name: Optional[str] = None,
        email: Optional[str] = None,
        country: Optional[str] = None,
        address: Optional[str] = None,
        phone: Optional[str] = None
    ) -> bool:
        """
        Updates an existing contact. Only non-None values will be updated.
        Returns True if updated, False if ID not found.
        """
        if id_number not in self.contacts:
            print("Contact not found!")
            return False

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

        self.save_contacts_to_file()
        print("Contact updated successfully!")
        return True
