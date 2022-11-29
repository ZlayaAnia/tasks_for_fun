import unicodedata

import requests
from bs4 import BeautifulSoup


class PatternParser:

    URL = "https://refactoring.guru/design-patterns/"

    def get_data_from_url(self, url):
        request_pattern_name = requests.get(url).text
        return BeautifulSoup(request_pattern_name, features="html.parser")

    def list_pattern(self):
        url = f"{self.URL}catalog"
        bs_pattern_name = self.get_data_from_url(url)
        data_pattern_name = bs_pattern_name.findAll("span", class_="pattern-name")

        return [pat_name.text for pat_name in data_pattern_name]

    def pattern_info(self, pattern_name):
        pattern_url = f"{self.URL}{pattern_name.lower()}"
        request_pattern_info = requests.get(pattern_url).text
        bs_pattern_info = BeautifulSoup(request_pattern_info, features="html.parser")
        if pattern_info := bs_pattern_info.find("div", class_="section intent"):
            info = pattern_info.text.replace("Intent", "")
            return unicodedata.normalize("NFKD", info).strip()
        else:
            print(
                "This pattern is not on the site, try with other names. Available names can be"
                " obtained with PatternParser.list_pattern()"
            )
