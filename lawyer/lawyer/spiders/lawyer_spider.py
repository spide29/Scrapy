import scrapy
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from scrapy.utils.project import get_project_settings
from selenium.webdriver.chrome.options import Options

class LawyerSpider(scrapy.Spider):
    name = 'hi'

    def start_requests(self):
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.get('https://lso.ca/public-resources/finding-a-lawyer-or-paralegal/directory-search/results')

     
        
        time.sleep(10)
        list1 = []
        list2 = []
        list3 = []
        visited = []

        while True:
            blocks = driver.find_elements(By.CLASS_NAME, "member-listing-name")
            for block in blocks:
                element = block.find_elements(By.TAG_NAME, "a")
                for el in element:
                    list1.append(el.get_attribute("href"))
                    

            for link in list1:
                # Wait for the response to be processed before moving on to the next link
                yield scrapy.Request(link, callback=self.parse_link)

            button = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/section/div/div[2]/div[2]/div[2]/div[3]/button')
            button.click()
            time.sleep(10)
            list1=[]
            
        driver.quit() 

    def parse_link(self, response):
        name = response.css('h2 ::text').extract()
        yield{
            'name':name
           }
        
        
