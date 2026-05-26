from urllib.parse import urlparse
from phishing_db import BLACKLISTED_DOMAINS, SUSPICIOUS_KEYWORDS


def is_blacklisted(url):
    domain = urlparse(url).netloc.lower()

    for blocked in BLACKLISTED_DOMAINS:
        if blocked in domain:
            return True

    return False


def contains_suspicious_keywords(url):
    lowered = url.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lowered:
            return True

    return False


def is_https(url):
    return url.startswith("https://")
