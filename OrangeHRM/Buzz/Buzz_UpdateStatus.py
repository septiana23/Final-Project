import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestBuzz(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_update_status(self): 
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/buzz/viewBuzz") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)
        browser.find_element(By.ID,"createPost_content").send_keys("Hallo Apa Kabar, Semuanya!") # add update status
        time.sleep(1)
        browser.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(3)
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
