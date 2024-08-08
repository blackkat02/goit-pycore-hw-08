from birthday_bot.name import Name
from birthday_bot.birthday import Birthday
from birthday_bot.address_book import AddressBook
from birthday_bot.decorators import InputError
from birthday_bot.phone import Phone
from datetime import date, datetime, timedelta
from typing import Any, Union, Dict, List


class Record:
    """Represents a record (contact) in the address book."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number: str) -> None:
        """Adds a phone number to the contact, enforcing phone number format.
        Args:
            phone (Phone): A Phone object representing the phone number.
        Raises:
            InputError: If the phone number is not a valid Phone object.
        """
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise InputError("Phone number must be 10 digits.")
        self.phones.append(phone_number)

    def remove_phone(self, phone_number):
        """Removes a phone number from the contact.
        Args:
            phone_number (str): The phone number to remove.
        """
        for phone in self.phones:
            if phone == phone_number:
                self.phones.remove(phone)

    def edit_phone(self, old_phone_number, new_phone_number):
        """Edits a phone number in the contact.
        Args:
            old_phone_number (str): The old phone number to replace.
            new_phone_number (str): The new phone number to add.
        Raises:
            InputError: If the old phone number is not found.
            InputError: If the new phone number doesn't have 10 digits.
        """
        if len(new_phone_number) != 10 or not new_phone_number.isdigit():
            raise InputError("The new phone number must be 10 digits.")
        len_start = len(self.phones)
        Record.remove_phone(self, phone_number=old_phone_number)
        if len(self.phones) == len_start:
            raise InputError("The old phon number is not exist")

        self.add_phone(new_phone_number)

    def find_phone(self, phone_number: str):
        """Finds a phone number in the contact.
        Args:
            phone_number (str): The phone number to search for.
        Returns:
            Phone | None: The Phone object if found, otherwise None.
        """
        for phone in self.phones:
            if phone == phone_number:
                return phone
        return None

    def add_date_of_birth(self, date_of_birth: str) -> Birthday:
        """Adds a date of birth, ensuring validity through a Birthday object creation.
        Args:
            date_of_birth (str): The date of birth, string in DD.MM.YYYY format.
        Returns:
            Birthday: The created Birthday object.
        """
        self.birthday = Birthday(date_of_birth)
        return self.birthday

    def __str__(self) -> str:
        """Defines the string representation of the record, used when printing.
        Returns:
            str: A formatted string with name, phones, and birthday (if set).
        """
        phones_str = '; '.join(p for p in self.phones)
        birthday_str = self.birthday.value.strftime('%d.%m.%Y') if self.birthday else "No birthday"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"
