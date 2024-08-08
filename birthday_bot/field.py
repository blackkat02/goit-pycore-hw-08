class Field:
    def __init__(self, value):
        """
        Initializes a Field object with the given value.
        Args:
            value: The value to store in the field.
        """
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the field value.
        Returns:
            The string representation of the field value.
        """
        return str(self.value)
