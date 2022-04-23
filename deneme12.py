from bs4 import BeautifulSoup as bs
import requests
import time
from selenium import webdriver


"""url="https://shiftdelete.net/oyun"
html = requests.get(url).text
soup = bs(html, "lxml")
soup.find_all("div",class_="post-title")        # webscrape kök kod
for i in soup.find_all("div",class_="post-title"):
    a=i.text
    print(a)"""

"""options=webdriver.ChromeOptions()
options.headless=False

browser=webdriver.Chrome(options=options)   #  arkada çalışan selenium
browser.get("https://www.google.com.tr/?hl=tr")
browser.save_screenshot("two.png")
browser.quit()"""



"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


options = webdriver.ChromeOptions()
options.headless = False

browser = webdriver.Chrome(options=options)
browser.get("https://www.instagram.com/")
username=WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password=WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("egemen.svg")
password.send_keys("789EmreSevgi852Qq")

btnSubmit = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
btnSubmit.click()"""

"""usernameInput = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
passwordInput = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
usernameInput.send_keys("egemen.svg")
passwordInput.send_keys("789EmreSevgi852Qq")"""

"""btnSubmit = browser.find_element_by_xpath("//*[@id='loginForm'']/div/div[3]")
btnSubmit.click()
browser.save_screenshot("screenshot31.png")
browser.quit"""
"""list1 = [1, 2, 4]
list2 = [4, 5, 6]
list_difference = []
for item in list1:
  if item not in list2:
    list_difference.append(item)


print(list_difference)

# out = 1,2"""

def fonk(a):
  return a
a=[1,2,3]
for i in fonk(a):
  print(i)