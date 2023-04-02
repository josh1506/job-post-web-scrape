from prettytable import PrettyTable

from Indeed.jobpost.jobpost import JobPost as JobPostIndeed


field_names = ["Job Title", "Company", "Location", "URL", "Date Posted"]


def run_indeed_job_posts(job_type, location):
    indeed_job_post = JobPostIndeed()
    indeed_job_post.navigate_landing_page()
    indeed_job_post.browse_jobs(job_type, location)
    job_list = indeed_job_post.load_job_posts()
    job_table = PrettyTable(field_names=field_names)
    job_table.add_rows(job_list)
    print(job_table)


search_type = input("Job type:\n>> ")
search_location = input("Job location:\n>> ")
run_indeed_job_posts(search_type, search_location)
