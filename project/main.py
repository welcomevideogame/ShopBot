from scraper import Scraper

def main():
    mc_scraper = Scraper.MicroCenter()
    while True:
        url = input("Enter a url to scrape: ")
        if "microcenter" in url:
            mc_scraper.set_url(url)
            mc_scraper.scrape_items()
            mc_scraper.print_items()
        elif url == "0":
            break
        else:
            print("Url not supported.")

if __name__ == "__main__":
    main()