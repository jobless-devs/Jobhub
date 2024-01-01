import psycopg2
import json
import os
import logging

try:
    # for local development, load environment variables from .env file
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    logging.warning('dotenv not available, assuming running in AWS environment')

def get_db_connection():
    try:
        return psycopg2.connect(
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT'],
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'])
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        raise

def fetch_data(cursor):
    try:
        cursor.execute("SELECT id, title, city, location, company, job_type, date_posted, job_url FROM jobs")
        # Fetch the column names
        colnames = [desc[0] for desc in cursor.description]
        # Use a list comprehension and zip to create a list of dictionaries
        return [dict(zip(colnames, row)) for row in cursor.fetchall()]

    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        raise
    
def lambda_handler(event, context):
    with get_db_connection() as conn, conn.cursor() as cursor:
        rows = fetch_data(cursor)
        # The rows are a list of dicts, which json.dumps will convert to a list of JSON objects
        json_rows = json.dumps(rows, default=str)

    return {
        'statusCode': 200,
        'body': json_rows,
        'records_fetched': len(rows)
    }
    
if __name__ == "__main__":
    # for local development, run the lambda function
    logging.basicConfig(level=logging.INFO)
    result = lambda_handler(None, None)

    # Extracting the statusCode, body, and records_fetched from the result
    status_code = result['statusCode']
    records_fetched = result['records_fetched']
    body = json.loads(result['body'])

    # Print statusCode, one example from body (if available), and records_fetched
    print(f"Status Code: {status_code}")
    print(f"Example Record: {body[0] if body else 'No records found'}")
    print(f"Total Records Fetched: {records_fetched}")