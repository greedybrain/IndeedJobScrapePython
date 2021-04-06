from bs4 import BeautifulSoup
import requests

from url_build import URLBuild


class JobScraper:
    __URL = URLBuild.get_url()
    all_cards = []

    # private
    @classmethod
    def __get_data_document(cls, url):
        return BeautifulSoup(requests.get(url).content, 'html.parser')

    # private
    @classmethod
    def __job_cards_from(cls, data):
        job_cards = data.find_all("div", class_="jobsearch-SerpJobCard")
        for card in job_cards:
            cls.all_cards.append(card)

    @classmethod
    def get_job_cards_for_each_page(cls):
        data_doc = cls.__get_data_document(cls.__URL)
        cls.__job_cards_from(data_doc)
        if cls.__contains_pagination(data_doc):
            pagination_list = data_doc.select("div.pagination ul.pagination-list li a")
            for page in pagination_list:
                complete_link = f"""https://www.indeed.com/${page.find("a").get("href")}"""
                data_doc = cls.__get_data_document(complete_link)
                cls.__job_cards_from(data_doc)

        return cls.all_cards

    @classmethod
    def __contains_pagination(cls, data):
        return data.find_all("*", class_="pagination") or data.find_all("*", class_="pagination-list")
