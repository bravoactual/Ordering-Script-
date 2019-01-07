import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.chrome import service
import re

url = "https://www.dutchie.com/dispensaries/cannabal-city-collective-los-angeles/menu"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

chrom_path = r"/Users/james/Downloads/chromedriver"
driver = webdriver.Chrome(chrom_path, chrome_options=chrome_options)
# driver.set_window_size(1924, 1050) # choose a resolution big enough

driver.get(url)
sleep(3)

# navigate to the specified product : just add the name
driver.find_element_by_partial_link_text('3C INDICA HOUSE MIX').click()
sleep(3)

# select the desired 1/2 OZ
weight_css_selector = '.product-modal__AddToCartContainer-sc-1xb83zk-9 > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
driver.find_element_by_css_selector(weight_css_selector).click()
desired_weight_css_selector = '.product-modal__AddToCartContainer-sc-1xb83zk-9 > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > select:nth-child(1) > option:nth-child(3)'
driver.find_element_by_css_selector(desired_weight_css_selector).click()
sleep(2)
#######
# select the desired quantity
quantity_css_selector = '.product-modal__AddToCartContainer-sc-1xb83zk-9 > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)'
driver.find_element_by_css_selector(quantity_css_selector).click()
desired_quantity_css_selector = '.product-modal__AddToCartContainer-sc-1xb83zk-9 > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2) > select:nth-child(1) > option:nth-child(2)'
driver.find_element_by_css_selector(desired_quantity_css_selector).click()
sleep(2)

# add to cart
add_to_cart_css_selector = '.product-modal__AddToCartContainer-sc-1xb83zk-9 > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(3)'
driver.find_element_by_css_selector(add_to_cart_css_selector).click()
sleep(2)

# Select Pick Up
driver.find_element_by_css_selector('body > div:nth-child(22) > div > div > div.styles__ButtonContainer-sc-1edagdx-2.ghJraX.sc-bwzfXH.hKiLMS.sc-bdVaJa.gMYdSF').click()
sleep(2)

# click on cart
driver.find_element_by_css_selector(
    '#navigation-container > div > div.navigation__UserCartContainer-sc-18zpigd-9.jqRiWr.sc-bwzfXH.kkVFCe.sc-bdVaJa.iHZvIS > div.icon__CartIcon-sc-4qy5kh-0.eoUoeu.sc-bdVaJa.iHZvIS').click()
sleep(2)
# proceed to checkout
driver.find_element_by_xpath('//button[text()="Proceed to Checkout - $"]').click()
sleep(2)
# Checkout as guest
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[5]/a').click()
sleep(4)
########################################################
# Filling the form :

# filling first name
First_name_css_selector = 'input.text-input-k2ughi-0:nth-child(1)'
First_name = driver.find_element_by_css_selector(First_name_css_selector)
First_name.send_keys('type first name here')
# filling last name
Last_name_css_selector = 'input.cfxgXT:nth-child(2)'
Last_name = driver.find_element_by_css_selector(Last_name_css_selector)
Last_name.send_keys('type last name here')
# filling Phone number
Phone_nu_css_selector = '.text-input-k2ughi-0-Component'
Phone_nu = driver.find_element_by_css_selector(Phone_nu_css_selector)
Phone_nu.send_keys('1234567891 ')
# Birth day
month_xpath = '//*[@id="top-scroll-container"]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/span/select'
select_month = Select(driver.find_element_by_xpath(month_xpath))
select_month.select_by_value('12')
day_xpath = '//*[@id="top-scroll-container"]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/span/select'
select_day = Select(driver.find_element_by_xpath(day_xpath))
select_day.select_by_value('17')
year_xpath = '//*[@id="top-scroll-container"]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/span/select'
select_year = Select(driver.find_element_by_xpath(year_xpath))
select_year.select_by_value('2018')
# choosing Credit
choosing_cash_box_xpath = '//*[@id="top-scroll-container"]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/label[2]/input'
driver.find_element_by_xpath(choosing_cash_box_xpath).click()
