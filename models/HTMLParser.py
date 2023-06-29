import re


class HTMLParser:
    def __init__(self, html_content):
        self.html_content = html_content

    def extract_information(self, pattern):
        result = re.search(pattern, self.html_content)
        return result.group(1) if result else ""

    def extract_current_version(self):
        pattern = r'Current code version\s*</td>\s*<td class="align-left">\s*([^<]+)'
        return self.extract_information(pattern)

    def extract_repo_link(self):
        pattern = r'Permanent link to code/repository used for this code version\s*</td>\s*<td class="align-left">\s*<a class="anchor u-display-inline anchor-paragraph anchor-external-link" href="([^"]+)"'
        return self.extract_information(pattern)

    def extract_license(self):
        pattern = r'Legal Code License\s*</td>\s*<td class="align-left">\s*([^<]+)'
        return self.extract_information(pattern)

    def extract_versioning_system(self):
        pattern = r'Code versioning system used\s*</td>\s*<td class="align-left">\s*([^<]+)'
        return self.extract_information(pattern)

    def extract_languages_tools_services(self):
        pattern = r'Software code languages, tools, and services used\s*</td>\s*<td class="align-left">\s*([^<]+)'
        return self.extract_information(pattern)

    def extract_compilation_requirements(self):
        pattern = r'Compilation requirements, operating environments &amp; dependencies\s*</td>\s*<td class="align-left">\s*([^<]+)'
        return self.extract_information(pattern)

    def extract_documentation_link(self):
        pattern = r'If available Link to developer documentation/manual\s*</td>\s*<td class="align-left">\s*<a class="anchor u-display-inline anchor-paragraph anchor-external-link" href="([^"]+)"'
        return self.extract_information(pattern)

    def extract_support_email(self):
        pattern = r'Support email for questions\s*</td>\s*<td class="align-left">\s*<a class="anchor u-display-inline anchor-paragraph anchor-external-link" href="mailto:([^"]+)"'
        return self.extract_information(pattern)