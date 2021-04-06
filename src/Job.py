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
    def job_summary(self):
        return self.__job_summary

