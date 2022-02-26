"""El siguiente page object, está dirigido a la Landing page de Netflix"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class PageObjectLandingPage:
    def __init__(self, my_driver):
        # constructor de los elementos a utilizar en la pantalla
        self.driver = my_driver
        self.login_button = (By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a')
        self.email_address_field = (By.ID, 'id_email_hero_fuji')
        self.get_started_button = (By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div/div/button')

    # métodos de la pantalla

    def click_login_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.login_button)).click()

    def click_and_complete_email_address_field(self, email):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.email_address_field)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.email_address_field)).clear()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.email_address_field)).send_keys(email)

    def click_get_started_button(self):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            self.get_started_button))).click().perform()
