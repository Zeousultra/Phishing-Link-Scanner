import argparse
import re
import requests
from urllib.parse import urlparse

PHISHING_KEYWORDS = ["login", "verify", "account", "update", "secure", "banking", "password", "signin"]
SHORTENERS = ["bit.ly", "t.co", "goo.gl", "tinyurl.com", "is.gd", "buff.ly", "adf.ly", "ow.ly"]

def is_ip_address(url):
    return bool(re.match(r"https?://\d{1,3}(?:\.\d{1,3}){3}", url))

def contains_phishing_keywords(url):
    found = [kw for kw in PHISHING_KEYWORDS if kw.lower() in url.lower()]
    return found

def uses_shortener(netloc):
    return any(shortener in netloc for shortener in SHORTENERS)

def follow_redirects(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.url if response.url != url else None
    except requests.RequestException:
        return None

def scan_url(url):
    parsed = urlparse(url)
    flags = []
    verdict_issues = []

    print("\n🔍 PHISHING LINK SCANNER\n" + "─" * 28)
    print(f"Scanning: {url}\n")

    # IP address check
    if is_ip_address(url):
        print("  ❌ Uses IP address instead of domain")
        verdict_issues.append("ip")
    else:
        print("  ✅ Uses domain name")

    # Phishing keywords
    keywords = contains_phishing_keywords(url)
    if keywords:
        print(f"  ❌ Contains phishing keywords: {', '.join(keywords)}")
        verdict_issues.append("keywords")
    else:
        print("  ✅ No phishing keywords found")

    # Shortened URL check
    if uses_shortener(parsed.netloc):
        print(f"  ❌ Uses URL shortener: {parsed.netloc}")
        verdict_issues.append("shortener")
    else:
        print("  ✅ Not a known URL shortener")

    # Redirect check
    redirect = follow_redirects(url)
    if redirect:
        print(f"  ➡ Redirects to: {redirect}")
        if uses_shortener(urlparse(redirect).netloc):
            verdict_issues.append("redirect_shortener")
    else:
        print("  ✅ No redirect detected")

    print("\n🧠 Final Verdict:")
    if verdict_issues:
        print(" ⚠ Suspicious — Might be phishing.")
    else:
        print(" ✅ Likely safe.")

def main():
    parser = argparse.ArgumentParser(description="Simple phishing link scanner")
    parser.add_argument("-u", "--url", help="URL to scan", required=True)
    args = parser.parse_args()
    scan_url(args.url)

if __name__ == "__main__":
    main()
