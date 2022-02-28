"""
1. Crear una clase llamada NetflixTest
2. Ingresar a Netflix
3. Maximizar la pagina al iniciar cada test
4. Agregar una espera implícita al iniciar cada test
5. Usar testng (u otro framework de pruebas) para la creación de todos los tests.
6. Crear un test llamado validarTituloTest, para realizar la validación del titulo.
7. Crear un método de test que se llame startSessionPageTest.
    a. Hacer click en Iniciar Sesión. Validar que el título de la página haya cambiado y que se encuentre el texto
     "Iniciar Sesión" dentro de los h1s.
    b. Validar que se encuentre el texto “Iniciar sesión con Facebook” en el sitio
8. Crear un método de test llamado loginToNetflixErrorTest que complete el campo del
email con XXX y la contraseña “holamundo”. Desclickear el botón de Recuerdame. Haz click en Iniciar
Sesión para luego validar que esté presente el mensaje de error: “Contraseña incorrecta.” y validar que
el checkbox “Recuerdame” esté seleccionado.
9. Crear un método llamado fakeEmailTest que complete el campo que se encuentra en la Landing
Page. Luego, haga click en COMIENZA YA. El email debe ser generado de forma aleatoria (mostrar por
pantalla el mail que se generó). Luego de hacer click, validar que dentro de la URL se encuentre la
palabra signup.
10. Todos los test deben cerrarse al finalizar su ejecución.
11. Crear un archivo testng que permita ejecutar la clase de test.
12. Crear un test que reciba por parámetro un tagName. Crear un método de test llamado
printTagsTest que imprima en pantalla todas las etiquetas que correspondan con el
parámetro recibido. Si no se encuentran elementos, se debe mostrar “No se encuentran
elementos con esta etiqueta”.
13. Agregar un orden de ejecución descendente a los tests.
14. Aplicar el patrón Page Object al proyecto. Utilizar herencia y clases bases para reutilizar
variables y métodos
"""

import sys
sys.path.append(r"C:\Prueba_Stech")
import json
import inspect
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_objects.Page_object_login_page import PageObjectLoginPage
from Page_objects.Page_object_landing_page import PageObjectLandingPage
from Funciones_extra.Funciones import FuncionesExtras
import time


class NetflixTest(unittest.TestCase):
    def setUp(self):
        # CHROME CONFIGURATION
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

        # JSON lOAD
        with open(r"C:\Prueba_Stech\Json\URL.json") as netflix_url:
            self.netflix_url = json.loads(netflix_url.read())

        # PAGE OBJECT
        self.landing_page = PageObjectLandingPage(self.driver)
        self.login_page = PageObjectLoginPage(self.driver)
        self.funcion_extra = FuncionesExtras()

    def test_validar_titulo_test(self):
        try:
            self.driver.get(self.netflix_url["netflix_landing_page_url"][0])
            title = self.driver.title
        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)
        else:
            self.assertEqual("Netflix Argentina: Ve series online, ve películas online", str(title)) # este assert valida que el título de la pagina sea igual al que se pasa por parametro
    
    def test_start_session_page_test(self):
        try:
            self.driver.get(self.netflix_url["netflix_landing_page_url"][0])
            landing_title = self.driver.title
            self.landing_page.click_login_button()
            login_title = self.driver.title
            self.assertNotEqual(landing_title, login_title) # este assert valida que los títlulos de las pantallas sean diferentes
            title_h1 = self.driver.find_element(By.TAG_NAME, 'h1').text
            self.assertEqual("Inicia sesión", title_h1)

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            facebook_login_text = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[2]/form/div/div/button/div/span'))).text
            self.assertEqual("Iniciar sesión con Facebook", facebook_login_text)  # este asserte verifica que el texto "Iniciar sesión con Facebook" sea igual al que se toma de la pantalla

    def test_login_to_netflix_error_test(self):
        try:
            self.driver.get(self.netflix_url["netflix_login_page_url"][0])
            self.login_page.click_and_complete_email_address_field("test@mail.com")
            self.login_page.click_and_complete_password_field("holamundo")
            self.login_page.click_remember_me_check()
            self.login_page.click_sign_in_button()
            error_message = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]/b'))).text

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            self.assertEqual("Contraseña incorrecta.", error_message)  # este assert verifica que aparezca el texto "contraseña incorrecta"
            self.assertTrue(WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                By.ID, 'bxid_rememberMe_true'))).is_selected())  # este assert verifica si el check de "recuerdame" está seleccionado

    def test_fake_email_test(self):
        try:
            self.driver.get(self.netflix_url["netflix_landing_page_url"][0])
            fake_email = self.funcion_extra.crear_email_random()
            print("El mail generado de forma aelatoria es: "+fake_email)
            self.landing_page.click_and_complete_email_address_field(fake_email)
            self.landing_page.click_get_started_button()
            time.sleep(3)
            url = self.driver.current_url

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            self.assertIn("signup", url)  # este assert verifica que la palabra "signup" se encuentre dentro de la URL

    def test_print_tags_test(self, tag_name='h1'):
        self.driver.get(self.netflix_url["netflix_landing_page_url"][0])
        self.tag_name = tag_name
        print("El tag que se recibe por parametro es: "+self.tag_name)
        try:
            lista = list(WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((
                By.TAG_NAME, self.tag_name))))
            if len(lista) > 0:
                for i in range(len(lista)):
                    print(i)
        except Exception:
            print("No se encuentran elementos con esta etiqueta")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
