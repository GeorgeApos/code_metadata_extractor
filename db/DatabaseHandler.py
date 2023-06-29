import mysql.connector


class DatabaseHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def create_table(self, table_name, columns):
        if self.connection:
            cursor = self.connection.cursor()
            column_definitions = ', '.join(columns)
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
            cursor.execute(create_table_query)
            self.connection.commit()
            cursor.close()
            print(f"Table '{table_name}' created successfully.")

    def insert_data(self, table_name, data):
        if self.connection:
            cursor = self.connection.cursor()
            placeholders = ', '.join(['%s'] * len(data))
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(insert_query, data)
            self.connection.commit()
            cursor.close()
            print("Data inserted successfully.")

    def retrieve_data(self, table_name):
        if self.connection:
            cursor = self.connection.cursor()
            select_query = f"SELECT * FROM {table_name}"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            cursor.close()
            return rows

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
