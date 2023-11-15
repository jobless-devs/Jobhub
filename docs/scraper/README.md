# 📚 JobHub Scraper Documentation

### 🌟 Overview
The JobHub Scraper automates job listing collection from various online platforms. Designed for containerized environments, it fetches job data based on predefined search terms and uploads to AWS S3 for analysis.

### 🔍 How It Works
1. **Setup**: Containerized with Docker for consistent environments. Configured via `main.py` and `config.py`.
2. **Scraping**: Initiated by `main.py`, collects listings from Indeed, LinkedIn, ZipRecruiter, and Glassdoor.
3. **Data Handling**: Saves data in CSV, then uploads to AWS S3, managed by `s3_helpers.py` and `aggregator.py`.
4. **Scalability & Flexibility**: Modular design for easy expansion and volume handling.
5. **Error Handling**: Built-in retry logic for reliable data collection.

### 🛠️ Key Components
- `main.py`: Entry point, orchestrates scraping, data aggregation, and S3 upload.
- `config.py`: Configuration settings.
- `Dockerfile` & `docker-compose.yml`: Container setup.
- `s3_helpers.py`: Manages AWS S3 uploads.
- `aggregator.py`: Combines CSV files.
- `jobspy` module: Core scraping logic.

### 📁 Folder & File Structure
- **Root Directory**: Contains `main.py`, Docker files, and configs.
  - `main.py`: Starts scraping and manages data flow.
  - `Dockerfile` & `docker-compose.yml`: Docker setup.
  - `requirements.txt`: Python dependencies.
  - `.env`: (Not in repo) Environment variables.
- **src/**: Core source code.
  - `jobspy/`: Scraping logic.
  - `processors/`: Houses `aggregator.py`.
  - `config.py`: Scraper settings.
- **s3/**: `s3_helpers.py` for S3 interactions.
- **data/**: (Generated) Stores CSV job data.
  - `individual_run/`: CSVs from each session.
  - `aggregated/`: Aggregated CSV file.
- **tests/**: Scraper test cases.

### ✍ Contribute & Improve
Contributions welcome to enhance efficiency, add features, or improve documentation.

### 🤔 Decisions & Trade-offs
- **Containerization**: Docker for consistent environments.
- **Local Storage vs. S3**: Ensures data integrity and fallback.

### Conclusion
The JobHub Scraper is a key tool for data collection, designed for efficiency, scalability, and reliability.

# Next Reading if interested: [scraping_process.md](scraping_process.md)
