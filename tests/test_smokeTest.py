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
from selenium.webdriver.chrome.options import Options


class TestSmokeTest():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adminPage(self):
    # Test name: Admin Page
    # Step # | name | target | value | comment
    # 1 | open | http://127.0.0.1:5500/teton/1.6/index.html |  | 
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    # 2 | setWindowSize | 1221x1032 |  | 
    self.driver.set_window_size(1221, 1032)
    # 3 | click | linkText=Admin |  | 
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    # 4 | assertText | css=.myinput:nth-child(2) | Username: | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
    # 5 | assertElementPresent | id=username |  | 
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    # 6 | click | id=username |  | 
    self.driver.find_element(By.ID, "username").click()
    # 7 | type | id=username | incorrect | 
    self.driver.find_element(By.ID, "username").send_keys("incorrect")
    # 8 | type | id=password | incorrect | 
    self.driver.find_element(By.ID, "password").send_keys("incorrect")
    # 9 | click | css=.admin-main |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".admin-main").click()
    # 10 | click | css=.mysubmit:nth-child(4) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    # 11 | waitForText | css=.errorMessage | Invalid username and password. | 
    WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".errorMessage"), "Invalid username and password."))
  
  def test_directoryPage(self):
    # Test name: Directory Page
    # Step # | name | target | value | comment
    # 1 | open | http://127.0.0.1:5500/teton/1.6/index.html |  | 
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    # 2 | setWindowSize | 1190x1032 |  | 
    self.driver.set_window_size(1190, 1032)
    # 3 | click | linkText=Directory |  | 
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    # 4 | click | id=directory-grid |  | 
    self.driver.find_element(By.ID, "directory-grid").click()
    # 5 | assertText | css=.gold-member:nth-child(9) > p:nth-child(2) | Teton Turf and Tree | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    # 6 | assertElementPresent | css=.gold-member:nth-child(9) |  | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
    assert len(elements) > 0
    # 7 | click | id=directory-list |  | 
    self.driver.find_element(By.ID, "directory-list").click()
    # 8 | assertText | css=.gold-member:nth-child(9) > p:nth-child(2) | Teton Turf and Tree | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    # 9 | assertElementPresent | css=.gold-member:nth-child(9) > p:nth-child(2) |  | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
  
  def test_homePage(self):
    # Test name: Home Page
    # Step # | name | target | value | comment
    # 1 | open | http://127.0.0.1:5500/teton/1.6/index.html |  | 
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    # 2 | assertElementPresent | css=.header-logo img |  | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    # 3 | assertText | css=.header-title > h1 | Teton Idaho | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    # 4 | assertText | css=.header-title > h2 | Chamber of Commerce | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    # 5 | assertTitle | Teton Idaho CoC |  | 
    assert self.driver.title == "Teton Idaho CoC"
    # 6 | setWindowSize | 1163x1032 |  | 
    self.driver.set_window_size(1163, 1032)
    # 7 | assertElementPresent | css=.spotlight1 > .centered-image |  | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
    assert len(elements) > 0
    # 8 | assertElementPresent | css=.spotlight2 > .centered-image |  | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
    # 9 | assertElementPresent | linkText=Join Us! |  | 
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
    # 10 | click | linkText=Join Us! |  | 
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
  
  def test_joinPage(self):
    # Test name: Join Page
    # Step # | name | target | value | comment
    # 1 | open | http://127.0.0.1:5500/teton/1.6/index.html |  | 
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    # 2 | setWindowSize | 1190x1032 |  | 
    self.driver.set_window_size(1190, 1032)
    # 3 | click | linkText=Join |  | 
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    # 4 | assertText | css=.myinput:nth-child(2) | First Name | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
    # 5 | assertElementPresent | name=fname |  | 
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    # 6 | click | name=fname |  | 
    self.driver.find_element(By.NAME, "fname").click()
    # 7 | click | name=fname |  | 
    self.driver.find_element(By.NAME, "fname").click()
    # 8 | type | name=fname | Ethem. | 
    self.driver.find_element(By.NAME, "fname").send_keys("Ethem.")
    # 9 | type | name=lname | Deli. | 
    self.driver.find_element(By.NAME, "lname").send_keys("Deli.")
    # 10 | type | name=bizname | Byu Idaho Pathway. | 
    self.driver.find_element(By.NAME, "bizname").send_keys("Byu Idaho Pathway.")
    # 11 | type | name=biztitle | Student. | 
    self.driver.find_element(By.NAME, "biztitle").send_keys("Student.")
    # 12 | click | name=submit |  | 
    self.driver.find_element(By.NAME, "submit").click()
    # 13 | assertText | css=.myinput:nth-child(2) | Email | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
    # 14 | assertElementPresent | name=email |  | 
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    # 15 | type | name=email | edeli@byupathway.edu | 
    self.driver.find_element(By.NAME, "email").send_keys("edeli@byupathway.edu")
  
