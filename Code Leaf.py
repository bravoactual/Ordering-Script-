import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.chrome import service
import re

url = "https://www.leafly.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

chrom_path = r"/Users/james/Downloads/chromedriver"
driver = webdriver.Chrome(chrom_path, chrome_options=chrome_options)
# driver.set_window_size(1924, 1050) # choose a resolution big enough

driver.get(url)
sleep(3)

# Legal Age 
driver.find_element_by_xpath('//*[@id="tou-continue"]').click()
sleep(1)

# Search Bar 
driver.find_element_by_xpath('//*[@id = "search-bar"]').click()
sleep(1)

# Type in the search bar 
inputElement = driver.find_element_by_xpath('//*[@id = "search-bar"]')
inputElement.send_keys('Cannabal City Collective')

# Hit Enter 
driver.find_element_by_xpath('//*[@id="search-section"]/div[1]/div/div/form/button/div').click()
sleep(1)

# Click Dispensary
driver.find_element_by_xpath('//*[@id="__next"]/main/div/div[1]/div[2]/div[2]').click()
sleep(1)

# Click Target 
driver.find_element_by_xpath('// *[@id="__next"]/main/div/div[1]/div[3]/div[2]/a/div[2]').click()
sleep(1)
