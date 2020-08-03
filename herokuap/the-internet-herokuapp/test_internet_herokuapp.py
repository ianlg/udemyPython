from selenium import webdriver
import time
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


URL = "http://the-internet.herokuapp.com"
AB_TESTING = "A/B Testing"
ADD_REMOVE_ELEMENTS = "Add/Remove Elements"
ADD_ELEMENT_XPATH = '//*[@id="content"]/div/button'
BASIC_AUTHENTICATION = "Basic Auth"
BROKEN_IMAGES = "Broken Images"
CHALLENGING_DOM = "Challenging DOM"
CHECKBOXES = "Checkboxes"




@pytest.fixture()
def herokuap_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/development/udemyPython/pytest/Webdrivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(URL)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_ab_testing(herokuap_setup):
    driver.find_element_by_link_text(AB_TESTING).click()
    time.sleep(5)
    assert "Also known as split testing" in driver.page_source

def test_add_remove_elements(herokuap_setup):
    driver.find_element_by_link_text(ADD_REMOVE_ELEMENTS).click()
    time.sleep(2)
    driver.find_element_by_xpath(ADD_ELEMENT_XPATH).click()
    driver.find_element_by_xpath(ADD_ELEMENT_XPATH).click()
    driver.find_element_by_xpath(ADD_ELEMENT_XPATH).click()
    driver.find_element_by_xpath(ADD_ELEMENT_XPATH).click()
    driver.find_element_by_xpath(ADD_ELEMENT_XPATH).click()
    driver.find_element_by_class_name("added-manually").click()
    driver.find_element_by_class_name("added-manually").click()
    driver.find_element_by_class_name("added-manually").click()
    driver.find_element_by_class_name("added-manually").click()
    driver.find_element_by_class_name("added-manually").click()
    #x = driver.find_element_by_class_name("added-manually")
    #assert len(x) == 0
    #ADD ASSERTION DELETE BUTTON IS NO LONGER VISIBLE

def test_authentication(herokuap_setup):
    driver.find_element_by_link_text(BASIC_AUTHENTICATION).click()
    alert = driver.switch_to.alert()
    time.sleep(2)
    #alert.authenticate("admin", "admin")

    # box = driver.switch_to.alert()
    # box.sendKeys("admin")
    # time.sleep(10)
    #pop up alert authentication

def test_broken_images(herokuap_setup):
    driver.find_element_by_link_text(BROKEN_IMAGES).click()
    pictures = driver.find_elements(By.TAG_NAME, 'img')
    for i in pictures:
        print(i.get_attribute("src"))
    status_1 = requests.get("http://the-internet.herokuapp.com/asdf.jpg")
    print(status_1)
    assert status_1.status_code == 404
    status_2 = requests.get("http://the-internet.herokuapp.com/hjkl.jpg")
    print(status_2)
    assert status_2.status_code == 404
    status_3 = requests.get("http://the-internet.herokuapp.com/img/avatar-blank.jpg")
    print(status_3)
    assert status_3.status_code == 200

def test_challenging_dom(herokuap_setup):
    driver.find_element_by_link_text(CHALLENGING_DOM).click()
    # selecting Apeirian3
    # select = driver.find_element_by_class_name("large-10 columns")
    # value = select.select_by_visible_text("edit")
    assert "The hardest part in automated web testing" in driver.page_source

def test_checkboxes(herokuap_setup):
    try:
        driver.find_element_by_link_text(CHECKBOXES).click()
        driver.find_element_by_xpath('//*[@id="checkboxes"]/input[1]').click()
        driver.find_element_by_xpath('//*[@id="checkboxes"]/input[2]').click()
        assert driver.find_element_by_xpath('//*[@id="checkboxes"]/input[1]').is_selected() == True
        assert driver.find_element_by_xpath('//*[@id="checkboxes"]/input[2]').is_selected() == True

    except AssertionError as error:
        print("There was an exception")
        print(error)
        raise

    except:
        print("There was an error")
        raise