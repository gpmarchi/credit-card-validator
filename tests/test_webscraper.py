import unittest
from webscraper.webscraper import WebScraper


class TestWebScraper(unittest.TestCase):
    def test_extract_iin_table(self):
        WebScraper().extract_iin_table()
