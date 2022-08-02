import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAdmin(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_seach_user(self): 
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
    
    def test_b_add_admin_and_delete(self): 
        # steps
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
        browser.find_element(By.ID,"btnAdd").click() # add admin
        time.sleep(3)
        browser.find_element(By.ID,"systemUser_userType").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Linda Jane Anderson")
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_userName").send_keys("linda10") 
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_password").send_keys("adminlinda") 
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("adminlinda") 
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("linda10") # search admin
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_userType").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_status").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        browser.find_element(By.ID,"ohrmList_chkSelectAll").click() # checklist admin
        time.sleep(3)
        browser.find_element(By.ID,"btnDelete").click() # delete admin
        time.sleep(3)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(3)
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()