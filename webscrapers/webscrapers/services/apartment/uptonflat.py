from services.core import BaseWebscraper

class UptonflatScraper(BaseWebscraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = 'apartment'
        self.start_url = 'https://www.uptonflats.com/floorplans'
        self.features = ['Name', 'Beds', 'Baths', 'SqFt', ' Availability', 'Rent', 'Deposit' ]
        self.clean_features = ["floorplan", "bedrooms", "baths", "size", "available", "rent", "deposit" ]
        
    def get_data(self, row, features):
        data = {}
        for clean_feature, feature in zip(self.clean_features, features):
            xpath = f'//*[contains(@data-selenium-id, "Floorplan{row}{feature}")]'
            value = self.driver.find_element(self.By.XPATH, xpath).text
            data[clean_feature] = value
        return data
        
        
    def scrape_data(self):
        # close pop-up
        xpath = '//button[contains(@class, "position-absolute")]'
        self.driver.find_elements(self.By.XPATH, xpath)
        close_button = self.driver.find_element(self.By.XPATH, xpath)
        close_button.click()
        
        # scroll
        self.scroll_page()
        
        # click toggle
        xpath = '//a[contains(@aria-controls, "floorPlanAccordion_2")]'
        twobedtoggle = self.driver.find_element(self.By.XPATH, xpath)
        twobedtoggle.click()
        
        # scroll
        self.scroll_page()
        
        # collect cards
        xpath = '//*[@id="fp-container"]//*[contains(@id, "fp-container")]'
        cards = self.driver.find_elements(self.By.XPATH, xpath)
        
        # get data
        for i in range(len(cards)):
            data = self.get_data(i, self.features)
            data["company"] = "UptonFlat"
            yield data
        
            
    