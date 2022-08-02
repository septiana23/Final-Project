import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestPIM(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_search_employee(self): 
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)
        browser.find_element(By.ID,"btnAdd").click() # add employee
        time.sleep(3)
        browser.find_element(By.ID,"firstName").send_keys("Edward") 
        time.sleep(1)
        browser.find_element(By.ID,"middleName").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"lastName").send_keys("Cullen") 
        time.sleep(1)
        
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)
    
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()