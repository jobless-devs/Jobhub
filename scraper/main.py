import os
from datetime import datetime
from src.jobspy import scrape_jobs
from s3.s3_helpers import upload_to_s3
from src.processors.aggregator import aggregate_csv_files
from src.config import SEARCH_TERMS, SCRAPER_SETTINGS

def setup_data_directory(base_path: str, sub_path: str) -> str:
    data_dir = os.path.join(base_path, sub_path)
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

def run_scraper(site_names, search_term, location, results_wanted, country, output_path):
    jobs = scrape_jobs(
        site_name=site_names,
        search_term=search_term,
        location=location,
        results_wanted=results_wanted,
        country_indeed=country
    )
    jobs.to_csv(output_path, index=False)
    print(f"Found {len(jobs)} jobs for '{search_term}', saved to {output_path}")

def upload_data_to_s3(bucket_name, s3_key, data_path):
    if bucket_name:
        upload_to_s3(bucket_name, s3_key, data_path)
        print(f"Jobs uploaded to S3 bucket {bucket_name} at {s3_key}")
    else:
        print("S3 bucket name is not set in .env file.")
        
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    individual_run_dir = setup_data_directory(current_dir, 'data/individual_run')
    aggregated_dir = setup_data_directory(current_dir, 'data/aggregated')
    
    search_terms = SEARCH_TERMS 
    site_names = SCRAPER_SETTINGS['site_names']
    location = SCRAPER_SETTINGS['location']
    results_wanted = SCRAPER_SETTINGS['results_wanted']
    country = SCRAPER_SETTINGS['country_indeed'] # Indeed only 
    
    for term in search_terms:
        timestamp = datetime.now().strftime('%Y%m%dT%H%M%S')  # Compact timestamp
        term_filename = term.replace(" ", "_").lower()
        csv_filename = f'jobs_{term_filename}_{timestamp}.csv'
        jobs_csv_path = os.path.join(individual_run_dir, csv_filename)
        
        run_scraper(site_names, term, location, results_wanted, country, jobs_csv_path)
    
    aggregated_file_path = aggregate_csv_files(individual_run_dir, aggregated_dir)
    
    date_prefix = datetime.now().strftime('%Y/%m/%d')  # S3 prefix in 'YYYY/MM/DD' format
    s3_key_aggregated = f"{date_prefix}/aggregated_jobs.csv"
    upload_data_to_s3(os.getenv('S3_BUCKET_NAME'), s3_key_aggregated, aggregated_file_path)

if __name__ == "__main__":
    print("Starting the scraping process...")
    main()
    print("Scraping process completed.")