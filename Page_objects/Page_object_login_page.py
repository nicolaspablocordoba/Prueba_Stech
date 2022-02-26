"""El siguiente Page object está dirigido a la pantalla de login de Netflix"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class PageObjectLoginPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        # constructor de los elementos a utilizar en la pantalla
        self.email_address_field = (By.ID, "id_userLoginId")
        self.password_field = (By.ID, 'id_password')
        self.sign_in_button = (By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        self.remember_me_check = (By.CLASS_NAME, 'login-remember-me-label-text')

    # métodos de la pantalla

    def click_and_complete_email_address_field(self, email):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            self.email_address_field))).click().perform()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.email_address_field)).clear()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.email_address_field)).send_keys(email)

    def click_and_complete_password_field(self, password):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password_field)).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password_field)).clear()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password_field)).send_keys(password)

    def click_sign_in_button(self):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            self.sign_in_button))).click().perform()

    def click_remember_me_check(self):
        ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            self.remember_me_check))).click().perform()
