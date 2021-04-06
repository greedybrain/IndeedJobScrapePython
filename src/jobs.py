from job import Job
from job_scraper import JobScraper


class Jobs:

    @classmethod
    def __get_job_listings(cls):
        listing = []
        for card in JobScraper.get_job_cards_for_each_page():
            title = card.select("h2.title").get_text()
            company = card.select("div.sjcl span.company").get_text()
            rating = card.select("div.sjcl span.ratingsDisplay a span.ratingsContent").get_text()
            location = card.select("div.sjcl div.location").get_text() if not not card.select(
                "div.sjcl div.location").get_text() else "N/A"

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
            print("\n================================")
            print(f"Title: {this_job.title}")
            print(f"Company: {this_job.company}")
            print(f"Rating: {this_job.rating}")
            print(f"Location: {this_job.location}")
            print("****** Summary/Description ******")
            for summary in this_job.summary:
                print(f"• {summary}")
            print("****** End ******")
