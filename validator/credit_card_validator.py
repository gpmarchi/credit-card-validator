from webscraper.webscraper import WebScraper
import validator.exceptions as exceptions
import validator.common_functions as commons


class CreditCardValidator:
    def __init__(self):
        self.__webscraper = WebScraper()
        self.__webscraper.fetch_iin_table_into_json_object()
        self.__issuing_networks = self.__webscraper.get_issuing_networks()

        self.__webscraper.fetch_mii_table_into_json_object()
        self.__industry_identifiers = self.__webscraper.get_industry_identifiers()

    def is_card_valid(self, credit_card):

        card_number = credit_card.get_card_number()
        sum_of_digits = 0

        for index, string_digit in enumerate(card_number[::-1], start=1):
            digit = int(string_digit)

            if index % 2 == 0:
                doubled_digit = digit * 2
                if doubled_digit > 9:
                    sum_of_digits += doubled_digit - 9
                else:
                    sum_of_digits += doubled_digit
            else:
                sum_of_digits += digit

        return sum_of_digits % 10 == 0

    def get_card_issuer(self, credit_card):
        if not self.is_card_valid(credit_card):
            raise exceptions.InvalidCreditCardError(
                "Unable to extract card issuer. Invalid card number informed."
            )

        card_issuer_id_number = credit_card.get_issuer_identification_number()

        for issuing_network in self.__issuing_networks:
            iin_ranges = issuing_network.get_iin_ranges()
            for iin_range in iin_ranges:
                if self.__is_card_issuer_in_iin_range(card_issuer_id_number, iin_range):
                    return issuing_network.get_issuing_network()

    def __is_card_issuer_in_iin_range(self, card_issuer_id_number, iin_range):
        if commons.is_composite_range("-", iin_range):
            iin_range_limits = commons.get_trimmed_split_strings(iin_range, "-")
            iin_range_inferior_limit = iin_range_limits[0]
            iin_range_superior_limit = iin_range_limits[1]
            # get length of any limit since they are the same
            iin_range_limit_length = len(iin_range_inferior_limit)
            return (
                int(iin_range_inferior_limit)
                <= int(card_issuer_id_number[0:iin_range_limit_length])
                <= int(iin_range_superior_limit)
            )
        return card_issuer_id_number[0 : len(iin_range)] in iin_range

    def get_issuer_category(self, credit_card):
        if not self.is_card_valid(credit_card):
            raise exceptions.InvalidCreditCardError(
                "Unable to extract industry type. Invalid card number informed."
            )

        card_major_id_number = credit_card.get_major_industry_identifier()

        for industry_identifier in self.__industry_identifiers:
            industry_id_digit = industry_identifier.get_industry_identifier_digit()
            if industry_id_digit == int(card_major_id_number):
                return industry_identifier.get_issuer_category()
