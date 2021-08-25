import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents a temperature value extracted from the timeanddate.com/weather webpage.
    """

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 '
                      'Safari/537.36 ',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'accept-language': 'en-GB,en-Us;q=0.9;q=0.8'
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """Extracts a value as instructed by the yml file and returns a dictionary"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """leans the output of _scrape"""
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())


if __name__ == "__main__":
    temperature = Temperature(country="ethiopia", city="addis-ababa")
    print(temperature.get())
