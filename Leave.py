import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLeave(unittest.TestCase): 

    def setUp(self):    
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_view_list_leave(self): 
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol log in
        time.sleep(3)
        browser.find_element(By.ID,"calFromDate").send_keys("") # search list leave
        time.sleep(1)
        browser.find_element(By.ID,"calToDate").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"leaveList_chkSearchFilter_checkboxgroup_allcheck").click()
        time.sleep(1)
        browser.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"leaveList_cmbSubunit").send_keys("All") 
        time.sleep(1)
        #browser.find_element(By.ID,"leaveList_cmbWithTerminated").click() 
        #time.sleep(3)
        browser.find_element(By.ID,"btnSearch").click()
        time.sleep(3)
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()