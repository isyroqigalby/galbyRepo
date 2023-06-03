import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class TricentisDemoWebShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login_tricentis(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/")

    def test_b_success_login_tricentis_without_click_remember_me(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/")

    def test_c_success_open_forgot_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.CLASS_NAME, "forgot-password").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/login")

    def test_d_failed_login_tricentis_without_input_any_fields(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
        data = driver.find_element(By.CSS_SELECTOR, "[class=message-error]").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", data)

    def test_e_failed_login_tricentis_with_wrong_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("bakuhantam@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
        data = driver.find_element(By.CSS_SELECTOR, "[class=message-error]").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", data)

    def test_f_failed_login_tricentis_with_wrong_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("cobacoba")
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
        data = driver.find_element(By.CSS_SELECTOR, "[class=message-error]").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", data)

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()