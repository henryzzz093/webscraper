import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

import requests


class BaseWebscraper:
    def __init__(self, *args, **kwargs):
        self.start_url = None
        self.By = By
        self.time = time
        self.service = None

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

    def scroll_page(self, speed=8):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.driver.execute_script(f"window.scrollTo(0, {current_scroll_position});")
            new_height = self.driver.execute_script("return document.body.scrollHeight")
    
    def load_data(self, data):
        url = f"http://host.docker.internal:8000/api/{self.service}/"
        try:
            response = requests.post(url, json=data)
            #print(response.json())
        except Exception as e:
            print(e)
            print(response)
            #print(data)
    
        

    def run(self):
        print(f"Scraping: {self.start_url}")
        self.connect()
        self.driver.get(self.start_url)
        for row in self.scrape_data():
            print(row)
            self.load_data(row)