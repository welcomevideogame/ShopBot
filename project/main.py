from scraper import Scraper

def main():
    url = "https://www.microcenter.com/category/4294967288/laptops-notebooks" # just an example
    scraper = Scraper.MicroCenter(url)
    scraper.scrape_items()
    scraper.print_items()

if __name__ == "__main__":
    main()