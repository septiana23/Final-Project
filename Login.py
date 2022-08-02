import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    
    def test_a_failed_login_with_empty_username_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Username cannot be empty')    
    
    def test_b_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Password cannot be empty')

    def test_c_failed_login_with_wrong_username_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Septiana") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("septiana") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.find_element(By.ID,"spanMessage").text
        self.assertEqual(response_message, 'Invalid credentials')

    def test_d_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)

        # validasi
        response_message = browser.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()