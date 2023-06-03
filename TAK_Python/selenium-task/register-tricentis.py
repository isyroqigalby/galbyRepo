import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import string    
import random

class TricentisDemoWebShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register_tricentis(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
        driver.find_element(By.ID, "Email").send_keys(ran+"@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/registerresult/1")

    def test_b_success_register_tricentis_from_login_page(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div[3]/input").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
        driver.find_element(By.ID, "Email").send_keys(ran+"@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/registerresult/1")

    def test_c_failed_register_with_existing_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_d_failed_register_without_input_all_fields(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_e_failed_register_without_select_gender(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_f_failed_register_without_input_first_name(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_g_failed_register_without_input_last_name(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_h_failed_register_without_input_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_i_failed_register_without_input_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_j_failed_register_without_input_confirm_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_k_failed_register_without_input_email_and_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

    def test_l_failed_register_without_input_email_and_confirm_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Isyroqi")
        driver.find_element(By.ID, "LastName").send_keys("Galby")
        driver.find_element(By.ID, "Email").send_keys("isyroqigalby.ig@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "register-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/register")

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()