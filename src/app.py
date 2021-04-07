import re
from bs4 import BeautifulSoup
import requests


class CLI:
    @classmethod
    def get_job_title(cls):
        job_title = ""

        while not job_title or re.match(".*\\d+.*", job_title):
            job_title = input("Job title: ")
        else:
            return job_title

    @classmethod
    def get_desired_salary(cls):
        desired_salary = ""

        while not desired_salary:
            desired_salary = input("Desired salary: ")
            if not desired_salary:
                print("Desired salary required!")
        else:
            return desired_salary

    @classmethod
    def get_location(cls):
        location = ""

        while not location:
            location = input("Location: ")
            if not location:
                print("Location required!")
        else:
            return location

    @classmethod
    def get_radius(cls):
        print("""
            1. within 5 miles
            2. within 10 miles
            3. within 15 miles
            4. within 25 miles
            5. within 50 miles
            6. within 100 miles
            """)

        radius = int(input("Choose number representing your preferred radius (Optional - enter 0 to skip): "))

        if radius == 1:
            return "5"
        elif radius == 2:
            return "10"
        elif radius == 3:
            return "15"
        elif radius == 4:
            return "25"
        elif radius == 5:
            return "50"
        elif radius == 6:
            return "100"
        else:
            return ""

    @classmethod
    def get_job_type(cls):
        print("""
            1. Part-time
            2. Full-time
            """)

        job_type = int(input("Choose number representing the job type (Optional - enter 0 to skip): "))

        if job_type == 1:
            return "parttime"
        elif job_type == 2:
            return "fulltime"
        else:
            return ""

    @classmethod
    def get_exp_level(cls):
        print("""
            1. Entry level
            2. Mid level
            3. Senior level
            """)

        exp_level = int(input("Choose the number representing the experience level (Optional - enter 0 to skip): "))

        if exp_level == 1:
            return "entry_level"
        elif exp_level == 2:
            return "mid_level"
        elif exp_level == 3:
            return "senior_level"
        else:
            return ""

    @classmethod
    def get_date_posted(cls):
        print("""
            1. Last 24 hours
            2. Last 3 days
            3. Last 7 days
            4. Last 14 days
            """)

        date_posted = int(input("Date posted (Optional - enter 0 to skip): "))
        print(date_posted
              )

        if date_posted == 1:
            return "1"
        elif date_posted == 2:
            return "3"
        elif date_posted == 3:
            return "7"
        elif date_posted == 4:
            return "14"
        else:
            return ""

    @classmethod
    def run(cls):
        Jobs.list_jobs()


"""========================================================================="""


class URLBuild:
    __get_job_title = CLI.get_job_title()
    __get_desired_salary = CLI.get_desired_salary()
    __get_location = CLI.get_location()
    __get_radius = CLI.get_radius()
    __get_job_type = CLI.get_job_type()
    __get_exp_level = CLI.get_exp_level()
    __get_date_posted = CLI.get_date_posted()

    def __init__(self, job_title, desired_salary, location, radius, job_type, exp_level, date_posted):
        self.__job_title = job_title
        self.__desired_salary = desired_salary
        self.__location = location
        self.__radius = radius
        self.__job_type = job_type
        self.__exp_level = exp_level
        self.__date_posted = date_posted

    def then_build_url(self):
        return f"""https://www.indeed.com/jobs?q={self.__job_title}+${self.__desired_salary}&l={self.__location}&radius={self.__radius}&jt={self.__job_type}&explvl={self.__exp_level}&fromage={self.__date_posted}"""

    @classmethod
    def get_url(cls):
        get_object_params = URLBuild(
            cls.__get_job_title,
            cls.__get_desired_salary,
            cls.__get_location,
            cls.__get_radius,
            cls.__get_job_type,
            cls.__get_exp_level,
            cls.__get_date_posted
        )
        return get_object_params.then_build_url()


"""========================================================================="""


class Job:
    def __init__(self, title, company, rating, location, job_summary):
        self.__title = title
        self.__company = company
        self.__rating = rating
        self.__location = location
        self.__job_summary = job_summary

    @property
    def title(self):
        return self.__title

    @property
    def company(self):
        return self.__company

    @property
    def rating(self):
        return self.__rating

    @property
    def location(self):
        return self.__location

    @property
    def summary(self):
        return self.__job_summary


"""========================================================================="""


class JobScraper:
    __URL = URLBuild.get_url()
    all_cards = []

    # private
    @classmethod
    def __get_data_document(cls, url):
        data = BeautifulSoup(requests.get(url).content, 'html.parser')

        return data

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


"""========================================================================="""


class Jobs:
    @classmethod
    def __get_job_listings(cls):
        listing = []
        for card in JobScraper.get_job_cards_for_each_page():
            title = "N/A" if len(card.select("h2.title")) == 0 else card.select("h2.title a")[0].get_text()
            company = "N/A" if len(card.select("div.sjcl span.company")) == 0 else card.select("div.sjcl span.company")[0].get_text()
            rating = "N/A" if len(card.select("div.sjcl span.ratingsDisplay a span.ratingsContent")) == 0 else card.select("div.sjcl span.ratingsDisplay a span.ratingsContent")[0].get_text()
            location = "N/A" if len(card.select("div.sjcl div.location")) == 0 else card.select("div.sjcl div.location")[0].get_text()

            job_summary_list = card.select("div.summary ul li")
            curated_job_summary_list = []
            for summary in job_summary_list:
                curated_job_summary_list.append(summary.get_text())

            listing.append(Job(title, company, rating, location, curated_job_summary_list))

        return listing

    @classmethod
    def list_jobs(cls):
        job_listings = cls.__get_job_listings()
        for this_job in job_listings:
            print(f"""\n================================\nTitle: {this_job.title}\nCompany: {this_job.company}\nRating: {this_job.rating}]\nLocation: {this_job.location}\n****** Summary/Description ******""")
            for summary in this_job.summary:
                print(f"• {summary}")
            print("****** End ******")


CLI.run()
