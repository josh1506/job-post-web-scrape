from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class JobPostReport:
    def __init__(self, job_search_result_list: WebElement):
        self.job_search_result_list = job_search_result_list
        self.job_post_card_list = self.get_job_post_cards()
        super().__init__()

    def get_job_post_cards(self):
        return self.job_search_result_list.find_elements(by=By.CLASS_NAME, value="job_seen_beacon")

    def transform_job_post_data(self):
        transformed_datas = []
        for job_post_container in self.job_post_card_list:
            job_post_title = job_post_container.find_element(
                by=By.CLASS_NAME,
                value="jobTitle"
            ).get_attribute("innerText")
            job_post_company = job_post_container.find_element(
                by=By.CLASS_NAME,
                value="companyName"
            ).get_attribute("innerText")
            company_location = job_post_container.find_element(
                by=By.CLASS_NAME,
                value="companyLocation"
            ).get_attribute("innerText")
            job_date_posted = job_post_container.find_element(
                by=By.CLASS_NAME,
                value="date"
            ).get_attribute("innerText").split("Posted")[-1].strip()
            job_post_url = job_post_container.find_element(by=By.CLASS_NAME, value="jcs-JobTitle").get_attribute("href")
            transformed_datas.append(
                [job_post_title, job_post_company, company_location, job_post_url, job_date_posted]
            )
        return transformed_datas

