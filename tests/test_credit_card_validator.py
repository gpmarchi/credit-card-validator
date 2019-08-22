import unittest
from validator.credit_card import CreditCard
from validator.credit_card_validator import CreditCardValidator


class TestCreditCardValidator(unittest.TestCase):

    __VISA_TEST_CARD_1 = CreditCard("4197631477853706")
    __VISA_TEST_CARD_2 = CreditCard("4853452052738542")
    __VISA_TEST_CARD_3 = CreditCard("4277906607581770")
    __VISA_TEST_CARD_4 = CreditCard("4374401171267578")
    __VISA_TEST_CARD_5 = CreditCard("4145145886714213")

    __AMEX_TEST_CARD_1 = CreditCard("342635314219791")
    __AMEX_TEST_CARD_2 = CreditCard("375686152388115")
    __AMEX_TEST_CARD_3 = CreditCard("376930245139765")
    __AMEX_TEST_CARD_4 = CreditCard("342154711836553")
    __AMEX_TEST_CARD_5 = CreditCard("342315999177277")

    def test_is_card_valid(self):
        self.assertTrue(CreditCardValidator().is_card_valid(self.__VISA_TEST_CARD_1))
        self.assertTrue(CreditCardValidator().is_card_valid(self.__VISA_TEST_CARD_2))
        self.assertTrue(CreditCardValidator().is_card_valid(self.__VISA_TEST_CARD_3))
        self.assertTrue(CreditCardValidator().is_card_valid(self.__VISA_TEST_CARD_4))
        self.assertFalse(CreditCardValidator().is_card_valid(self.__VISA_TEST_CARD_5))

        self.assertTrue(CreditCardValidator().is_card_valid(self.__AMEX_TEST_CARD_1))
        self.assertTrue(CreditCardValidator().is_card_valid(self.__AMEX_TEST_CARD_2))
        self.assertTrue(CreditCardValidator().is_card_valid(self.__AMEX_TEST_CARD_3))
        self.assertTrue(CreditCardValidator().is_card_valid(self.__AMEX_TEST_CARD_4))
        self.assertFalse(CreditCardValidator().is_card_valid(self.__AMEX_TEST_CARD_5))


if __name__ == "__main__":
    unittest.main()
