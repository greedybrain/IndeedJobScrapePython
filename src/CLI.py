import re


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

        radius = input(int("Choose number representing your preferred radius (Optional - press enter to skip): "))

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

        job_type = input(int("Choose number representing the job type (Optional - press enter to skip): "))

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

        exp_level = input(int("Choose the number representing the experience level (Optional - press enter to skip): "))

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

        date_posted = input(int("Date posted (Optional - press enter to skip): "))

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
        pass
