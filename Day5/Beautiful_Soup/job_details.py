import requests
from bs4 import BeautifulSoup
import re

class JobDetails:
    @staticmethod
    def get_job_details(job_url):
        """Extracts job details from an individual job listing."""
        if job_url == 'N/A':
            return {}

        job_html = requests.get(job_url).text
        job_soup = BeautifulSoup(job_html, 'lxml')

        details_list = job_soup.find('ul', class_='top-jd-dtl d-flex mt-8')
        experience, salary = 'N/A', 'N/A'

        if details_list:
            list_items = details_list.find_all('li')
            for li in list_items:
                text = " ".join(li.stripped_strings)
                text = re.sub(r'\s+', ' ', text)  # Remove excessive spaces
                if li.find('i', class_='srp-icons experience'):
                    experience = text
                elif li.find('i', class_='srp-icons salary'):
                    salary = text

        location_tag = job_soup.find('span', class_='job-location-trunicate')
        skill_tags = job_soup.find_all('span', class_='jd-skill-tag')
        skills = [re.sub(r'\s+', ' ', skill.text.strip()) for skill in skill_tags if skill.text.strip()]

        return {
            "experience": experience,
            "salary": salary,
            "location": location_tag.text.strip() if location_tag else 'N/A',
            "skills": skills
        }
