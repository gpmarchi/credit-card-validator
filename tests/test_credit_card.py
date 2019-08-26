import unittest
from validator.credit_card import CreditCard


class TestCreditCard(unittest.TestCase):

    __VISA_TEST_CARD_1 = CreditCard("4197631477853706")

    def test_get_major_industry_identifier(self):
        self.assertEqual("4", self.__VISA_TEST_CARD_1.get_major_industry_identifier())

    def test_get_issuer_identification_number(self):
        self.assertEqual(
            "419763", self.__VISA_TEST_CARD_1.get_issuer_identification_number()
        )

    def test_get_account_number(self):
        self.assertEqual("147785370", self.__VISA_TEST_CARD_1.get_account_number())

    def test_get_checksum(self):
        self.assertEqual("6", self.__VISA_TEST_CARD_1.get_checksum())

    def test_get_card_number(self):
        self.assertEqual("4197631477853706", self.__VISA_TEST_CARD_1.get_card_number())
