from selenium import webdriver
from selenium.webdriver import ChromeOptions
import json

class Bot:

    def __init__(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.page_load_strategy = 'eager'
        options.add_argument("user-data-dir=./profile")
        self.driver = webdriver.Chrome(options=options)
        with open('config/config.json') as f:
            data = json.load(f)
            self.base_url = data['base_url']
