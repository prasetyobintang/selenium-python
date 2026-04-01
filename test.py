from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Browser opened successfully!")

driver.quit()