# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPreferenceViews():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_preferenceViews2(self):
    self.driver.get("http://localhost:8000/admin/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "Votings").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("High")
    self.driver.find_element(By.ID, "id_themeVotation").click()
    dropdown = self.driver.find_element(By.ID, "id_themeVotation")
    dropdown.find_element(By.XPATH, "//option[. = 'Self-interest']").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_question")
    dropdown.find_element(By.XPATH, "//option[. = '¿Es david cervantes?']").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_auths")
    dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
    self.driver.find_element(By.NAME, "_save").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "  ---------"
    self.driver.find_element(By.ID, "id_preference").click()
    dropdown = self.driver.find_element(By.ID, "id_preference")
    dropdown.find_element(By.XPATH, "//option[. = 'High']").click()
    self.driver.find_element(By.ID, "id_preference").click()
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("Mid")
    self.driver.find_element(By.CSS_SELECTOR, ".field-themeVotation > div").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    dropdown = self.driver.find_element(By.ID, "id_themeVotation")
    dropdown.find_element(By.XPATH, "//option[. = 'Testing']").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_question")
    dropdown.find_element(By.XPATH, "//option[. = '¿Es david cervantes?']").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_auths")
    dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
    self.driver.find_element(By.NAME, "_save").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "  ---------"
    self.driver.find_element(By.ID, "id_preference").click()
    dropdown = self.driver.find_element(By.ID, "id_preference")
    dropdown.find_element(By.XPATH, "//option[. = 'Mid']").click()
    self.driver.find_element(By.ID, "id_preference").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "Mid"
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, ".object-tools > li").click()
    self.driver.find_element(By.CSS_SELECTOR, ".addlink").click()
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("Low")
    self.driver.find_element(By.ID, "id_themeVotation").click()
    dropdown = self.driver.find_element(By.ID, "id_themeVotation")
    dropdown.find_element(By.XPATH, "//option[. = 'Testing']").click()
    self.driver.find_element(By.ID, "id_themeVotation").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_question")
    dropdown.find_element(By.XPATH, "//option[. = '¿Es david cervantes?']").click()
    self.driver.find_element(By.ID, "id_question").click()
    dropdown = self.driver.find_element(By.ID, "id_auths")
    dropdown.find_element(By.XPATH, "//option[. = 'http://localhost:8000']").click()
    self.driver.find_element(By.NAME, "_save").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "  ---------"
    self.driver.find_element(By.ID, "id_preference").click()
    dropdown = self.driver.find_element(By.ID, "id_preference")
    dropdown.find_element(By.XPATH, "//option[. = 'Low']").click()
    self.driver.find_element(By.ID, "id_preference").click()
    element = self.driver.find_element(By.ID, "id_preference")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "Low"
    self.driver.find_element(By.NAME, "_save").click()
    assert self.driver.find_element(By.LINK_TEXT, "High").text == "High"
    self.driver.find_element(By.LINK_TEXT, "High").click()
    self.driver.find_element(By.LINK_TEXT, "Mid").click()
    assert self.driver.find_element(By.LINK_TEXT, "Mid").text == "Mid"
    self.driver.find_element(By.LINK_TEXT, "Low").click()
    assert self.driver.find_element(By.LINK_TEXT, "Low").text == "Low"
    self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(7) > li:nth-child(1) > a").click()
    self.driver.find_element(By.NAME, "action").click()
    dropdown = self.driver.find_element(By.NAME, "action")
    dropdown.find_element(By.XPATH, "//option[. = 'Delete selected votings']").click()
    self.driver.find_element(By.NAME, "action").click()
    self.driver.find_element(By.NAME, "_selected_action").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row2:nth-child(2) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row1:nth-child(3) .action-select").click()
    self.driver.find_element(By.NAME, "index").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()
  
