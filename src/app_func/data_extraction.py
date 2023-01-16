import os
import requests
import json
from dotenv import load_dotenv
from typing import Optional
import pandas as pd


class ApiFunctions:
    def __init__(self, language: str):
        load_dotenv()
        apikey = os.getenv("API_KEY")
        self.headers = {
            "Content-Type": "application/json",
            "X-Content-Language": language,
            "X-API-Key": apikey,
        }

    def query_get_deal_types(self) -> list:
        query = "http://api.stb.gov.sg/content/deals/v2/types"
        response = requests.get(query, headers=self.headers)
        jsonResponse = response.json()
        dealtypes = []
        for res in jsonResponse["data"]:
            dealtypes.append(res["name"])

        return dealtypes

    # def query_walking_trail_details_by_keywords_or_uuid(
    #     self, uuid: Optional[str] = None, keyword: Optional[str] = None
    # ):
    #     if uuid is not None:
    #         self.query_walking_trail_details_by_uuid(uuid)
    #     query = f"https://api.stb.gov.sg/content/walking-trails/v2/search{}"
    #     '/content/walking-trails/v2/search?searchType=keyword&searchValues=west%20coast HTTP/1.1'
    #     response = requests.get(query, headers=headers)
    #     jsonResponse = response.json()
    #     dealtypes = []

    def query_walking_trail_details_by_uuid(self, uuid: Optional[str] = None):

        query = f"https://api.stb.gov.sg/content/walking-trails/v2/details/{uuid}"
        response = requests.get(query, headers=self.headers)
        jsonResponse = response.json()
        # print(jsonResponse["data"])
        # with open("data.json", "w") as f:
        #     json.dump(jsonResponse["data"], f)

        # df = pd.read_json(jsonResponse["data"], orient="index")
        # print(df.head())
        return jsonResponse

    def query_deals_by_poi(self):
        output = json.load("data.json")
        print(output.data)
        pass


if __name__ == "__main__":
    dealtype = ApiFunctions("en").query_get_deal_types()
    trail_detail = ApiFunctions("en").query_walking_trail_details_by_uuid(
        "00944ba2370b7ac488fbe01d2e8aa1baa3a"
    )

    print(trail_detail)
    # ApiFunctions().read_json()
