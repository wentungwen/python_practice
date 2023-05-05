import requests
import os




class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_endpoint = os.environ.get("TEQUILA_ENDPOINT")

    def get_lowest_price(self, iata_code):
        header = {"apikey": os.environ.get("TEQUILA_API")}
        search_params = {
            "fly_from": "city:LON",
            "fly_to": f"city:{iata_code}",
            "date_from": "01/04/2023",
            "date_to": "02/06/2023",
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        res = requests.get(url=f"{self.flight_endpoint}/v2/search?", params=search_params, headers=header)
        data = res.json()["data"]
        lowest_price = data[0]["price"]
        return lowest_price
