import requests
from bs4 import BeautifulSoup
import re
from job_details import JobDetails

class JobScraper:
    def __init__(self, url, unfamiliar_skills):
        self.url = url
        self.unfamiliar_skills = unfamiliar_skills

    def scrape_jobs(self):
        """Scrapes job listings from TimesJobs and filters out unwanted skills."""
        print(f'Filtering out jobs with "{self.unfamiliar_skills}" skill')
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        for job in jobs:
            published_date_tag = job.find('span', class_='sim-posted')
            published_date = published_date_tag.span.text.strip() if published_date_tag and published_date_tag.span else ''

            more_info_tag = job.find('a', class_='posoverlay_srp')
            more_info = more_info_tag['href'].strip() if more_info_tag else 'N/A'

            company_name = job.find('h3', class_='joblist-comp-name')
            company_name = re.sub(r'\s+', ' ', company_name.text.strip()) if company_name else 'N/A'

            if 'few' in published_date.lower():
                job_details = JobDetails.get_job_details(more_info)
                skills = job_details.get("skills", "N/A")

                if self.unfamiliar_skills not in skills:
                    print(f'Company Name: {company_name}')
                    print(f'Required Skills: {skills}')
                    print(f'Experience: {job_details.get("experience", "N/A")}')
                    print(f'Salary: {job_details.get("salary", "N/A")}')
                    print(f'Location: {job_details.get("location", "N/A")}')
                    print(f'More Info: {more_info}\n')
