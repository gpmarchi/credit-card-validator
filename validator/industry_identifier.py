class IndustryIdentifier:
    def __init__(self, industry_identifier_digit, issuer_category):
        self.__industry_identifier_digit = industry_identifier_digit
        self.__issuer_category = issuer_category

    def __str__(self):
        return (
            "MII digit value: " + str(self.__industry_identifier_digit) + "\n"
            "Issuer category: " + self.__issuer_category + "\n"
        )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if (
                self.__industry_identifier_digit == other.__industry_identifier_digit
                and self.__issuer_category == other.__issuer_category
            ):
                return True

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_industry_identifier_digit(self):
        return self.__industry_identifier_digit

    def get_issuer_category(self):
        return self.__issuer_category
