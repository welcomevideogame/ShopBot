from scraper import Scraper
import os
from utilities import Utilities
from webbot import WebBot
import string

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
        options = {"Sort by price": False, "Filter out store only": False, "Filter out of stock": False, "Filter brands": False, "Simple view": False, "Show warnings": True, "Buy Item": False}
        scraper = Scraper.MicroCenter()
        scraper.set_url(self.url)
        pagination = self.check_pagination()
        scraper.scrape_items(pagination)

        brands = {brand: False for brand in scraper.get_brands()}

        total_items = scraper.get_product_count()
        if not total_items:
            print("No items found.")
            return

        while True:
            os.system('cls')
            for option in options:
                print("[" + str(list(options).index(option) + 1) + "] " + option + ": " + str(options[option]))
                if option == "Filter brands":
                    if options[option]:
                        for i, brand in enumerate(brands):
                            print(f"\t[{list(string.ascii_uppercase)[i]}] {brand} : {str(brands[brand])}")
            choice = input("Enter a number to toggle an option: ")
            if choice:
                if choice.isnumeric():
                    choice = int(choice)
                    choice -= 1
                    if choice in range(len(options)):
                        options[list(options)[choice]] = not options[list(options)[choice]]
                else:
                    choice = choice.upper()
                    if choice in string.ascii_uppercase:
                        choice = list(string.ascii_uppercase).index(choice)
                        if choice in range(len(brands)):
                            brands[list(brands)[choice]] = not brands[list(brands)[choice]]
            else:
                break
        if options["Show warnings"]:
            if not pagination:
                print("Warning: No Pagination detected. It is recommended to use a link with pagination.\nPress enter to continue.")
                input()

        new_brands = [brand for brand in brands if brands[brand]]
        scraper.print_items(options, new_brands)
        save = input("Save to csv? (y/n): ").upper()
        if save == "Y":
            filename = input("Enter a filename: ")
            Utilities.save_to_csv(filename, scraper.products)

        if options["Buy Item"]:
            choice = input("Enter the number of the item you want to buy: ")
            if choice.isnumeric() and choice in range(len(scraper.products)):
                print("Opening browser...")
                bot = WebBot()
                bot = bot.MicroCenterBot()
                bot.go_to(scraper.products[choice + 1]["url"])
            else:
                input("Invalid choice.")


        scraper.clear_items()

    def check_pagination(self):
        return "page=" in self.url