# Credit Card Validator

![GitHub issues](https://img.shields.io/github/issues-raw/gpmarchi/credit-card-validator)
![GitHub last commit](https://img.shields.io/github/last-commit/gpmarchi/credit-card-validator)
![GitHub](https://img.shields.io/github/license/gpmarchi/credit-card-validator)

## Table of Contents

- [About the project](#about-the-project)
- [Reference](#reference)
- [Usage](#usage)

## About the Project

This project was developed in Python as a means for me to learn a bit more about the language.
The idea initially was to make a simple credit card validator library to be published in [PyPi](https://pypi.org/). Then I decided to add some webscrapping capabilities to the library, so all the data for validating the cards and telling from which company and market sector they were emitted are comming from Wikipedia.

This library is still an evolving personal project as I'm planning on adding some more features to it. There's the issue of it needing a fallback in case something goes wrong with the Wikipedia scrape, and also making it available via a REST API using Django. After those previous ideas are done, I'll probably develop an webapp made with React to make the validator available on the web.

## Reference

Credit card numbers are logically composed as demonstrated below:

[example-card]: https://miro.medium.com/max/460/0*2sYEHfIj5UHkF3CI

![Card number subdivisions][example-card]

> Image extracted from article: [_A Comprehensive Guide to Validating and Formatting Credit Cards_][1]
>
> by **Kelvin Zhang**

[1]: https://medium.com/hootsuite-engineering/a-comprehensive-guide-to-validating-and-formatting-credit-cards-b9fa63ec7863

**1.** Major Industry Identifier (MII) - some description

**2.** Issuer Identification Number (IIN) - some description

**3.** Account Number - some description

**4.** Checksum - some description

This project goes a little bit further and scrapes information from
[_Wikipedia_](<https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)>)
about the Issuer Identification Number (IIN), the Major Industry Identifier (MII) and feeds it to the validator.

This enables the validator to be always up to date with current valid IIN ranges
from active issuing companies, as well as their card number lengths.

Therefore, it is possible for the library to correctly identify the issuer of the card and also display other relevant information regarding the card being validated.

Card numbers are validated using the [_Luhn algorithm_](https://en.wikipedia.org/wiki/Luhn_algorithm#Implementation_examples).

## Usage

Here goes the class descriptions and some code examples of how to use the library.

Also info about the REST API and usage as well.
