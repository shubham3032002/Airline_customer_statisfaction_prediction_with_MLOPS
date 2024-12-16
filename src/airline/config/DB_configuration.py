import mysql.connector
from mysql.connector import Error
from src.airline.logger import logging
from src.airline.exception import customException
import sys
from src.airline.constants import DB_configuration

class MySqlDatabase:
    def __init__(self, db_configuration):
        self.host = db_configuration['host']
        self.user = db_configuration['user']
        self.password = db_configuration['password']
        self.database = db_configuration['database']
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                logging.info(f"Connected to the database '{self.database}' successfully.")
                return self.connection
        except Error as e:
            logging.error(f"Error connecting to the database: {str(e)}")
            raise customException(e, sys)

    def close_connection(self):
        """
        Closes the database connection.
        """
        try:
            if self.connection and self.connection.is_connected():
                self.connection.close()
                logging.info("Database connection closed successfully.")
        except Error as e:
            logging.error("Error while closing the database connection.")
            raise customException(e, sys)
