from services.core import BaseWebscraper


class BravernScraper(BaseWebscraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = 'apartment'
        self.start_url = "https://www.thebravernapts.com/floorplans"
    
    def scrape_data(self):
        xpath = '//*[@id="floorplans-container"]//*[contains(@id, "fp-container")]'
        for element in self.driver.find_elements(self.By.XPATH, xpath):
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