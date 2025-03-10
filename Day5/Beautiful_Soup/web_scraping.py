import requests
from course_scraper import CourseScraper
from job_scraper import JobScraper

if __name__ == "__main__":
    # Extracting courses from local HTML file
    with open('index.html', 'r', encoding='utf-8') as file:
        soup = file.read()

    course_scraper = CourseScraper(soup)
    courses = course_scraper.extract_courses()
    course_scraper.display_courses(courses)

    # Scraping latest job listings from TimesJobs
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=%22Software+Developer%22&txtKeywords=%22Software+Developer%22%2C&txtLocation="
    unfamiliar_skills = input('Enter skills to filter out: ').strip()

    job_scraper = JobScraper(url, unfamiliar_skills)
    job_scraper.scrape_jobs()
