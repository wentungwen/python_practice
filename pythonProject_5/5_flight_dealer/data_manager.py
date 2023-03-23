import os
import requests
import flight_search as fs

tequila_header = {
    "apikey": os.environ.get("TEQUILA_API")
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_api = os.environ.get("TEQUILA_API")
        self.flight_endpoint = os.environ.get("TEQUILA_ENDPOINT")
        self.sheety_url = os.environ.get("SHEETY_URL")
        self.city_dict = {}

    def write_to_sheety(self):
        """ Read the city_list and write the IATA code to sheety """
        self.get_sheety_data()
        for idx, key in enumerate(self.city_dict):
            iata_params = {
                "term": key,
                "location_types": "city"
            }
            res = requests.get(url=f"{self.flight_endpoint}/locations/query?",
                               params=iata_params, headers=tequila_header)
            flight_code = res.json()["locations"][0]["code"]

            flight_data = fs.FlightSearch()
            lowest_price = flight_data.get_lowest_price(flight_code)
            lowest_price_sheety = self.city_dict[key]
            if self.if_price_lower(lowest_price, lowest_price_sheety):
                print(f"The lowest price of {key} now is {lowest_price} which is lower than {lowest_price_sheety}")

            self.write_iata_to_sheety(key, flight_code, idx)

    def write_iata_to_sheety(self, key, flight_code, idx):
        sheety_data = {
            "price": {
                "city": key,
                "code": flight_code
            }
        }
        res = requests.put(url=f"{self.sheety_url}/{idx + 2}", json=sheety_data)

    def get_sheety_data(self):
        """ update sheety data"""
        res = requests.get(url=self.sheety_url)
        cities_data = res.json()["prices"]
        self.city_dict = {n["city"]: n["lowest"] for n in cities_data}

    def if_price_lower(self, lowest_price, city_dict):
        """ Return true while the price is lower """
        if lowest_price < city_dict:
            return True
        # self.city_dict = berlin:2
