from db import db_host, db_user, db_password, db_name, table_name, columns
from db.DatabaseHandler import DatabaseHandler
from models import urls_to_check
from models.HTMLParser import HTMLParser
from models.Paper import Paper
from models.WebpageScraper import WebpageScraper

if __name__ == '__main__':
    db_handler = DatabaseHandler(host=db_host, user=db_user, password=db_password,
                                 database=db_name)

    for url in urls_to_check:
        web_scraper = WebpageScraper()
        source_code = web_scraper.get_page_source(url)
        web_scraper.quit()

        # Find the <div> containing the code metadata
        metadata_div = web_scraper.find_metadata_div(source_code)

        # Create HTMLParser object
        parser = HTMLParser(metadata_div)

        # Extract the desired information and store it in the Paper object
        paper = Paper(url)

        paper.current_version = parser.extract_current_version()
        paper.repo_link = parser.extract_repo_link()
        paper.license = parser.extract_license()
        paper.versioning_system = parser.extract_versioning_system()
        paper.languages_tools_services = parser.extract_languages_tools_services()
        paper.compilation_requirements = parser.extract_compilation_requirements()
        paper.documentation_link = parser.extract_documentation_link()
        paper.support_email = parser.extract_support_email()

        paper.print_data()

        # Connect to the database
        db_handler.connect()

        # Create a table
        db_handler.create_table(table_name, columns)

        # Insert data into the table
        data = (
            paper.url,
            paper.current_version,
            paper.repo_link,
            paper.license,
            paper.versioning_system,
            paper.languages_tools_services,
            paper.compilation_requirements,
            paper.documentation_link,
            paper.support_email
        )
        db_handler.insert_data(table_name, data)

    # Close the database connection
    db_handler.close_connection()
