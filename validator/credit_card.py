import validator.common_functions as commons


class CreditCard:
    def __init__(self, card_number=""):
        commons.is_valid_number_in_string(card_number)
        self.__card_number = card_number

    def get_major_industry_identifier(self):
        return self.__card_number[0]

    def get_issuer_identification_number(self):
        return self.__card_number[0:5]

    def get_account_number(self):
        return self.__card_number[6:-2]

    def get_checksum(self):
        return self.__card_number[-1]

    def get_card_number(self):
        return self.__card_number
