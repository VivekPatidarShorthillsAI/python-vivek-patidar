import re
from bs4 import BeautifulSoup

class CourseScraper:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'lxml')

    def extract_courses(self):
        """Extracts course details from a local HTML file."""
        course_cards = self.soup.find_all('div', class_='card')
        courses = []

        for course in course_cards:
            course_name = re.sub(r'\s+', ' ', course.h5.text.strip())  # Remove excessive spaces
            course_price_text = course.a.text.strip()
            course_price_match = re.search(r'\d+', course_price_text)  # Extract only the numeric price
            course_price = course_price_match.group() if course_price_match else 'N/A'
            courses.append((course_name, course_price))

        return courses

    @staticmethod
    def display_courses(courses):
        """Displays the extracted courses."""
        for name, price in courses:
            print(f'{name} costs {price}')
