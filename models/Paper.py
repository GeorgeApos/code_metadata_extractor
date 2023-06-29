class Paper:
    def __init__(self, url):
        self.url = url
        self.current_version = None
        self.repo_link = None
        self.license = None
        self.versioning_system = None
        self.languages_tools_services = None
        self.compilation_requirements = None
        self.documentation_link = None
        self.support_email = None

    def print_data(self):
        print("URL:", self.url)
        print("Current code version:", self.current_version)
        print("Permanent link to code/repository:", self.repo_link)
        print("Legal Code License:", self.license)
        print("Code versioning system used:", self.versioning_system)
        print("Software code languages, tools, and services used:", self.languages_tools_services)
        print("Compilation requirements, operating environments & dependencies:", self.compilation_requirements)
        print("If available Link to developer documentation/manual:", self.documentation_link)
        print("Support email for questions:", self.support_email)