# from django.test import TestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

# from base.tests import BaseTestCase

# class AdminTestCase(StaticLiveServerTestCase):


#    def setUp(self):
#        #Load base test functionality for decide
#        self.base = BaseTestCase()
#        self.base.setUp()

#        options = webdriver.ChromeOptions()
#        options.headless = True
#        self.driver = webdriver.Chrome(options=options)

#        super().setUp()

#    def tearDown(self):
#        super().tearDown()
#        self.driver.quit()

#        self.base.tearDown()

#    def test_simpleCorrectLogin(self):
#        self.driver.get(f'{self.live_server_url}/admin/')
#       self.driver.find_element_by_id('id_username').send_keys("admin")
#       self.driver.find_element_by_id('id_password').send_keys("qwerty",Keys.ENTER)

#        print(self.driver.current_url)
#         In case of a correct loging, a element with id 'user-tools' is shown in the upper right part
#        self.assertTrue(len(self.driver.find_elements_by_id('user-tools'))==1)

#     Ejercicio Login Incorrecto

#    def test_simpleIncorrectLogin(self):
#        self.driver.get(f'{self.live_server_url}/admin/')
#        self.driver.find_element_by_id('id_username').send_keys("incorrect")
#        self.driver.find_element_by_id('id_password').send_keys("incorrect")
#        self.driver.find_element_by_id('login-form').submit()

#         In case of a correct loging, a element with id 'user-tools' is shown in the upper right part
#        self.assertTrue(len(self.driver.find_elements_by_class_name('errornote'))==1)

#    def test_crear_pregunta(self):
#        self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
#        self.driver.set_window_size(1778, 893)
#        self.driver.find_element(By.ID, "id_username").click()
#        self.driver.find_element(By.ID, "id_username").send_keys("user")
#        self.driver.find_element(By.ID, "id_password").send_keys("decidep1")
#        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
#        self.driver.find_element(By.CSS_SELECTOR, ".model-question .addlink").click()
#        self.driver.find_element(By.ID, "id_desc").send_keys("pregunta de prueba")
#        self.driver.find_element(By.ID, "id_options-0-number").click()
#       self.driver.find_element(By.ID, "id_options-0-number").send_keys("1")
#        self.driver.find_element(By.ID, "id_options-0-number").click()
#        self.driver.find_element(By.ID, "id_options-0-option").click()
#        self.driver.find_element(By.ID, "id_options-0-option").send_keys("hola mundo")
#        self.driver.find_element(By.NAME, "_save").click()

#         Comprobamos que se ha creado la pregunta con el nombre: "pregunta de prueba"
#        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".row1:nth-child(1) a").text == "pregunta de prueba")
