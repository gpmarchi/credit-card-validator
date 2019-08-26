from webscraper.webscraper import WebScraper
import validator.exceptions as exceptions
import validator.common_functions as commons


class CreditCardValidator:
    def __init__(self):
        self.__webscraper = WebScraper()
        self.__webscraper.fetch_iin_table_into_json_object()
        self.__issuing_networks = self.__webscraper.get_list_of_issuing_networks()

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

                if "-" in iin_range:

                    iin_range_limits = commons.get_trimmed_split_strings(iin_range, "-")
                    iin_range_inferior_limit = iin_range_limits[0]
                    iin_range_superior_limit = iin_range_limits[1]
                    iin_range_limit_length = len(iin_range_limits[0])

                    if (
                        int(iin_range_inferior_limit)
                        <= int(card_issuer_id_number[0:iin_range_limit_length])
                        <= int(iin_range_superior_limit)
                    ):
                        return issuing_network.get_issuing_network()

                elif iin_range in card_issuer_id_number[0 : len(iin_range)]:

                    return issuing_network.get_issuing_network()

    def get_industry_type(self, credit_card):
        pass

    def get_account_number(self, credit_card):
        pass
