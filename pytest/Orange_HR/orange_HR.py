from selenium import webdriver
import pytest
import time

URL = "https://opensource-demo.orangehrmlive.com"
USERNAME = "Admin"
PASSWORD = "admin123"
LEAVE_ELEMENT = "menu_leave_viewLeaveModule"
TIME_ELEMENT = "menu_time_viewTimeModule"
RECRUITMENT_ELEMENT = "menu_recruitment_viewRecruitmentModule"
DIRECTORY_ELEMENT = "menu_directory_viewDirectory"
MAINTENANCE_ELEMENT = "menu_maintenance_purgeEmployee"
BUZZ_ELEMENT = "menu_buzz_viewBuzz"


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/development/udemyPython/pytest/Webdrivers/chromedriver.exe")
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(URL)
    yield
    driver.close()
    driver.quit()

def login(test_setup):
    driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtUsername").send_keys(USERNAME)
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys(PASSWORD)
    driver.find_element_by_id("btnLogin").click()
    title = driver.title
    assert title == "OrangeHRM"

def test_leave_page(test_setup):
    login(test_setup)
    driver.find_element_by_id(LEAVE_ELEMENT).click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="leave-list-search"]/a').is_displayed()
    driver.find_element_by_id("btnSearch").is_enabled()
    assert "Leave List" in driver.page_source

def test_time_page(test_setup):
    login(test_setup)
    driver.find_element_by_id(TIME_ELEMENT).click()
    time.sleep(2)
    assert "Define Timesheet Period" in driver.page_source

def test_recruitment_page(test_setup):
    login(test_setup)
    driver.find_element_by_id(RECRUITMENT_ELEMENT).click()
    time.sleep(2)
    assert "Candidates" in driver.page_source

def test_directory_page(test_setup):
    login(test_setup)
    driver.find_element_by_id(DIRECTORY_ELEMENT).click()
    time.sleep(2)
    assert "Search Directory" in driver.page_source

def test_maintenance_page(test_setup):
    login(test_setup)
    driver.find_element_by_id(MAINTENANCE_ELEMENT).click()
    time.sleep(2)
    assert "Purge Employee Records" in driver.page_source

def test_buzz_page(test_setup):
    login(test_setup)
    driver.find_element_by_id(BUZZ_ELEMENT).click()
    time.sleep(2)
    assert "Buzz is accessible for the user who is assigned with an employee" in driver.page_source


