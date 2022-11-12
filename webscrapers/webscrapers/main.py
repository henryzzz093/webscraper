import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

import requests


class BaseWebscraper:
    def __init__(self, *args, **kwargs):
        self.start_url = None

    def connect(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920, 1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        )
        self.driver = webdriver.Remote(
                    command_executor="http://host.docker.internal:4444/wd/hub",
                    options=chrome_options,
                )
        
    def scrape_data(self):
        pass
    
    def load_data(self, data):
        url = "http://host.docker.internal:8000/api/apartments/"
        try:
            response = requests.post(url, json=data)
            print(response.json())
        except Exception as e:
            print(e)
            print(response)
            print(data)
        

    def run(self):
        print(f"Scraping: {self.start_url}")
        self.connect()
        self.driver.get(self.start_url)
        for row in self.scrape_data():
            print(row)
            self.load_data(row)



class BravernScraper(BaseWebscraper):
    def __init__(self, *args, **kwargs):
        self.start_url = "https://www.thebravernapts.com/floorplans"
    
    def scrape_data(self):
        xpath = '//*[@id="floorplans-container"]//*[contains(@id, "fp-container")]'
        for element in self.driver.find_elements(By.XPATH, xpath):
            row = element.text.split("\n")
            
            yield {
                "company": "The Bravern",
                "floorplan": row[0],
                "available": row[4],
                "bedrooms": row[1],
                "baths": row[2],
                "size": row[3],
                "rent": row[5],
                "deposit": row[6],
            }


class TwoLincolnScraper(BaseWebscraper):
    def __init__(self, *args, **kwargs):
        self.start_url = "https://www.liveattwolincolntower.com/floorplans.aspx"

    def scrape_data(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        xpath = "//*[contains(@data-selenium-id, 'FPRowNum')]"
        tabs = self.driver.find_elements(By.XPATH, xpath)

        xpath = "//*[contains(@id, 'FP_Detail')]"
        elements = self.driver.find_elements(By.XPATH, xpath)

        for i, tab in enumerate(tabs[:-1]):
            tab.click()
        
            row = elements[i].text.split("\n")
            yield {
                "company": "Two Lincoln",
                "floorplan": row[0],
                "available": row[1],
                "bedrooms": row[2],
                "baths": row[3],
                "size": row[4],
                "rent": row[5],
                "deposit": row[6],
            }
                
            time.sleep(1)
            

def webscraper_factory(scraper):
    action_class = None
    match scraper:
        case "bravern":
            action_class = BravernScraper()
        case "two_lincoln":
            action_class = TwoLincolnScraper()
        
    return action_class


if __name__ == "__main__":
    scraper = os.getenv("SCRAPER")
    
    print(scraper.upper())
    
    scraper = webscraper_factory(scraper)

    print("Running Webscraper!")
    scraper.run()
    print("Scraping job completed!")
    
    