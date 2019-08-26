import unittest
from webscraper.webscraper import WebScraper


class TestWebScraper(unittest.TestCase):
    def test_fetch_iin_table_into_json_object(self):
        WebScraper().fetch_iin_table_into_json_object()

    def test_get_list_of_issuing_networks(self):
        webscraper = WebScraper()
        webscraper.fetch_iin_table_into_json_object()
        webscraper.get_list_of_issuing_networks()
