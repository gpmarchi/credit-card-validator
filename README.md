# credit-card-validator

## Simple credit card validator

This project scrapes information from
[Wikipedia](https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN))
about the Issuer Identification Number (IIN) and feeds it to the validator
using JSON.

This enables the validator to always be up to date with current valid IIN ranges
from active issuing companies, as well as their cards lengths.

The cards are validated using the Luhn algorithm.
