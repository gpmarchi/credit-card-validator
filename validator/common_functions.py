from validator.issuing_network import IssuingNetwork
from validator.industry_identifier import IndustryIdentifier


def is_valid_number_in_string(number):
    if type(number) is not str:
        raise TypeError("Card number must be a string representation of the number.")
    elif not number.isdigit():
        raise ValueError(
            "The string representation of the card number must contain only digits."
        )


def issuing_network_json_object_decoder(json_object):
    return IssuingNetwork(
        json_object["Issuing network"],
        json_object["IIN ranges"],
        json_object["Active"],
        json_object["Length"],
        json_object["Validation"],
    )


def industry_identifier_json_object_decoder(json_object):
    return IndustryIdentifier(
        json_object["MII digit value"], json_object["Issuer category"]
    )


def get_trimmed_split_strings(string_to_split, delimiter):
    split_strings = string_to_split.split(delimiter)
    trimmed_split_strings = []
    for string in split_strings:
        trimmed_split_strings.append(string.strip())
    return trimmed_split_strings


def get_boolean_from_string(string):
    return string.lower() == "yes"
