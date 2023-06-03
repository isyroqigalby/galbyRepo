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

    def test_d_success_checkout_tricentis(self):
        driver = self.driver
        #Login flow before add item to cart
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("cobacoba@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("TestDoangIni1")
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()

        #Open the Category Computerds
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ul/li[2]/a").click()

        #Open the Subcategory Notebook
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/a/img").click()

        #Click Add To Cart
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/div[2]/input").click()

        #Open Cart Page
        driver.find_element(By.CLASS_NAME, "ico-cart").click()

        #Checklist the Item in Cart
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[1]/input").click()

        #Checklist the Term of Service
        driver.find_element(By.ID, "termsofservice").click()

        #Click Checkout Button
        driver.find_element(By.ID, "checkout").click()

        #Click Continue in Billing Address
        driver.find_element(By.CLASS_NAME, "button-1 new-address-next-step-button").click()

        #Click Continue in Shipping Address
        driver.find_element(By.XPATH, "//*[@id=shipping-buttons-container]/input").click()

        #Click Continue in Shipping Method
        driver.find_element(By.CLASS_NAME, "button-1 shipping-method-next-step-button").click()

        #Click Continue in Payment Method
        driver.find_element(By.CLASS_NAME, "button-1 payment-method-next-step-button").click()

        #Click Continue in Payment Information
        driver.find_element(By.CLASS_NAME, "button-1 payment-info-next-step-button").click()

        #Click Continue in Confirm Order
        driver.find_element(By.CLASS_NAME, "button-1 confirm-order-next-step-button").click()
        self.assertNotIn("No results found.", driver.page_source)
        url = driver.current_url
        self.assertEqual(url, "https://demowebshop.tricentis.com/checkout/completed/")

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()