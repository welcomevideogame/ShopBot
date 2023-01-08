from scraper import Scraper
import os
from utilities import Utilities

def main():
    mc_scraper = Scraper.MicroCenter()
    options = {"Sort by price": False, "Filter out store only": False}
    while True:
        url = input("Enter a url to scrape: ")
        if "microcenter" in url:
            mc_scraper.set_url(url)
            mc_scraper.scrape_items()
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
            mc_scraper.print_items(options)
            mc_scraper.clear_items()
        elif url == "0":
            break
        else:
            print("Url not supported.")

if __name__ == "__main__":
    main()