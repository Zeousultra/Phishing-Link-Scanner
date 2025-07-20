import re
import argparse
import requests
from urllib.parse import urlparse
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Define phishing-related keywords
phishing_keywords = [
    "login", "verify", "account", "secure", "bank", "update", "free", "gift"
]

# Known URL shorteners
url_shorteners = [
    "bit.ly", "t.co", "tinyurl.com", "goo.gl", "ow.ly", "buff.ly", "adf.ly"
]

def is_shortened(url):
    domain = urlparse(url).netloc
    return any(short in domain for short in url_shorteners)

def contains_keywords(url):
    found = [kw for kw in phishing_keywords if kw in url.lower()]
    return found

def is_suspicious_structure(url):
    domain = urlparse(url).netloc
    return domain.count(".") > 3

def resolve_redirects(url):
    try:
        response = requests.get(url, timeout=5)
        return response.url
    except requests.RequestException:
        return None

def analyze_url(url):
    print(Fore.CYAN + "\n────────────────────────────")
    print(Fore.YELLOW + f"Scanning: {url}\n")

    domain = urlparse(url).netloc
    if domain:
        print(Fore.GREEN + "  ✅ Uses domain name")
    else:
        print(Fore.RED + "  ❌ No domain detected")

    keywords = contains_keywords(url)
    if keywords:
        print(Fore.RED + f"  ❌ Contains phishing keywords: {', '.join(keywords)}")
    else:
        print(Fore.GREEN + "  ✅ No phishing keywords detected")

    if is_shortened(url):
        print(Fore.RED + "  ❌ Known URL shortener used")
    else:
        print(Fore.GREEN + "  ✅ Not a known URL shortener")

    if is_suspicious_structure(url):
        print(Fore.RED + "  ⚠ Suspicious domain structure")

    redirect_url = resolve_redirects(url)
    if redirect_url and redirect_url != url:
        print(Fore.BLUE + f"  ➡ Redirects to: {redirect_url}")
    elif redirect_url:
        print(Fore.GREEN + "  ✅ No redirection detected")
    else:
        print(Fore.RED + "  ❌ Failed to resolve URL")

    if keywords or is_shortened(url) or is_suspicious_structure(url):
        print(Fore.RED + Style.BRIGHT + "\n⚠ This URL may be a PHISHING ATTEMPT.\n")
    else:
        print(Fore.GREEN + Style.BRIGHT + "\n✅ This URL appears to be safe.\n")

def main():
    parser = argparse.ArgumentParser(description="Phishing Link Scanner")
    parser.add_argument("-u", "--url", required=True, help="URL to scan")
    args = parser.parse_args()
    analyze_url(args.url)

if __name__ == "__main__":
    main()
