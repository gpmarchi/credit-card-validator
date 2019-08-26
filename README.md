# Credit Card Validator

## Simple credit card validator in Python

![GitHub issues](https://img.shields.io/github/issues-raw/gpmarchi/credit-card-validator)
![GitHub last commit](https://img.shields.io/github/last-commit/gpmarchi/credit-card-validator)
![GitHub](https://img.shields.io/github/license/gpmarchi/credit-card-validator)

Credit card numbers are logically composed as demonstrated below:

[example-card]: https://miro.medium.com/max/460/0*2sYEHfIj5UHkF3CI

![alt text][example-card]

> Image extracted from article: <cite>[_A Comprehensive Guide to Validating and Formatting Credit Cards_][1]<cite>
>
> by **Kelvin Zhang**

[1]:https://medium.com/hootsuite-engineering/a-comprehensive-guide-to-validating-and-formatting-credit-cards-b9fa63ec7863

**1.** Major Industry Identifier (MII)

**2.** Issuer Identification Number (IIN)

**3.** Account Number

**4.** Checksum

This project goes a little bit further and scrapes information from
[_Wikipedia_](https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN))
about the Issuer Identification Number (IIN), and feeds it to the validator.

This enables the validator to be always up to date with current valid IIN ranges
from active issuing companies, as well as their card number lengths.

Therefore, it is possible for the library to correctly identify the issuer of the card and also display other relevant information regarding the card being validated.

Card numbers are validated using the [_Luhn algorithm_](https://en.wikipedia.org/wiki/Luhn_algorithm#Implementation_examples).
