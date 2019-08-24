def is_valid_number_in_string(number):
    if type(number) is not str:
        raise TypeError("Card number must be a string representation of the number.")
    elif not number.isdigit():
        raise ValueError(
            "The string representation of the card number must contain only digits."
        )
