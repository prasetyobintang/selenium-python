# import lib/dependency yang dibutuhkan
from modulefinder import test
from faker import Faker

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

# setup faker
faker = Faker()

# setup webdriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# print(driver.service.path) # cek path chromedriver

# set default matikan javascript untuk mempercepat loading page
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

try: 
    # buka website
    driver.get("https://www.saucedemo.com/")
    # tunggu sampai website selesai dimuat
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
    
    # input valid credential
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # wait sampai elemen terpenuhi
    wait = WebDriverWait(driver, 5)

    # validasi login
    try:
        wait.until(EC.url_contains("/inventory.html"))
        print(f"Login berhasil, URL saat ini: {driver.current_url}")
    except:
        if "saucedemo.com" in driver.current_url:
            print(f"Login gagal, URL saat ini: {driver.current_url}")
        else: 
            print(f"Login gagal dengan kondisi tidak terduga, URL saat ini: {driver.current_url}")
            
    # validasi inventory page dengan item
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
    
    # ambil text semua item
    # item_names = [item.text for item in items]
    # print(f"Nama item yang ditemukan: {item_names}")
    
    # validasi item tertentu opsional
    # expected_items= [
    #     "Sauce Labs Backpack", 
    #     "Sauce Labs Bike Light"
    # ]
    
    # for expected in expected_items:
    #     if expected in item_names:
    #         print(f"Item ditemukan: {expected}")
    #     else:
    #         print(f"Item tidak ditemukan: {expected}")
    
    # sesi pilih item dan validasi keranjang
    item_name = "Sauce Labs Backpack"
    
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    
    selected_price = None
    
    for item in items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        if name == item_name:
            selected_price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            item.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            print(f"Item dipilih: {name} dengan harga: {selected_price}")
            break
        
    # sesi cek keranjang
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    cart_item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    
    if cart_item == item_name:
        print(f"Item di keranjang sesuai dengan yang dipilih: {cart_item}")
    else:   
        print(f"Item di keranjang tidak sesuai dengan yang dipilih: {cart_item}")    
        
    # sesi checkout dan validasi form checkout dengan data faker
    # validasi page berada di /cart.html
    try:
        wait.until(EC.url_contains("/cart.html"))
        print(f"Berada di halaman keranjang, URL saat ini: {driver.current_url}")
    except:
        print(f"Belum berada di halaman keranjang, URL saat ini: {driver.current_url}")

    driver.find_element(By.ID, "checkout").click()
    
    # validasi page berada di /checkout-step-one.html
    try:
        wait.until(EC.url_contains("/checkout-step-one.html"))
        print(f"Berada di halaman checkout, URL saat ini: {driver.current_url}")
    except:
        print(f"Belum berada di halaman checkout, URL saat ini: {driver.current_url}")
        
    first_name = faker.first_name()
    last_name = faker.last_name()
    postal_code = faker.postcode()
    
    driver.find_element(By.ID, "first-name").send_keys(first_name)    
    driver.find_element(By.ID, "last-name").send_keys(last_name)    
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    print(f"Data checkout diisi: {first_name} {last_name} {postal_code}")
    driver.find_element(By.ID, "continue").click()
    
    # sesi validasi dan cek harga di halaman checkout
    item_total = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_subtotal_label"))).text
    print(f"Total harga item: {item_total}")
    item_tax = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_tax_label"))).text
    print(f"Total pajak: {item_tax}")
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    print(f"Total keseluruhan: {total}")
    
    # ambil angka
    item_total_value = float(item_total.split("$")[1])
    item_tax_value = float(item_tax.split("$")[1])
    total_value = float(total.split("$")[1])
    
    if round(item_total_value + item_tax_value, 2) == round(total_value, 2):
        print("Perhitungan harga valid: Total item + pajak sesuai dengan total keseluruhan")
    else:
        print("Perhitungan harga tidak valid: Total item + pajak tidak sesuai dengan total keseluruhan")
        
    # sesi validasi konfirmasi order
    driver.find_element(By.ID, "finish").click()
    
    success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
    
    if success_message == "Thank you for your order!":
        print("Order berhasil dikonfirmasi dengan pesan: Thank you for your order!")
    else:
        print(f"Order gagal dikonfirmasi, pesan yang muncul: {success_message}")    

finally:
    driver.quit()