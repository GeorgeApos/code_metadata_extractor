# Configure the database connection
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_name = 'science_dir'

# Configure the table
table_name = 'papers'
columns = [
    'url VARCHAR(255) PRIMARY KEY',
    'current_version VARCHAR(255)',
    'repo_link VARCHAR(255)',
    'license VARCHAR(255)',
    'versioning_system VARCHAR(255)',
    'languages_tools_services VARCHAR(255)',
    'compilation_requirements VARCHAR(255)',
    'documentation_link VARCHAR(255)',
    'support_email VARCHAR(255)'
]