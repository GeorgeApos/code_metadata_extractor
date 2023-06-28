import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_metadata_div(source_code_to_search):
    print("Finding metadata div...")
    soup = BeautifulSoup(source_code_to_search, 'html.parser')
    metadata_div = soup.find('div', class_='groups')
    metadata_div.prettify()

    return metadata_div.prettify()


def get_page_source(page_url):
    driver = webdriver.Chrome()
    driver.get(page_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'groups')))
    page_source = driver.page_source
    page_source = page_source.encode('utf-8')
    driver.quit()

    return page_source


if __name__ == '__main__':
    url = 'https://www.sciencedirect.com/science/article/pii/S2665963823000283'
    source_code = get_page_source(url)
    print("=====================================================")
    metadata_div = find_metadata_div(source_code)
    print("Metadata Div: \n", metadata_div)
    pattern_version = r"([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)"
    pattern_gitUrl = r'^.*[^"]*.*$'
    version_match = re.search(pattern_version, metadata_div, re.DOTALL)
    gitUrl_match = re.search(pattern_gitUrl, metadata_div, re.DOTALL)
    if version_match:
        print("Version: ", version_match.group(1))
    else:
        print("Version: Not found")

    if gitUrl_match:
        print("Git URL: ", gitUrl_match.group(0))
    else:
        print("Git URL: Not found")
    print("=====================================================")