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

    ##### Deals User and Provider API ######

    def query_get_deal_types(self) -> list:
        """Function to get existing deal types
        Returns:
            list: list of deal types
        """
        query = "http://api.stb.gov.sg/content/deals/v2/types"
        response = requests.get(query, headers=self.headers)
        jsonResponse = response.json()
        deal_types = []
        for res in jsonResponse["data"]:
            deal_types.append(res["name"])

        return deal_types

    ##### Content User API ######

    def list_content(self) -> list:
        """Function to get list of content categories
        Returns:
            list: list of content categories
        """
        query = "https://api.stb.gov.sg/content/common/v2/datasets"
        jsonResponse = requests.get(query, headers=self.headers).json()
        content_types = []
        for res in jsonResponse["data"]:
            content_types.append(res)

        return content_types

    def list_content_types(self, category: str) -> list:
        """Function to get a list of attraction types within the content category
        Args:
            category (str): content categories: accommodation, attractions,
                            bars_clubs, cruises, events, food_beverages, precincts,
                            shops, tours, venues, walking_trails
        Returns:
            list: list of content categories types
        """
        category = category.strip().replace(" ", "%20")
        query = f"http://api.stb.gov.sg/content/common/v2/types?category={category}"

        response = requests.get(query, headers=self.headers)
        jsonResponse = response.json()
        content_types = []
        for res in jsonResponse["data"]:
            content_types.append(res)

        return content_types

    def query_by_keywords_or_uuid(
        self, content=str, uuid: Optional[str] = None, keyword: Optional[str] = None
    ):
        """content: [accommodation | attractions | bars-clubs | cruises | events | food-beverages | precincts | shops | tours | venues | walking-trails]."""
        if uuid is not None:
            return self.query_by_uuid(content, uuid)
        else:
            return self.query_by_keywords(content, keyword)

    def query_by_keywords(self, content=str, keyword: Optional[str] = None):
        """query_by_keywords _summary_
        Args:
            content (_type_, optional): _description_. Defaults to str.
            keyword (Optional[str], optional): _description_. Defaults to None.
        Returns:
            TypeJSON: _description_
        """
        keyword = keyword.strip().replace(" ", "%20")
        query = f"https://api.stb.gov.sg/content/{content}/v2/search?searchType=keyword&searchValues={keyword}"
        response = requests.get(query, headers=self.headers)
        jsonResponse = response.json()

        return jsonResponse

    def query_by_uuid(self, content=str, uuid: Optional[str] = None):
        """query_by_uuid _summary_
        Args:
            content (_type_, optional): _description_. Defaults to str.
            uuid (Optional[str], optional): _description_. Defaults to None.
        Returns:
            TypeJSON: _description_
        """
        query = f"https://api.stb.gov.sg/content/{content}/v2/details/{uuid}"
        response = requests.get(query, headers=self.headers)
        jsonResponse = response.json()

        return jsonResponse


if __name__ == "__main__":
    dealtype = ApiFunctions("en").query_get_deal_types()
    trail_detail = ApiFunctions("en").query_walking_trail_details_by_uuid(
        "00944ba2370b7ac488fbe01d2e8aa1baa3a"
    )

    print(trail_detail)
    # ApiFunctions().read_json()
