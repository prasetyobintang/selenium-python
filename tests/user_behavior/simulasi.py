import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Setup driver ===
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-save-password-bubble")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# === Helper ===
def random_delay(a=0.3, b=1.2):
    time.sleep(random.uniform(a, b))

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.15))

def move_and_click(element):
    actions.move_to_element(element).pause(random.uniform(0.2, 0.6)).click().perform()

# === Flow: INVALID LOGIN ===

# Tunggu field muncul dulu (ini penting)
username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

# Isi form (sengaja salah)
human_typing(username, "standard_use")
random_delay()

human_typing(password, "secret_sauce")
random_delay()

# Klik login
login_btn = driver.find_element(By.ID, "login-button")
move_and_click(login_btn)

# Validasi error muncul
error_msg = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
)

print("Error muncul:", error_msg.is_displayed())
print("Isi error:", error_msg.text)

assert "Epic sadface" in error_msg.text