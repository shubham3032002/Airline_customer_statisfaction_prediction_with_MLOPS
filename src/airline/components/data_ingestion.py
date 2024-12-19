
import mysql.connector
from mysql.connector import Error
import os
import csv
import sys
from contextlib import contextmanager
from src.airline.exception import customException
from src.airline.logger import logging
from pathlib import Path
from src.airline.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.connection = None

    @contextmanager
    def get_connection(self):
        """Context manager for MySQL connection."""
        connection = mysql.connector.connect(
            host=self.config.host,
            user=self.config.user,
            password=self.config.password,
            database=self.config.database
        )
        try:
            yield connection
        finally:
            if connection.is_connected():
                connection.close()
                logging.info("Database connection closed successfully.")

    def extract_to_csv(self, output_dir: Path):
        """Extract data from MySQL table and save to a CSV file."""
        try:
            with self.get_connection() as connection:
                cursor = connection.cursor()
                query = f"SELECT * FROM {self.config.table_name}"
                cursor.execute(query)

                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                logging.info("Data fetched successfully.")

                # Ensure output directory exists
                output_dir.mkdir(parents=True, exist_ok=True)
                csv_file = output_dir / f"{self.config.table_name}_data.csv"

                with csv_file.open(mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(columns)
                    writer.writerows(rows)

                logging.info(f"Data successfully saved to {csv_file}")

        except Exception as e:
            logging.error(f"Error while extracting data from the database: {str(e)}")
            raise customException(e, sys)