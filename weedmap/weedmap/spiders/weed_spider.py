# import scrapy
# from ..items import WeedmapItem
# import pandas as pd
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Chrome, ChromeOptions
# from scrapy.utils.project import get_project_settings
# from selenium.webdriver.chrome.options import Options

# class WeedSpider(scrapy.Spider):
#     name = 'hi'

#     def start_requests(self):
#         settings = get_project_settings()
#         driver_path = settings.get('CHROME_DRIVER_PATH')
#         options = ChromeOptions()
#         options.headless = True
#         driver = webdriver.Chrome(executable_path=driver_path, options=options)
#         driver.get('https://weedmaps.com/dispensaries/in/united-states/california/lake-forest')

     
#         links = []

#         div = driver.find_elements(By.CLASS_NAME, 'eQOCGV')
#         for d in div:
#             link_els = d.find_elements(By.TAG_NAME, 'a')
#             for link_el in link_els:
#                 href = link_el.get_attribute('href')
#                 links.append(href)
                
#         for link in links:
#             yield scrapy.Request(url=link, callback=self.parse)

#         driver.quit()
                

#     def parse(self, response, **kwargs):
#             items = WeedmapItem()
#             title  = response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[1]/h1/text()').extract()
#             star= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[3]/a/div/div[1]/text()').extract()
#             rating= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[3]/a/div/div[2]/text()').extract()
#             name= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/text()').extract()
#             # co= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/text()').extract()
#             medical= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div/text()').extract()
#             order= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[5]/text()').extract()
#             phone= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[3]/a[1]/div[2]/text()').extract()

#             items['title'] = title
#             items['star'] = star
#             items['rating'] = rating
#             items['name'] = name
#             # items['co'] = co
#             items['medical'] = medical
#             items['order'] = order
#             items['phone'] = phone

#             yield items
        
##############################################################


# import scrapy
# from ..items import WeedmapItem
# class QuoteSpider(scrapy.Spider):
#     name = 'hi'
#     start_urls = ['https://weedmaps.com/dispensaries/cannabaska']

#     def parse(self, response, **kwargs):
#         di = response.css('div.iECFKK')
#         items = WeedmapItem()
#         for tag in di:
#             title  = tag.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[1]/h1/text()').extract()
#             items['title'] = title
#             yield items

##############################################################

import scrapy
from ..items import WeedmapItem
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from scrapy.utils.project import get_project_settings
from selenium.webdriver.chrome.options import Options

class WeedSpider(scrapy.Spider):
    name = 'hi'

    def start_requests(self):
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.get('https://weedmaps.com/dispensaries/in/united-states/california/lake-forest')

     
        
        links = []
        disp=[]
        temp=[]
        vvisited=[]
        h1_list = []
        price_list = []

        while True:
            div = driver.find_elements(By.CLASS_NAME, 'eQOCGV')
            for d in div:
                link_els = d.find_elements(By.TAG_NAME, 'a')
                for link_el in link_els:
                    href = link_el.get_attribute('href')
                    disp.append(href)
                    
            blocksss = driver.find_elements(By.CLASS_NAME,'kmGAHV')
            for blockss in blocksss:
                block = blockss.find_elements(By.CLASS_NAME,'cVQPKf')
            for href in block:
                temp.append(href.get_attribute("href"))
                
            if temp[1] is None:
                temp=[]
                vvisited.extend(disp)
                disp=[]
                break
            else:
                driver.get(temp[1])
                temp=[]
                vvisited.extend(disp)
                disp=[]
        for links in vvisited:
            time.sleep(2)
            yield scrapy.Request(url=links, callback=self.parse)

        driver.quit()
                

    def parse(self, response, **kwargs):
            items = WeedmapItem()
            title  = TariffItem
            star= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[3]/a/div/div[1]/text()').extract()
            rating= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[3]/a/div/div[2]/text()').extract()
            add = response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[3]/span/text()').extract()
            name= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/text()').extract()
            # co= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/text()').extract()
            medical= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div/text()').extract()
            order= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[5]/text()').extract()
            phone= response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[3]/a[1]/div[2]/text()').extract()

            items['title'] = title
            items['star'] = star
            items['rating'] = rating
            items['add'] = add
            items['name'] = name
            # items['co'] = co
            items['medical'] = medical
            items['order'] = order
            items['phone'] = phone
            
            yield items
   









        
        
