from os import read
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as us

def khoitao():
    return us.Chrome()

def clickPlay(info,link) :
    user = info.split('|')[0]
    pas = info.split('|')[1]
    driver = khoitao()
    driver.maximize_window()
    driver.get("https://www.bigo.tv/vi/")
    time.sleep(2)
    driver.find_element_by_class_name("head-right__login__btn").click()
    time.sleep(2)
    driver.find_element_by_class_name('right-top-change').click()
    time.sleep(2)
    driver.find_element_by_class_name('CountrySelect-Component').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/header/div[3]/div/div[2]/div/form/div[2]/div/ul/li[230]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/header/div[3]/div/div[2]/div/form/div[4]/div/input').send_keys(user)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/header/div[3]/div/div[2]/div/form/div[6]/input').send_keys(pas)
    time.sleep(2)
    driver.find_element_by_class_name('btn-sumbit').click()
    time.sleep(10)
    driver.get(link)
    time.sleep(1)
    driver.refresh()
    time.sleep(5)
    driver.find_element_by_class_name('vjs-big-play-button').click()
    time.sleep(5)
    driver.close()

