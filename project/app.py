from scraper import Scraper
import os
from utilities import Utilities

class App:

    url = None

    def __init__(self):
        
        while True:
            self.url = input("Enter a url to scrape: ")
            if "microcenter" in self.url:
                self.microcenter()
            elif self.url == "0":
                break
            else:
                print("Url not supported.")

    def microcenter(self):
        options = {"Sort by price": False, "Filter out store only": False, "Filter out of stock": False, "Simple view": False, "Show warnings": True}
        scraper = Scraper.MicroCenter()
        scraper.set_url(self.url)
        pagination = self.check_pagination()
        scraper.scrape_items(pagination)

        while True:
            os.system('cls')
            for option in options:
                print("[" + str(list(options).index(option) + 1) + "] " + option + ": " + str(options[option]))
            
            choice = input("Enter a number to toggle an option: ")
            choice = Utilities.try_parse_int(choice)
            if choice:
                choice -= 1
                if choice in range(len(options)):
                    options[list(options)[choice]] = not options[list(options)[choice]]
            else:
                break
        if options["Show warnings"]:
            if not pagination:
                print("Warning: No Pagination detected. It is recommended to use a link with pagination.\nPress enter to continue.")
                input()
        scraper.print_items(options)
        save = input("Save to csv? (y/n): ").upper()
        if save == "Y":
            filename = input("Enter a filename: ")
            Utilities.save_to_csv(filename, scraper.products)
        scraper.clear_items()

    def check_pagination(self):
        return "page=" in self.url