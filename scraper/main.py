import os
from datetime import datetime
from src.jobspy import scrape_jobs
from s3.s3_helpers import upload_to_s3  # Make sure to import your helper function

# Get the directory in which the current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ensure the 'data' directory exists within the same directory as the script
data_dir = os.path.join(current_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term="Software Engineer",
    location="Vancouver, BC",
    results_wanted=30,
    country_indeed='Canada'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")

# Generate a date prefix and timestamp for the filename
date_prefix = datetime.now().strftime('%Y/%m/%d')  # S3 prefix in 'YYYY/MM/DD' format
timestamp = datetime.now().strftime('%Y%m%dT%H%M%S')  # Compact timestamp

# Construct the S3 key with the prefix and the timestamped filename
s3_key = f"{date_prefix}/jobs_{timestamp}.csv"

# Save the jobs to a CSV file in the 'data' directory with a timestamp
jobs_csv_path = os.path.join(data_dir, f'jobs_{timestamp}.csv')
jobs.to_csv(jobs_csv_path, index=False)

print(f"Jobs saved to {jobs_csv_path}")

# Now use the helper function to upload the file to S3
s3_bucket_name = os.getenv('S3_BUCKET_NAME')
if s3_bucket_name:
    upload_to_s3(s3_bucket_name, s3_key, jobs_csv_path)
    print(f"Jobs uploaded to S3 bucket {s3_bucket_name} at {s3_key}")
else:
    print("S3 bucket name is not set in .env file.")

print("Done!")