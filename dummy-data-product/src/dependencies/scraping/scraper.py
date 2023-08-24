import requests
from bs4 import BeautifulSoup

class WorldBankScraper:
    def __init__(self):
        self.base_url = "https://etenders.gov.in/eprocure/app"

    def scrape_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            tender_elements = soup.find_all("div", class_="views-row")
            tenders = []

            for element in tender_elements:
                tender = {
                    "title": element.find("h2").text.strip(),
                    "description": element.find("div", class_="views-field-field-short-description").text.strip(),
                    "date": element.find("div", class_="views-field-field-issue-date").text.strip()
                }
                tenders.append(tender)

            return tenders
        else:
            print("Failed to fetch data")
            return None

if __name__ == "__main__":
    scraper = WorldBankScraper()
    scraped_data = scraper.scrape_data()
    if scraped_data:
        for tender in scraped_data:
            print("Title:", tender["title"])
            print("Description:", tender["description"])
            print("Date:", tender["date"])
            print("-" * 50)
