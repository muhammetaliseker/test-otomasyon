from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Tarayıcı başlatılır (Chrome)
driver = webdriver.Chrome()

try:
    # Login sayfasına git
    driver.get("https://the-internet.herokuapp.com/login")

    # Sayfa yüklenmesi için kısa bir bekleme
    time.sleep(2)

    # Kullanıcı adı ve şifre alanlarını bul
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Yanlış bilgiler gir
    username_field.send_keys("wronguser")
    password_field.send_keys("wrongpass")

    # Login butonuna bas
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Sonuç için kısa bir bekleme
    time.sleep(2)

    # Hata mesajını bul ve kontrol et
    error_message = driver.find_element(By.ID, "flash")

    # Mesaj içinde "Your username is invalid!" geçiyor mu kontrol et
    if "Your username is invalid!" in error_message.text:
        print("✅ Test Başarılı: Hata mesajı göründü.")
    else:
        print("❌ Test Başarısız: Hata mesajı beklenildiği gibi değil.")

finally:
    # Tarayıcıyı kapat
    driver.quit()
    
