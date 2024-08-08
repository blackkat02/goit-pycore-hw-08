from collections import UserDict
from datetime import date, datetime, timedelta
from birthday_bot.birthday import Birthday


class AddressBook(UserDict):
    """Provides a dictionary-like interface for managing records in an address book.
        This class inherits from `UserDict` to provide dictionary-like behavior for storing
        and retrieving records.
        """

    def add_record_phone(self, record):

        """Adds a Record object to the address book, checking for duplicate names.
        Args:
            record (Record): The Record object to add.
        Raises:
            ValueError: If a record with the same name already exists.
        """
        if record.name.value in self.data:
            print(f"Warning: Duplicate name '{record.name.value}'. Skipping record.")
        else:
            self.data[record.name.value] = record

    def find(self, name: str):
        """Finds a record by name.
        Args:
            name (str): The name to search for.
        Returns:
            Record: The record object found, or None if not found.
        """
        return self.data.get(name)

    def delete(self, name: str):
        """Deletes a record from the address book.
        Args:
            name (str): The name of the record to delete.
        """
        if name in self.data:
            print(name, self.data[name])
            del self.data[name]
            print(name)

    @property
    def get_upcoming_birthdays(self) -> str:
        """Calculates and returns a list of upcoming birthdays within the next 7 days.
        This method considers weekends (Saturdays and Sundays) to avoid scheduling
        congratulations on those days.
        Returns:
            str: A list of dictionaries containing name and congratulation date
                        for upcoming birthdays.
        """
        upcoming_list_birthdays = []
        current_date = datetime.now().date()
        print(f"Today is {current_date.strftime("%d.%m.%Y")}")

        for name, record in self.data.items():
            if isinstance(record.birthday, Birthday):
                birthday_this_year = record.birthday.value.replace(year=current_date.year)
            else:
                birthday_this_year = current_date.replace(day=current_date.day - 1)

            if birthday_this_year < current_date:
                birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

            if birthday_this_year - current_date <= timedelta(days=7):
                birthday_weekday = int(birthday_this_year.strftime("%w"))
                number_weekday = [6, 0]
                if birthday_weekday in number_weekday:
                    days = 2 - number_weekday.index(birthday_weekday)
                    birthday_this_year += timedelta(days=days)

                upcoming_list_birthdays.append(
                    {"name": record.name.value[0],
                     "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")}
                )

        if upcoming_list_birthdays:
            return (f"The birthday contact list for the next 7 days is: \n"
                    f"{'\n'.join([f"{i + 1}. {t}" for i, t in enumerate(upcoming_list_birthdays)])}")
        return "The birthday contact list for the next 7 days is empty"