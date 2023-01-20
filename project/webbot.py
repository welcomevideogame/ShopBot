from helium import *
from utilities import Utilities

class WebBot:
    headless = False

    def __init__(self):
        self.driver = start_firefox(headless = self.headless)

    def go_to(self, url):
        self.driver.get(url)

    def multi_click(self, path):
        for i in path:
            wait_until(S(i).exists)
            click(S(i))

class MicroCenterBot(WebBot):

    def buy_page(self):
        buy_path = [".col-12 > form:nth-child(1) > div:nth-child(13) > button:nth-child(1)",
                    "div.mb-10:nth-child(12)"]
        
        self.multi_click(buy_path)
        
        inputs = ["#firstname-input", "#lastname-input", "#email-input", "#phone-input"]
        config = Utilities.get_login_config()
        cleaner =  lambda x: x.replace("#", "").replace("-input", "")
        for i in inputs:
            wait_until(S(i).exists)
            write(config[cleaner(i)], into = S(i))

        continue_path = ["#create-account-checkbox", "#contact-submit"]
        self.multi_click(continue_path)
    

    