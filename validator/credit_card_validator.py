class CreditCardValidator:
    def is_card_valid(self, card):

        card_number = card.get_card_number()
        index = 1
        sum_of_digits = 0

        for string_digit in card_number[::-1]:
            digit = int(string_digit)

            if index % 2 == 0:
                doubled_digit = digit * 2
                if doubled_digit > 9:
                    sum_of_digits += doubled_digit - 9
                else:
                    sum_of_digits += doubled_digit
            else:
                sum_of_digits += digit

            index += 1

        return sum_of_digits % 10 == 0
