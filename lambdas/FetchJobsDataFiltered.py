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
    logging.warning('dotenv not available, assuming running in AWS environment')
    
# Constants for environment variables
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

# Province mapping for Canadian provinces in a standardized format
PROVINCE_MAPPING = {
    "ab": "alberta",
    "bc": "britishcolumbia",
    "mb": "manitoba",
    "nb": "newbrunswick",
    "nl": "newfoundlandandlabrador",
    "ns": "novascotia",
    "on": "ontario",
    "pe": "princeedwardisland",
    "qc": "quebec",
    "sk": "saskatchewan",
    "nt": "northwestterritories",
    "nu": "nunavut",
    "yt": "yukon"
}

def standardize_location(location: str) -> str:
    """Standardize the location string to lowercase without spaces."""
    return location.lower().replace(" ", "")

def get_db_connection():
    """Establishes a database connection using configured environment variables."""
    try:
        return psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME, 
            user=DB_USER, password=DB_PASSWORD)
    except Exception as e:
        logging.error("Database connection failed: %s", e)
        raise

def get_date_days_ago(days: str) -> str:
    """Calculates the date 'days' number of days ago from today."""
    try:
        days_ago = int(days)
        target_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
        return target_date.strftime('%Y-%m-%d')
    except ValueError:
        logging.error("Invalid input for days: %s", days)
        raise
    
    
def build_query(event: Dict[str, Any]) -> (str, List[Any]):
    """Builds the SQL query based on the provided parameters in the event."""
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

    query = f"{base_query} WHERE {' AND '.join(conditions)} ORDER BY date_posted DESC" if conditions else base_query
    return query, values


def execute_query(cursor, query: str, values: List[Any]) -> List[Dict[str, Any]]:
    """Executes the given SQL query and returns the result."""
    try:
        cursor.execute(query, values)
        return cursor.fetchall()
    except Exception as e:
        logging.error("Query execution failed: %s", e)
        raise

def lambda_handler(event, context):
    """Entry point for the AWS Lambda function."""
    with get_db_connection() as conn:
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
    # for local development, run the lambda function
    logging.basicConfig(level=logging.INFO)
    
    # Mock event for filtering data, all empty = get all jobs
    mock_event = {'location': 'BC', 'postedWithin': '3', 'title': 'software-engineer'}
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