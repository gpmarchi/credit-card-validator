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

        with urllib.request.urlopen(
            "https://en.wikipedia.org/wiki/ISO/IEC_7812#Major_industry_identifier"
        ) as url:
            mii_page = url.read()

        self.__iin_html_parser = BeautifulSoup(iin_page, "html.parser")
        self.__iin_json_object = None

        self.__mii_html_parser = BeautifulSoup(mii_page, "html.parser")
        self.__mii_json_object = None

    def fetch_iin_table_into_json_object(self):
        html_tables = self.__iin_html_parser.find_all("table")

        general_iin_table = html_tables[0]
        # TODO: deal with canada specific iin table
        # canada_iin_table = html_tables[1]

        iin_data_frame = pandas.read_html(str(general_iin_table))[0]

        # regex for removing cross references and any notes inside parentheses
        iin_data_frame.replace(r"\[\d+\]|\(([^()]+)\)", "", inplace=True, regex=True)
        # regex for removing unicode character '–' and replacing with '-'
        iin_data_frame.replace(r"–| - ", "-", inplace=True, regex=True)
        # regex for removing any numbers from 'Active' column
        iin_data_frame.replace({"Active": {r" *[\d]": ""}}, inplace=True, regex=True)

        self.__iin_json_object = iin_data_frame.to_json(orient="records")

    def fetch_mii_table_into_json_object(self):
        mii_html_table = self.__mii_html_parser.find("table")
        mii_data_frame = pandas.read_html(str(mii_html_table))[0]
        self.__mii_json_object = mii_data_frame.to_json(orient="records")

    def get_issuing_networks(self):
        issuing_networks = json.loads(
            self.__iin_json_object,
            object_hook=commons.issuing_network_json_object_decoder,
        )
        return issuing_networks

    def get_industry_identifiers(self):
        industry_identifiers = json.loads(
            self.__mii_json_object,
            object_hook=commons.industry_identifier_json_object_decoder,
        )
        return industry_identifiers

    def get_iin_json_object(self):
        return self.__iin_json_object

    def get_mii_json_object(self):
        return self.__mii_json_object
