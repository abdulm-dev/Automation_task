import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tripshepherd.com/")
city_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"hero\"]/div[1]/button")))
city_option.click()
time.sleep(2)
austin_checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Austin']")))
austin_checkbox.click()
time.sleep(2)
private_tour = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Private Tours']")))
private_tour.click()
time.sleep(2)
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/tours/private-tour-of-austin']")))
element.click()
time.sleep(10)

driver.quit()
