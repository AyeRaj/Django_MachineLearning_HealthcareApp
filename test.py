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


from django.test import LiveServerTestCase

class SafeTestCase(LiveServerTestCase):
    def testDisease(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        driver.set_window_size(1552, 840)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Diagnose").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(6) h1").click()
        time.sleep(1)
        driver.find_element(By.ID, "Pregnancies").click()
        driver.find_element(By.ID, "Pregnancies").send_keys("2")
        time.sleep(0.5)
        driver.find_element(By.ID, "Glucose").click()
        driver.find_element(By.ID, "Glucose").send_keys("60")
        time.sleep(0.5)
        driver.find_element(By.ID, "BloodPressure").click()
        driver.find_element(By.ID, "BloodPressure").send_keys("120")
        time.sleep(0.5)
        driver.find_element(By.ID, "BMI").click()
        driver.find_element(By.ID, "BMI").send_keys("50")
        time.sleep(0.5)
        driver.find_element(By.ID, "DiabetesPedigreeFunction").click()
        driver.find_element(By.ID, "DiabetesPedigreeFunction").send_keys("0")
        time.sleep(0.5)
        driver.find_element(By.ID, "Age").click()
        driver.find_element(By.ID, "Age").send_keys("30")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
        assert "You are Safe" in driver.page_source
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, "Go Back").click()
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, "Home").click()
        time.sleep(0.5)
        driver.close()

class RiskTestCase(LiveServerTestCase):
    def testDisease(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        driver.set_window_size(1552, 840)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Diagnose").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".box:nth-child(6) h1").click()
        time.sleep(1)
        driver.find_element(By.ID, "Pregnancies").click()
        driver.find_element(By.ID, "Pregnancies").send_keys("4")
        time.sleep(0.5)
        driver.find_element(By.ID, "Glucose").click()
        driver.find_element(By.ID, "Glucose").send_keys("90")
        time.sleep(0.5)
        driver.find_element(By.ID, "BloodPressure").click()
        driver.find_element(By.ID, "BloodPressure").send_keys("100")
        time.sleep(0.5)
        driver.find_element(By.ID, "BMI").click()
        driver.find_element(By.ID, "BMI").send_keys("80")
        time.sleep(0.5)
        driver.find_element(By.ID, "DiabetesPedigreeFunction").click()
        driver.find_element(By.ID, "DiabetesPedigreeFunction").send_keys("1")
        time.sleep(0.5)
        driver.find_element(By.ID, "Age").click()
        driver.find_element(By.ID, "Age").send_keys("55")
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
        assert "You are at Risk" in driver.page_source
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, "Go Back").click()
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, "Home").click()
        time.sleep(0.5)
        driver.close()

class ServerTest(LiveServerTestCase):
    def testServer(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')
        assert "eVaidyahCare" in driver.title
  