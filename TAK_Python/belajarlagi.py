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
        driver.get("https://demoqa.com/browser-windows")
        driver.find_element(By.ID, "tabButton").click()
        driver.switch_to.window(driver.window_handles[1])
        url = driver.current_url
        self.assertEqual(url, "https://demoqa.com/sample")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()