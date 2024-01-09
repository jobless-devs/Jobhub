import logging
import os
from typing import Optional

import psycopg2
import psycopg2.extras


def get_db_connection(**kwargs: Optional[str]) -> psycopg2.extensions.connection:
    """
    :param kwargs: database connection parameters.
    :return: A psycopg2 connection object.
    """
    required_params = ['host', 'port', 'dbname', 'user', 'password']
    missing_params = [param for param in required_params if param not in kwargs]
    
    if missing_params:
        logging.error(f"Missing required database parameters: {', '.join(missing_params)}")
        raise ValueError(f"Missing required database parameters: {', '.join(missing_params)}")

    try:
        return psycopg2.connect(**kwargs)
    except psycopg2.DatabaseError as e:
        function_name = "dbConnectionLayer"
        sub_function_name = "get_db_connection()"
        logging.error("[%s - %s]: Database connection failed. Exception: %s", function_name, sub_function_name, e)
        raise

if __name__ == "__main__":
    try:
        import dotenv
        dotenv.load_dotenv()
        DB_CONFIG = {
            "host": os.getenv('DB_HOST'),
            "port": os.getenv('DB_PORT'),
            "dbname": os.getenv('DB_NAME'),
            "user": os.getenv('DB_USER'),
            "password": os.getenv('DB_PASSWORD')
        }
        connection = get_db_connection(**DB_CONFIG)
        print("Database connection established successfully.")
    except Exception as e:
        print(f"Error: {e}")
