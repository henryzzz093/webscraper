from services.core import BaseWebscraper
import time

class BookingFlightScraper(BaseWebscraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = 'airline'
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        self.start_url = f'https://flights.booking.com/flights/SEA.CITY-LAS.CITY/?type=ROUNDTRIP&adults=1&cabinClass=ECONOMY&children=&from=SEA.CITY&to=LAS.CITY&fromCountry=US&toCountry=US&fromLocationName=Seattle&toLocationName=Las+Vegas&depart={start_date}&return={end_date}&sort=BEST&travelPurpose=leisure&aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaLQCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKx7OmbBsACAdICJGVhZjJmMDRhLTA1MmQtNGY0OC1iNjUwLTNkM2NlMjNkM2E2YtgCBeACAQ'


    def get_data(self, card):
        xpath = './child::*//*[contains(@data-test-id, "flight_card_price_main_price")]'
        price = card.find_element(self.By.XPATH, xpath).text
        xpath =  xpath = './child::*//*[contains(@data-testid, "flight_card_carriers_carrier")]'
        airline = card.find_element(self.By.XPATH, xpath).text
        xpath = './child::*//*[contains(@data-testid, "flight_card_segment_departure_time")]'
        departure_time = card.find_element(self.By.XPATH, xpath).text
        xpath = './child::*//*[contains(@data-testid, "flight_card_segment_destination_time")]'
        destination_time = card.find_element(self.By.XPATH, xpath).text
        xpath = './child::*//*[contains(@data-testid, "flight_card_segment_stops")]'
        stops = card.find_element(self.By.XPATH, xpath).text
        xpath = './child::*//*[contains(@data-testid, "flight_card_segment_duration")]'
        duration = card.find_element(self.By.XPATH, xpath).text

        data = {}

        data['price'] = price
        data['airline'] = airline
        data['departure_time'] = departure_time
        data['destination_time'] = destination_time
        data['stops'] = stops
        data['duration'] = duration
        data['company'] = airline

        return data
        #yield data

    

    def get_cards(self):
        xpath = '//*[contains(@id, "flight-card")]'
        list_of_cards = self.driver.find_elements(self.By.XPATH, xpath)
        return list_of_cards
    
    
    def next_page_active(self):
        xpath = '//button[contains(@aria-label, "Next")]'
        next_page = self.driver.find_element(self.By.XPATH, xpath)
        return next_page.is_enabled()
    
    
    def scrape_data(self):


        # wait for page fully loaded 
        print('sleeping')
        self.time.sleep(20)
        print('ready to scroll page')
        self.scroll_page()
        print('getting data')

        for card in self.get_cards():
            yield self.get_data(card)
        
        while self.next_page_active():
            self.click_next_page()
            print('sleeping')
            self.time.sleep(5)
            print('ready to scroll page')
            self.scroll_page()
            print('getting data')

            for card in self.get_cards():
                yield self.get_data(card)
            

    def click_next_page(self):
        xpath = '//button[contains(@aria-label, "Next")]'
        next_page = self.driver.find_element(self.By.XPATH, xpath)
        next_page.click()
        
            
    

