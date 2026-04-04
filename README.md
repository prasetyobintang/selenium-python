# 🧪 Selenium Python - E2E Automation

Project sederhana untuk belajar **QA Automation** menggunakan **Python + Selenium** dengan pendekatan **end-to-end testing** + sedikit simulasi user behavior.

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

### Optional (Next Step)
- pytest → test runner
- webdriver-manager → auto manage driver
- pytest-html → reporting

---

## ⚙️ Setup

1. Clone repository:

2. Buat virtual environment:
```
python -m venv venv
```
3. Aktifkan virtual environment:
```
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```
4. Update pip:
```
python -m pip install --upgrade pip
```
5. install dependencies:
```
pip install selenium faker
```

---

## ▶️ Run
```
python main.py
```

---

## 🧪 Test Flow
### ✅ Positive Flow
Login dengan user valid
Validasi redirect ke /inventory.html
Validasi item muncul di halaman inventory
Pilih item & add to cart
Validasi item di cart
Checkout
Isi form (faker: first name, last name, zip)
Validasi:
item total
tax
total (item + tax)
Finish checkout
Validasi order sukses

### ❌ Negative Flow
Login dengan credential tidak valid
Validasi error message muncul
Validasi isi error message sesuai expected

---

## 📁 Struktur Project
selenium-python/
    tests/
        negative/
            saucedemo_negative.py
        positive/
            saucedemo_positive.py
        simulasi/
            user_behavior.py
.gitignore
main.py
README.md
test.py

---

## 🧠 Notes
### 📋 General
Menggunakan explicit wait untuk menghindari flaky test
Validasi tidak hanya URL, tapi juga:
state halaman
data item
perhitungan harga
Error handling fokus ke behavior, bukan sekadar element existence

--- 

## 🤖 Simulasi User Behavior

Pendekatan tambahan untuk membuat automation lebih realistis:

Delay natural (tidak instant)
Typing per karakter
Scroll bertahap
Interaction berbasis user flow (bukan lompat-lompat element)

> Digunakan untuk eksplorasi behavior, bukan pengganti testing deterministik

---

## ⚠️ Limitations
Tidak handle browser-level popup (contoh: password leak detection Chrome)
Belum menggunakan test runner (pytest)
Belum ada reporting

---

## 🔥 Future Improvement
Integrasi ke pytest
Parallel testing
Headless + CI/CD pipeline
Reporting (HTML / Allure)
Page Object Model (POM)

---

## 👨‍💻 Author

Prasetyo Bintang Arummardi ✨