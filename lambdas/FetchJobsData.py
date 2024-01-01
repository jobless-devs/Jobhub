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
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        raise
    
def lambda_handler(event, context):
    with get_db_connection() as conn, conn.cursor() as cursor:
        rows = fetch_data(cursor)

    return {
        'statusCode': 200,
        'body': json.dumps(rows, default=str),
        'records_fetched': len(rows)
    }
    
if __name__ == "__main__":
    # for local development, run the lambda function
    logging.basicConfig(level=logging.INFO)
    print(lambda_handler(None, None))