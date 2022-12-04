from services.core import BaseWebscraper


class TwoLincolnScraper(BaseWebscraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = 'apartment'
        self.start_url = "https://www.liveattwolincolntower.com/floorplans.aspx"

    def scrape_data(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        xpath = "//*[contains(@data-selenium-id, 'FPRowNum')]"
        tabs = self.driver.find_elements(self.By.XPATH, xpath)

        xpath = "//*[contains(@id, 'FP_Detail')]"
        elements = self.driver.find_elements(self.By.XPATH, xpath)

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
                
            self.time.sleep(1)