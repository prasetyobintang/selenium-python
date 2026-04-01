from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # buka website
    driver.get("https://www.saucedemo.com/")

    # verifikasi title
    assert "Swag Labs" in driver.title

    # isi login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # klik login
    driver.find_element(By.ID, "login-button").click()

    # tunggu sampai pindah halaman (biar gak flaky)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))

    # verifikasi login berhasil
    if "inventory" in driver.current_url:
        print("Login berhasil, berada di halaman inventory 😌")
    else:
        print("Login gagal, tidak berada di halaman inventory 😭")

finally:
    # tutup browser
    driver.quit()