from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

def new_chat(user_name):
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_3qx7_"]')
    new_chat.click()

    new_user = chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name)


chrome_browser = webdriver.Chrome(executable_path='D:\Python Projects\chromedriver')
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(15)

user_name_list = ["Roopa", "Twilio", "Ravishankar N S"]

for user_name in user_name_list:
    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        new_chat(user_name)

    message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
    message_box.send_keys('Hi mom this is a test message from python')

    message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    message_box.click()