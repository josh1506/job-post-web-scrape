from selenium import webdriver
from selenium.webdriver.common.by import By

from .constants import url
from .jobpost_records import JobPostReport


class JobPost(webdriver.Chrome):
    def __init__(self, tear_down=False):
        self.tear_down = tear_down
        super().__init__()
        self.maximize_window()
        self.implicitly_wait(10)

    def navigate_landing_page(self):
        self.get(url)
        reject_cookies_button = self.find_element(by=By.ID, value='onetrust-accept-btn-handler')
        reject_cookies_button.click()

    def browse_jobs(self, job_type=None, job_location=None):
        if job_type:
            job_type_input = self.find_element(by=By.ID, value="text-input-what")
            job_type_input.clear()
            job_type_input.send_keys(job_type)
        if job_location:
            job_type_location = self.find_element(by=By.ID, value="text-input-where")
            job_type_location.clear()
            job_type_location.send_keys(job_location)
            job_type_location_select = self.find_elements(by=By.CLASS_NAME, value="icl-Autocomplete-option")[0]
            job_type_location_select.click()
        find_jobs_button = self.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
        find_jobs_button.click()
        sort_date_link = self.find_element(by=By.CSS_SELECTOR, value="[href*='&sort=date']")
        sort_date_link.click()

    def load_job_posts(self):
        job_post_list = []
        while True:
            job_post_results = self.find_element(by=By.CLASS_NAME, value="jobsearch-ResultsList")
            job_post_report = JobPostReport(job_post_results)
            transformed_job_list = job_post_report.transform_job_post_data()
            job_post_list.extend(transformed_job_list)
            try:
                pagination_next_button = self.find_element(by=By.CSS_SELECTOR, value='[data-testid="pagination-page-next"]')
                pagination_next_button.click()
            except:
                break
        return job_post_list
