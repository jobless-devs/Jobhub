import re
import numpy as np

import requests
import tls_client
from ..jobs import JobType

import functools
import time

def retry(exception_to_check, tries=2, delay=9, backoff=2, status_code=[429, 403]):
    """
    Retry decorator with exponential backoff.
    """
    def deco_retry(func):
        @functools.wraps(func)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    if any(str(code) in str(e) for code in status_code):
                        print(f"{str(e)}, Retrying in {mdelay} seconds...(attempt {tries - mtries + 1}/{tries})")
                        time.sleep(mdelay)
                        mtries -= 1
                        mdelay *= backoff
                    else:
                        raise
            return func(*args, **kwargs)
        return f_retry  # true decorator
    return deco_retry

def count_urgent_words(description: str) -> int:
    """
    Count the number of urgent words or phrases in a job description.
    """
    urgent_patterns = re.compile(
        r"\burgen(t|cy)|\bimmediate(ly)?\b|start asap|\bhiring (now|immediate(ly)?)\b",
        re.IGNORECASE,
    )
    matches = re.findall(urgent_patterns, description)
    count = len(matches)

    return count


def extract_emails_from_text(text: str) -> list[str] | None:
    if not text:
        return None
    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    return email_regex.findall(text)


def create_session(proxy: dict | None = None, is_tls: bool = True):
    """
    Creates a tls client session

    :return: A session object with or without proxies.
    """
    if is_tls:
        session = tls_client.Session(
            client_identifier="chrome112",
            random_tls_extension_order=True,
        )
        session.proxies = proxy
        # TODO multiple proxies
        # if self.proxies:
        #     session.proxies = {
        #         "http": random.choice(self.proxies),
        #         "https": random.choice(self.proxies),
        #     }
    else:
        session = requests.Session()
        session.allow_redirects = True
        if proxy:
            session.proxies.update(proxy)

    return session


def get_enum_from_job_type(job_type_str: str) -> JobType | None:
    """
    Given a string, returns the corresponding JobType enum member if a match is found.
    """
    res = None
    for job_type in JobType:
        if job_type_str in job_type.value:
            res = job_type
    return res

def currency_parser(cur_str):
    # Remove any non-numerical characters
    # except for ',' '.' or '-' (e.g. EUR)
    cur_str = re.sub("[^-0-9.,]", '', cur_str)
    # Remove any 000s separators (either , or .)
    cur_str = re.sub("[.,]", '', cur_str[:-3]) + cur_str[-3:]

    if '.' in list(cur_str[-3:]):
        num = float(cur_str)
    elif ',' in list(cur_str[-3:]):
        num = float(cur_str.replace(',', '.'))
    else:
        num = float(cur_str)

    return np.round(num, 2)
