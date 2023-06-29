from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WebpageScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def quit(self):
        self.driver.quit()

    def get_page_source(self, page_url):
        # Open the webpage
        self.driver.get(page_url)

        # Wait for the div we want to finish loading
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'groups')))

        # Get the page source
        page_source = self.driver.page_source
        page_source = page_source.encode('utf-8')

        return page_source

    @staticmethod
    def find_metadata_div(source_code_to_search):
        # Parse the HTML string
        soup = BeautifulSoup(source_code_to_search, 'html.parser')

        # Find the <div> containing the code metadata
        metadata_div = soup.find('div', class_='groups')

        return metadata_div.prettify()
