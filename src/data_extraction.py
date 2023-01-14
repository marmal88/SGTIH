import os
import requests
import json
from dotenv import load_dotenv


class ApiFunctions:
    def __init__(self):
        load_dotenv()
        self.apikey = os.getenv("API_KEY")

    def query_get_deal_types(self, language):
        headers = {
            "Content-Type": "application/json",
            "X-Content-Language": language,
            "X-API-Key": self.apikey,
        }
        query = "http://api.stb.gov.sg/content/deals/v2/types"
        output_json = requests.get(query, headers=headers).json()
        with open("data.json", "w") as f:
            json.dump(output_json, f)

    def read_json(self):
        output = json.load("data.json")
        print(output.data)


if __name__ == "__main__":
    ApiFunctions().query_get_deal_types(language="en")
    ApiFunctions().read_json()
