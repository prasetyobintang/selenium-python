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
from selenium.common.exceptions import TimeoutException

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
# actions = ActionChains(driver)

# === Helper ===
def random_delay(a=0.3, b=1.0):
    time.sleep(random.uniform(a, b))

def human_typing(element, text, typo_chance=0.1):
    for char in text:
        if random.random() < typo_chance:
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            element.send_keys(wrong_char)
            time.sleep(random.uniform(0.05, 0.15))
            element.send_keys("\b")  # backspace
            time.sleep(random.uniform(0.05, 0.15))
        
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

def move_and_click(driver, element):
    ActionChains(driver)\
        .move_to_element(element)\
        .pause(random.uniform(0.2, 0.5))\
        .click()\
        .perform()

def check_navigation_type(label):
    nav_type = driver.execute_script(
        "return performance.getEntriesByType('navigation')[0].type"
    )
    print(f"{label}: {nav_type}")
    
def random_scroll(driver):
    scroll_amount = random.randint(100, 400)
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(random.uniform(0.3, 0.8))    
    
def scroll_to_footer(driver, wait):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # scroll ke bawah
        scroll_step = random.choice([150, 250, 400, 600])
        pause = random.choice([0.3, 0,6, 1.2])
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")
        time.sleep(random.uniform(0.4, 1.0))

        # cek footer muncul
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer_copy")))
            return footer
        except:
            pass
        
        # cek udah mentok
        new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
        if new_height >= last_height:
            break

def click_twitter_footer(driver, wait):
    twitter = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "social_twitter")))
    
    # scroll ke twitter dulu
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twitter)
    time.sleep(random.uniform(0.5, 1.0))

    # tunggu keliatan
    try:
        ActionChains(driver)\
            .move_to_element(twitter)\
            .pause(random.uniform(0.3, 0.7))\
            .click()\
            .perform() 
    except:            
        # fallback klik biasa
        driver.execute_script("arguments[0].click();", twitter)
    time.sleep(random.uniform(0.5, 1.2))
    
    # klik
    # twitter.click()  
    
# === STEP 1: INVALID LOGIN ===
print("\n=== STEP 1: INVALID LOGIN ===")

username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

human_typing(username, "standard_used")  # sengaja salah
random_delay()

human_typing(password, "secret_sauce")
random_delay()

login_btn = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")
move_and_click(driver, login_btn)

time.sleep(1)

print("URL setelah login gagal:", driver.current_url)
check_navigation_type("After invalid login")

# === STEP 2: REFRESH OBSERVATION ===
print("\n=== STEP 2: REFRESH OBSERVATION ===")

check_navigation_type("Before refresh")

# kasih marker visual (opsional tapi satisfying 😏)
driver.execute_script("""
let div = document.createElement('div');
div.innerText = 'Check Refresh';
div.style.position = 'fixed';
div.style.top = '50%';
div.style.left = '50%';
div.style.transform = 'translate(-50%, -50%)';
div.style.fontSize = '50px';
div.style.color = 'red';
div.style.zIndex = '9999';
document.body.appendChild(div);
""")
time.sleep(2)

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

login_btn = driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")
move_and_click(driver, login_btn)

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

# === STEP 5: SCROLL & INTERACT ===
print("\n=== STEP 5: SCROLL & INTERACT ===")

scroll_to_footer(driver, wait)
random_delay()

click_twitter_footer(driver, wait)

driver.switch_to.window(driver.window_handles[-1])  # pindah ke tab baru
time.sleep(random.uniform(1.0, 2.0))

print("Klik Twitter footer, URL sekarang:", driver.current_url)

# === STEP 6: MAKE SURE DI TWITTER ===
# Cek URL dan bio twitter dan double click bio buat highlight (biar keliatan)
print("\n=== STEP 6: MAKE SURE DI TWITTER ===")
try:
    bio_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='UserDescription']")))
    bio_text = bio_element.text
    
    # === EXPERIMENT ===: double click highlight (disabled for stability) ===
    # ActionChains(driver).double_click(bio_element).perform()
    # time.sleep(random.uniform(0.5, 1.0))
    
except TimeoutException:
    bio_text = "Gagal ambil bio Twitter"

print(f"Bio Twitter: {bio_text}")

# === DONE ===
driver.quit()