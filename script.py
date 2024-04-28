import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from requests.exceptions import ConnectionError

def is_pypi_website(link_url):
    parsed_url = urlparse(link_url)
    return parsed_url.netloc == 'pypi.org'

def get_redirected_url(url):
    response = requests.head(url, allow_redirects=True)
    return response.url

def check_links(link_url, timeout=5):
    response = requests.get(link_url)
    if response.status_code != 200:
        print(f"Error: Failed to fetch {link_url}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)

    for link in links:
        href = link['href']
        if href.startswith('http') or href.startswith('mailto:'):
            continue

        absolute_url = urljoin(link_url, href)
        try:
            link_response = requests.head(absolute_url, timeout=timeout)
        except ConnectionError as e:
            print(f"Connection error for link: {absolute_url}. Ignoring and continuing.")
            continue

        if link_response.status_code != 200:
            print(f"Broken link: {absolute_url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check links on a PyPI website.")
    parser.add_argument("--link-url", required=True, help="URL of the PyPI website to check")
    args = parser.parse_args()

    link_url = args.link_url
    if is_pypi_website(link_url):
        check_links(link_url)
    else:
        print("This is not a PyPI website.")
