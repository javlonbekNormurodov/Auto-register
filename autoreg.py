# AUTO REGISTER
from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver")
browser.get("https://phptravels.com/")
chrome = webdriver.Chrome("./chromedriver")
print(browser.title)

browser.fullscreen_window()
time.sleep(1)

loginButton = browser.find_element_by_xpath("/html/body/header/div/nav/a[6]")
loginButton.click()
chrome.get("https://phptravels.org/index.php?rp=/login")
chrome.fullscreen_window()
usernameButton = chrome.find_element_by_xpath("//*[@id='inputEmail']")
passwordButton = chrome.find_element_by_xpath("//*[@id='inputPassword']")
time.sleep(2)
usernameButton.send_keys("Username@gmail.com")
passwordButton.send_keys("password")
time.sleep(1)
chrome.find_element_by_xpath("//*[@id='login']").click()
