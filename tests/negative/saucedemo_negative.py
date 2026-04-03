# import lib/dependency yang dibutuhkan
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# setup options untuk webdriver
options = Options()
# Matikan password manager & warning
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})
# Flag penting
options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding")
# Optional tapi bantu bikin clean
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-notifications")

# setup webdriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# set default matikan javascript untuk mempercepat loading page
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

try:
    # list array credential yang akan diuji dan validasi login gagal
    credentials = [
        ("locked_out_user", "secret_sauce", False, "Epic sadface: Sorry, this user has been locked out."),
        ("problem_user", "secret_sauce", True, "Login berhasil, bug pada inventory"),
        ("performance_glitch_user", "secret_sauce", True, "Login berhasil, tapi loading lama"),
        ("error_user", "secret_sauce", True, "Login berhasil, fitur tidak berfungsi"),
        ("visual_user", "secret_sauce", True, "Login berhasil, tapi tampilan berantakan"),
        ("admin", "admin", False, "Epic sadface: Username and password do not match any user in this service"),
        ("!@#", "#@!", False, "Epic sadface: Username and password do not match any user in this service")
    ]
    
    for username, password, should_login, expected_message in credentials:
        print(f"\nTesting credential: {username} Expected login: {should_login} message: {expected_message}")
        
        # buka website
        driver.get("https://www.saucedemo.com/")
        # tunggu sampai website selesai dimuat
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")) and EC.url_contains("saucedemo.com"))
        # hapus cookies untuk memastikan tidak ada sesi yang tersisa
        driver.delete_all_cookies()
        
        # input credential
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        # wait biar nggak flaky
        wait = WebDriverWait(driver, 5)
        
        login_success = False
        
        try:
            wait.until(EC.url_contains("/inventory.html"))
            login_success = True
        except:
            login_success = False
            
        # Validasi hasil login sesuai ekspektasi
        if login_success == should_login:
            print(f"Sesuai ekspektasi: {username}")
        else:
            print(f"Tidak sesuai ekspektasi: {username}")
            
finally:
    driver.quit()