from birthday_bot.field import Field
from datetime import date, datetime
from typing import Union


class Birthday(Field):
    """Represents a birthday field and ensures valid date format."""

    def __init__(self, date_of_birth: str):
        formatted_date = self.get_formatted_date(date_of_birth)
        if formatted_date:
            super().__init__(formatted_date)
        else:
            raise ValueError("Invalid date format stored in Birthday object.")

    @staticmethod
    def get_formatted_date(date_of_birth: str) -> Union[date, None]:
        """Formats the birthday as a date object using the provided format code.
        Args:
            date_of_birth (str): The date of birth in DD.MM.YYYY format.
        Returns:
            Union[date, None]: The formatted date object or None if the format is invalid.
        """
        try:
            return datetime.strptime(date_of_birth, '%d.%m.%Y').date()
        except ValueError:
            return None