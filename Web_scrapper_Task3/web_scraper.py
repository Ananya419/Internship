"""
Web Scraper for News Headlines
Scrapes top headlines from a news website and saves them to headlines.txt
"""
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Try to find headlines in <h2> tags
    headlines = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
    # If no <h2> found, try <title> tags (usually only one)
    if not headlines:
        headlines = [title.get_text(strip=True) for title in soup.find_all('title')]
    return headlines

def save_headlines(headlines, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for headline in headlines:
            f.write(headline + '\n')

def main():
    # Example: BBC News homepage
    url = 'https://www.bbc.com/news'
    headlines = fetch_headlines(url)
    save_headlines(headlines, 'headlines.txt')
    print(f"Saved {len(headlines)} headlines to headlines.txt")

if __name__ == "__main__":
    main()
