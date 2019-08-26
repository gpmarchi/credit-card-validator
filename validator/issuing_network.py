import validator.common_functions as commons


class IssuingNetwork:
    def __init__(self, issuing_network, iin_ranges, is_active, card_length, validation):
        self.__issuing_network = issuing_network
        self.__iin_ranges = commons.get_trimmed_split_strings(iin_ranges, ",")
        self.__is_active = commons.get_boolean_from_string(is_active)
        self.__card_length = card_length
        self.__validation = validation

    def __str__(self):
        return (
            "Issuing Network: " + self.__issuing_network + "\n"
            "IIN ranges: " + str(self.__iin_ranges) + "\n"
            "Is Active: " + str(self.__is_active) + "\n"
            "Card Length: " + self.__card_length + "\n"
            "Validation: " + (self.__validation or "no validation") + "\n"
        )

    def get_issuing_network(self):
        return self.__issuing_network

    def get_iin_ranges(self):
        return self.__iin_ranges

    def get_acrive(self):
        return self.__is_active

    def get_length(self):
        return self.__card_length

    def get_validation(self):
        return self.__validation
