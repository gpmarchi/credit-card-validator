import unittest
import json
from webscraper.webscraper import WebScraper
from validator.issuing_network import IssuingNetwork
from validator.industry_identifier import IndustryIdentifier


class TestWebScraper(unittest.TestCase):

    __ISSUING_NETWORK_TEST = IssuingNetwork(
        "American Express", "34, 37", "Yes", "15", "Luhn algorithm"
    )

    __INDUSTRY_IDENTIFIER_TEST = IndustryIdentifier(
        0, "ISO/TC 68 and other industry assignments"
    )

    def test_fetch_iin_table_into_json_object(self):
        webscraper = WebScraper()
        webscraper.fetch_iin_table_into_json_object()
        json_iin_dict = json.loads(webscraper.get_iin_json_object())

        self.assertEqual("American Express", json_iin_dict[0]["Issuing network"])
        self.assertEqual("34, 37", json_iin_dict[0]["IIN ranges"])
        self.assertEqual("Yes", json_iin_dict[0]["Active"])
        self.assertEqual("15", json_iin_dict[0]["Length"])
        self.assertEqual("Luhn algorithm", json_iin_dict[0]["Validation"])

        self.assertEqual(29, len(json_iin_dict))

    def test_fetch_mii_table_into_json_object(self):
        webscraper = WebScraper()
        webscraper.fetch_mii_table_into_json_object()
        json_mii_dict = json.loads(webscraper.get_mii_json_object())

        self.assertEqual(0, json_mii_dict[0]["MII digit value"])
        self.assertEqual(
            "ISO/TC 68 and other industry assignments",
            json_mii_dict[0]["Issuer category"],
        )

        self.assertEqual(10, len(json_mii_dict))

    def test_get_issuing_networks(self):
        webscraper = WebScraper()
        webscraper.fetch_iin_table_into_json_object()
        issuing_networks = webscraper.get_issuing_networks()

        self.assertEqual(self.__ISSUING_NETWORK_TEST, issuing_networks[0])
        self.assertEqual(29, len(issuing_networks))

    def test_get_industry_identifiers(self):
        webscraper = WebScraper()
        webscraper.fetch_mii_table_into_json_object()
        industry_identifiers = webscraper.get_industry_identifiers()

        self.assertEqual(self.__INDUSTRY_IDENTIFIER_TEST, industry_identifiers[0])
        self.assertEqual(10, len(industry_identifiers))
