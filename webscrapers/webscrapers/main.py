import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
import argparse 
from ast import literal_eval

import requests

from services import apartment, airline

def webscraper_factory(service, scraper, **kwargs):
    action_class = None

    match service:
        case "airline":
            match scraper:
                case "booking":
                    action_class = airline.BookingFlightScraper(**kwargs)


        case "apartment":
            match scraper:
                case "bravern":
                    action_class = apartment.BravernScraper(**kwargs)
                case "two_lincoln":
                    action_class = apartment.TwoLincolnScraper(**kwargs)
                case "uptonflat":
                    action_class = apartment.UptonflatScraper(**kwargs)
                
    return action_class


if __name__ == "__main__":
    cli = argparse.ArgumentParser()
    arguments = {"--scraper":str, "--service":str, "--kwargs":str}
    for key, value in arguments.items():
        cli.add_argument(key, type = value)
    
    args = cli.parse_args()
    print(args.kwargs)

    kwargs = literal_eval(args.kwargs)

    print(args.scraper)
    print(args.service)
    print(args.kwargs)
    print(kwargs)
    
    scraper = webscraper_factory(args.service, args.scraper, **kwargs)

    print("Running Webscraper!")
    scraper.run()
    print("Scraping job completed!")
    
    