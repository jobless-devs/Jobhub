# Search terms configuration
SEARCH_TERMS = [
    "Software Engineer Intern", 
    "Software Developer Intern", 
    "Data Engineer Intern", 
    "Data Engineer Coop", 
]

# Scraper settings configuration
SCRAPER_SETTINGS = {
    "site_names": ["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    "location": "",
    "results_wanted": 100,
    "country_indeed": "Canada",
    "hyperlinks": False,
    "proxy": None,
    "offset": 0,
}

# Retry settings configuration
RETRY_SETTINGS = {
    "tries": 3,
    "delay": 1,
    "backoff": 3,
    "status_code": 429,
}