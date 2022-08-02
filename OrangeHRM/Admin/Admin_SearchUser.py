import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAdmin(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_seach_user(self): 
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("") # search admin
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_userType").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_status").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
