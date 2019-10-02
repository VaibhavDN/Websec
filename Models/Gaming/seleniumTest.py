from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.giantbomb.com/")
print(driver.title)
html = driver.page_source
print(html)
driver.close()