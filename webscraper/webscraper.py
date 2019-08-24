import urllib.request
import pandas
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        pandas.set_option("display.max_columns", 5)

        with urllib.request.urlopen(
            "https://en.wikipedia.org/wiki/Payment_card_number#\
            Issuer_identification_number_(IIN)"
        ) as url:
            iin_page = url.read()

        self.__html_parser = BeautifulSoup(iin_page, "html.parser")

    def extract_iin_table(self):
        html_tables = self.__html_parser.find_all("table")
        iin_table = html_tables[0]
        canada_iin_table = html_tables[1]

        iin_data_frame = pandas.read_html(str(iin_table))[0]
        iin_data_frame.replace("\[\d+\]|\(([^()]+)\)", "", inplace=True, regex=True)
        print("\n" + str(iin_data_frame))
