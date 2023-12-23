"""
jobspy.scrapers.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Scrapers' exceptions.
"""

class ScraperException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with the scraper")

class LinkedInException(ScraperException):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with LinkedIn")


class IndeedException(ScraperException):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Indeed")


class ZipRecruiterException(ScraperException):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with ZipRecruiter")


class GlassdoorException(ScraperException):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Glassdoor")