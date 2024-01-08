import psycopg2
import psycopg2.extras
import json
import os
import logging
from typing import Dict, List, Any
import datetime

try:
    # for local development, load environment variables from .env file
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    # Import in production
    from DbConnection import get_db_connection # dbConnectionLayer
    from ProvinceMapping import PROVINCE_MAPPING # provinceMappingLayer
    from DbConfig import DB_CONFIG # dbConfig file

FUNCTION_NAME = 'FetchJobsDataFiltered' # For error logging purpose

def standardize_location(location: str) -> str:
    """
    Standardizes a location string by converting it to lowercase and removing spaces.

    :param location: A string representing the location.
    :return: A standardized location string.
    """
    return location.lower().replace(" ", "")

def get_date_days_ago(days: str) -> str:
    """
    Computes a date that is a given number of days in the past from the current date.

    :param days: A string representing the number of days.
    :return: A string representing the date in 'YYYY-MM-DD' format.
    :raises ValueError: If the input is not a valid number of days.
    """
    try:
        days_ago = int(days)
        target_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
        return target_date.strftime('%Y-%m-%d')
    except ValueError:
        sub_function_name = "get_date_days_ago()"
        logging.error("[%s - %s]: Invalid input for days", FUNCTION_NAME, sub_function_name)
        raise
    
    
def build_query(event: Dict[str, Any]) -> (str, List[Any]):
    """
    Builds an SQL query for fetching job data based on the parameters provided in the event.

    :param event: A dictionary containing parameters for the query.
    :return: A tuple containing the SQL query string and a list of values for the query parameters.
    """
    base_query = "SELECT id, title, city, location, company, job_type, date_posted, job_url FROM jobs"
    conditions = []
    values = []

    # Check if 'postedWithin' is present and not empty
    if event.get('postedWithin'):
        target_date = get_date_days_ago(days=event['postedWithin'])
        conditions.append("date_posted >= %s")
        values.append(target_date)

    # Check if 'location' is present and not empty
    if event.get('location'):
        location_param = standardize_location(event['location'])
        province_full = PROVINCE_MAPPING.get(location_param, location_param)
        location_condition = "(REPLACE(LOWER(location), ' ', '') ILIKE %s OR REPLACE(LOWER(location), ' ', '') ILIKE %s)"
        conditions.append(location_condition)
        values.extend([f"%{location_param}%", f"%{province_full}%"])

    # Check if 'title' is present and not empty
    if event.get('title'):
        title_param = event['title'].replace("-", " ")
        title_condition = "title ILIKE %s"
        conditions.append(title_condition)
        values.append(f"%{title_param}%")

    if conditions:
        query = f"{base_query} WHERE {' AND '.join(conditions)} ORDER BY date_posted DESC"
    else:
        query = f"{base_query} ORDER BY date_posted DESC"
    return query, values


def execute_query(cursor: psycopg2.extensions.cursor, query: str, values: List[Any]) -> List[Dict[str, Any]]:
    """
    Executes a SQL query using the provided cursor, query string, and values.

    :param cursor: A database cursor to execute the query.
    :param query: A string representing the SQL query to be executed.
    :param values: A list of values for the query parameters.
    :return: A list of dictionaries, each representing a row in the result set.
    """
    try:
        cursor.execute(query, values)
        return cursor.fetchall()
    except Exception as e:
        sub_function_name = "execute_query()"
        logging.error("[%s - %s]: Database connection failed. Exception: %s", FUNCTION_NAME, sub_function_name, e)
        raise

def lambda_handler(event, context):
    """
    AWS Lambda handler function to fetch filtered job data based on the event.

    :param event: The event triggering this Lambda function.
    :param context: Runtime information provided by AWS Lambda.
    :return: A dictionary with statusCode, body (JSON string), and number of records.
    """
    with get_db_connection(**DB_CONFIG) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            query, values = build_query(event)
            results = execute_query(cursor, query, values)
            json_results = json.dumps(results, default=str)

    return {
        'statusCode': 200,
        'body': json_results,
        'records_fetched': len(results)
    }

# Local development testing...
if __name__ == "__main__":
    import sys
    # Import 
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    sys.path.insert(0, project_root)
    from lambdas.layers.dbConnectionLayer.python.DbConnection import get_db_connection
    from lambdas.layers.provinceMappingLayer.python.ProvinceMapping import PROVINCE_MAPPING
    from lambdas.layers.dbConfigLayer.python.DbConfig import DB_CONFIG 
    
    logging.basicConfig(level=logging.INFO)
    
    # Mock event for filtering data, all empty = get all jobs
    # Mock event for all jobs:
    # mock_event = {'location': '', 'postedWithin': '', 'title': ''}
    mock_event = {'location': 'BC', 'postedWithin': '10', 'title': 'software-engineer'}
    result = lambda_handler(mock_event, None)

    # Extracting the statusCode, body, and records_fetched from the result
    status_code = result['statusCode']
    records_fetched = result['records_fetched']
    body = json.loads(result['body'])

    # Print statusCode, one example from body (if available), and records_fetched
    print(f"Status Code: {status_code}")
    # print(f"Example Record: {body[0] if body else 'No records found'}")
    print(f"Example Record: {body if body else 'No records found'}")
    
    print(f"Total Records Fetched: {records_fetched}")