from bs4 import BeautifulSoup

import validator.common_functions as commons
import urllib.request
import pandas
import json


class WebScraper:
    def __init__(self):
        with urllib.request.urlopen(
            "https://en.wikipedia.org/wiki/Payment_card_number#\
            Issuer_identification_number_(IIN)"
        ) as url:
            iin_page = url.read()

        self.__html_parser = BeautifulSoup(iin_page, "html.parser")
        self.__iin_json_object = None

    def fetch_iin_table_into_json_object(self):
        html_tables = self.__html_parser.find_all("table")

        general_iin_table = html_tables[0]
        # TODO: deal with canada specific iin table
        # canada_iin_table = html_tables[1]

        iin_data_frame = pandas.read_html(str(general_iin_table))[0]

        # regex for removing cross references and any notes inside parentheses
        iin_data_frame.replace("\[\d+\]|\(([^()]+)\)", "", inplace=True, regex=True)
        # regex for removing unicode character '–' and replacing with '-'
        iin_data_frame.replace("–| - ", "-", inplace=True, regex=True)
        # regex for removing any numbers from 'Active' column
        iin_data_frame.replace({"Active": {" *[\d]": ""}}, inplace=True, regex=True)

        self.__iin_json_object = iin_data_frame.to_json(orient="records")

    def get_list_of_issuing_networks(self):
        issuing_networks = json.loads(
            self.__iin_json_object,
            object_hook=commons.issuing_network_json_object_decoder,
        )

        for iin in issuing_networks:
            print(iin)

        return issuing_networks
