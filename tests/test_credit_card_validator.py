import unittest

import validator.exceptions as exceptions
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

    __MASTER_TEST_CARD_1 = CreditCard("5148750950511412")
    __MASTER_TEST_CARD_2 = CreditCard("5335912905851409")
    __MASTER_TEST_CARD_3 = CreditCard("5437299977416387")
    __MASTER_TEST_CARD_4 = CreditCard("5457000166519956")
    __MASTER_TEST_CARD_5 = CreditCard("5205870067211175")

    __DISCOVER_TEST_CARD_1 = CreditCard("6011545267432266")
    __DISCOVER_TEST_CARD_2 = CreditCard("6011116706486626")
    __DISCOVER_TEST_CARD_3 = CreditCard("6011879468332664")
    __DISCOVER_TEST_CARD_4 = CreditCard("6011135436826372")
    __DISCOVER_TEST_CARD_5 = CreditCard("6011894516615358")

    __JCB_TEST_CARD_1 = CreditCard("3589383466738302")
    __JCB_TEST_CARD_2 = CreditCard("3578607623466438")
    __JCB_TEST_CARD_3 = CreditCard("3538102016385170")
    __JCB_TEST_CARD_4 = CreditCard("3569114675641340")
    __JCB_TEST_CARD_5 = CreditCard("3548805774982008")

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

    def test_get_card_issuer(self):
        self.assertRaises(
            exceptions.InvalidCreditCardError,
            CreditCardValidator().get_card_issuer,
            self.__VISA_TEST_CARD_5,
        )

        self.assertEqual(
            "Visa", CreditCardValidator().get_card_issuer(self.__VISA_TEST_CARD_1)
        )
        self.assertEqual(
            "American Express",
            CreditCardValidator().get_card_issuer(self.__AMEX_TEST_CARD_1),
        )
        self.assertEqual(
            "Mastercard",
            CreditCardValidator().get_card_issuer(self.__MASTER_TEST_CARD_1),
        )
        self.assertEqual(
            "Discover Card",
            CreditCardValidator().get_card_issuer(self.__DISCOVER_TEST_CARD_1),
        )
        self.assertEqual(
            "JCB", CreditCardValidator().get_card_issuer(self.__JCB_TEST_CARD_1)
        )
