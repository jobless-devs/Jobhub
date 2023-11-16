# 📚 JobHub Scraper: Scraping & Uploading Process

## Overview
This document details the JobHub Scraper's process for scraping job listings and uploading data to AWS S3.

## Scraping Process
1. **Initialization**: `main.py` starts the process, using settings from `config.py`.
2. **Configuration Load**: `config.py` loads search terms and scraper settings.
3. **Scraping Loop**:
   - For each term in `SEARCH_TERMS`, the scraper:
     - Generates a timestamped filename.
     - Calls `run_scraper()` with site names, search term, location, desired results, and country.
     - Saves scraped jobs to a CSV file in `data/individual_run`.
4. **Data Aggregation**:
   - `aggregate_csv_files()` in `aggregator.py` combines individual CSVs into one file in `data/aggregated`.

## Uploading Process
1. **S3 Bucket Preparation**: Ensures AWS S3 bucket details are set in `.env`.
2. **Upload Trigger**:
   - After data aggregation, `upload_data_to_s3()` in `s3_helpers.py` is called.
   - Prepares an S3 key using the current date.
3. **Data Upload**:
   - Uploads the aggregated CSV to the specified S3 bucket.
   - Prints confirmation upon successful upload.

## Key Components
- `main.py`: Orchestrates scraping and uploading.
- `config.py`: Holds search terms and scraper settings.
- `s3_helpers.py`: Manages AWS S3 interactions.
- `aggregator.py`: Aggregates CSV files for upload.

## Conclusion
The JobHub Scraper efficiently collects job listings and uploads them to AWS S3, following a structured, step-by-step process for reliability and scalability.

# Next reading if interested: [potential_improvements.md](potential_improvements.md) 
