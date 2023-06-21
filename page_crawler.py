import requests
from bs4 import BeautifulSoup

def get_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links on the page
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))

        return links
    else:
        # If the status code is not 200, return an empty list
        return []

def crawl_web(seed, max_pages):
    # Create a list to hold the URLs to crawl
    tocrawl = [seed]

    # Create a set to hold the URLs that have already been crawled
    crawled = set()

    # Keep crawling until we've reached the maximum number of pages or there are no more pages to crawl
    while tocrawl and len(crawled) < max_pages:
        # Get the next URL to crawl
        page = tocrawl.pop()

        # If we've already crawled this page, skip it
        if page in crawled:
            continue

        # Get the links on the current page
        links = get_links(page)

        # Add the current page to the list of crawled pages
        crawled.add(page)

        # Add the links on the current page to the list of URLs to crawl
        for link in links:
            if link.startswith('http') and link not in crawled:
                tocrawl.append(link)

    return crawled
