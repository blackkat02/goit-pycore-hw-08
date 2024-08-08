from functools import wraps


class InputError(Exception):
    pass

    def input_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Invalid input. Please check the format and try again."
            except KeyError:
                return "Contact not found."
            except IndexError:
                return "Insufficient arguments provided."
            except InputError as e:
                return str(e)
        return wrapper