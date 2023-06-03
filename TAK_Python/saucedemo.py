import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Saucedemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login_saucedemo(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://www.saucedemo.com/inventory.html")

    def test_failed_login_saucedemo_wrong_credentials(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("salahnama")
        driver.find_element(By.ID, "password").send_keys("salahpassword")
        driver.find_element(By.ID, "login-button").click()
        data = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
        self.assertIn("Username and password do not match any user in this service", data)

    def test_failed_login_saucedemo_locked_user(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        data = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text
        self.assertIn("Sorry, this user has been locked out", data)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()