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

1. Clone repo:
```
git clone https://github.com/prasetyobintang/selenium-python.git

cd selenium-python
```
2. Buat virtual environment:
```
python -m venv venv
```
3. Aktifkan virtual environment:
```
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
```
4. Update pip:
```
python -m pip install --upgrade pip
```
5. Install dependency:
```
pip install selenium faker
```
> Note: Pastikan virtual environment sudah aktif sebelum install dependency 

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
tests/
    negative/
        saucedemo_negative.py
    positive/   
        saucedemo_positive.py
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

Prasetyo Bintang Arummardi ✨