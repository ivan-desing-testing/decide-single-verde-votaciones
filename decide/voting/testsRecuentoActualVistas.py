from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from base import mods
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from base.tests import BaseTestCase

class AdminTestCase(StaticLiveServerTestCase):


    def setUp(self):
        #Load base test functionality for decide
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()            
            
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()


#LOS SIGUIENTES TEST DEBEN SER EJECUTADOS CON LA BASE DE DATOS DE VOTACIONES VACÍA, YA QUE SE USAN LAS IDs DE LAS VOTACIONES CREADAS.
    
    def test_vista_recuento_Actual(self):

    #Creando la votación

        self.driver.get("http://localhost:8000/admin/login/?next=/admin/")
        self.driver.set_window_size(1778, 893)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("user")
        self.driver.find_element(By.ID, "id_password").send_keys("decidep1")
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Votings").click()
        self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("Votacion de prueba")
        self.driver.find_element(By.ID, "id_desc").click()
        self.driver.find_element(By.ID, "id_desc").send_keys("descripcion de prueba")
        self.driver.find_element(By.ID, "id_question").click()
        dropdown = self.driver.find_element(By.ID, "id_question")
        dropdown.find_element(By.XPATH, "//option[. = 'pregunta de prueba']").click()
        self.driver.find_element(By.ID, "id_question").click()
        dropdown = self.driver.find_element(By.ID, "id_auths")
        dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
        self.driver.find_element(By.NAME, "_save").click()
        self.driver.find_element(By.NAME, "_selected_action").click()
        self.driver.find_element(By.NAME, "action").click()

        #Ponemos la votación en comenzar
        dropdown = self.driver.find_element(By.NAME, "action")
        dropdown.find_element(By.XPATH, "//option[. = 'Start']").click()
        self.driver.find_element(By.NAME, "action").click()
        self.driver.find_element(By.NAME, "index").click()

        #EJECUTAMOS LA ACCION CURRENTTALLY Y VEMOS QUE SE EJECUTA CORRECTAMENTE
        dropdown = self.driver.find_element(By.NAME, "action")
        dropdown.find_element(By.XPATH, "//option[. = 'CurrentTally']").click()
        self.driver.find_element(By.NAME, "action").click()
        self.driver.find_element(By.NAME, "index").click()

        