from cli import CLI


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


CLI.run()
