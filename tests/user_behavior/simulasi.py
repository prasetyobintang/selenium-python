# === Simulasi User Behavior: Login dan Refresh ===

# === Import Libraries Dependend===
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
def random_delay(a=0.3, b=1.0):
    time.sleep(random.uniform(a, b))

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.15))

def move_and_click(element):
    actions.move_to_element(element).pause(random.uniform(0.2, 0.5)).click().perform()

def check_navigation_type(label):
    nav_type = driver.execute_script(
        "return performance.getEntriesByType('navigation')[0].type"
    )
    print(f"{label}: {nav_type}")

# === STEP 1: INVALID LOGIN ===
print("\n=== STEP 1: INVALID LOGIN ===")

username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

human_typing(username, "standard_used")  # sengaja salah
random_delay()

human_typing(password, "secret_sauce")
random_delay()

login_btn = driver.find_element(By.ID, "login-button")
move_and_click(login_btn)

time.sleep(1)

print("URL setelah login gagal:", driver.current_url)
check_navigation_type("After invalid login")

# === STEP 2: REFRESH OBSERVATION ===
print("\n=== STEP 2: REFRESH OBSERVATION ===")

check_navigation_type("Before refresh")

# kasih marker visual (opsional tapi satisfying 😏)
driver.execute_script("document.body.style.background = 'red'")
time.sleep(1)

driver.refresh()

time.sleep(2)

check_navigation_type("After refresh")

# === STEP 3: VALID LOGIN ===
print("\n=== STEP 3: VALID LOGIN ===")

username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

username.clear()
password.clear()

human_typing(username, "standard_user")
random_delay()

human_typing(password, "secret_sauce")
random_delay()

login_btn = driver.find_element(By.ID, "login-button")
move_and_click(login_btn)

# tunggu inventory muncul
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

print("Login sukses, URL:", driver.current_url)
check_navigation_type("After valid login")

# === STEP 4: REFRESH SETELAH LOGIN ===
print("\n=== STEP 4: REFRESH SETELAH LOGIN ===")

check_navigation_type("Before refresh (inventory)")

driver.refresh()

time.sleep(2)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

check_navigation_type("After refresh (inventory)")

print("Masih di inventory:", driver.current_url)

# === DONE ===
driver.quit()