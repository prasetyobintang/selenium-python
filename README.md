# 🧪 Selenium Python - E2E Automation (SauceDemo)

Project sederhana untuk belajar **QA Automation** menggunakan **Python + Selenium** dengan flow end-to-end.

---

## 🚀 Tech Stack

- Python
- Selenium WebDriver
- Faker (dummy data)
- Chrome Browser

---

## ⚙️ Setup
## 📦 Dependencies

### Core
- selenium
- faker

### Optional / Future Improvement
- pytest (test runner)
- webdriver-manager (auto driver management)
- pytest-html (reporting)

1. pastikan Python berada di PATH, cek: 
```
python --version
```
2. pastikan pip juga sudah terinstall, cek: 
```
pip --version
```
3. upgrade pip:
```
python -m pip install --upgrade pip
```
4. install core dependency:
```
pip install selenium
pip install faker
```

---

## ▶️ Run
```
python main.py
```

---

## 🧪 Test Flow

1. Login dengan user valid  
2. Validasi berhasil login (URL `/inventory.html`)  
3. Validasi item di halaman inventory  
4. Pilih 1 item & add to cart  
5. Validasi item di cart  
6. Checkout  
7. Isi form (faker: first name, last name, zip)  
8. Validasi:
   - item total  
   - tax  
   - total (item + tax)  
9. Finish checkout  
10. Validasi order sukses  

---

## 📁 Struktur Project
```
selenium-python/
main.py
test.py
.gitignore
README.md
```

---

## 🧠 Notes

- Menggunakan explicit wait untuk menghindari flaky test  
- Validasi tidak hanya URL, tapi juga:
  - data item
  - perhitungan harga  
- Faker digunakan untuk data input dinamis  

---

## 👨‍💻 Author

Prasetyo Bintang ✨