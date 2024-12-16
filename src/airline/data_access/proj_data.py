import os
import csv
from src.airline.logger import logging
from src.airline.exception import customException
from src.airline.config.DB_configuration import MySqlDatabase


class MySqlDataExtractor:
    def __init__(self, db_configuration, table_name):
        self.db = MySqlDatabase(db_configuration)  # Use the connection class
        self.table_name = table_name

    def extract_to_csv(self, output_dir="../../../artifacts/raw"):
        """
        Extracts data from the database table and writes it to a CSV file.
        """
        try:
            # Establish connection
            connection = self.db.connect()
            cursor = connection.cursor()

            # Execute query
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)

            # Fetch rows and columns
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            logging.info("Data fetched successfully.")

            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)
            csv_file = os.path.join(output_dir, f"{self.table_name}_data.csv")

            # Write data to CSV
            with open(csv_file, mode='w', newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(columns)  # Write headers
                writer.writerows(rows)   # Write all rows

            logging.info(f"Data successfully saved to {csv_file}")

        except Exception as e:
            logging.error("Error while extracting data from the database.")
            raise customException(f"Error in extracting data: {e}")

        finally:
            # Clean up resources
            if 'cursor' in locals():
                cursor.close()
            self.db.close_connection()
