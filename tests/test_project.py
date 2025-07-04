import os
import pytest
from selenium.webdriver.common.by import By

BASE_URL = "http://the-internet.herokuapp.com/"

def test_homepage_title(driver):
    driver.get(BASE_URL)
    assert driver.title == "The Internet"

def test_checkboxes(driver):
    driver.get(BASE_URL)
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()

    header = driver.find_element(By.TAG_NAME, "h3").text
    assert header == "Checkboxes"

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert_checkbox_state(checkboxes[0], should_be_checked=False)
    assert_checkbox_state(checkboxes[1], should_be_checked=True)

def test_file_upload(driver):
    driver.get(BASE_URL)
    driver.find_element(By.LINK_TEXT, "File Upload").click()

    header = driver.find_element(By.TAG_NAME, "h3").text
    assert header == "File Uploader"

    file_input = driver.find_element(By.ID, "file-upload")
    upload_button = driver.find_element(By.ID, "file-submit")

    file_input.send_keys(os.getcwd()+"/uploads/sample_file.txt")
    upload_button.click()

    uploaded_text = driver.find_element(By.TAG_NAME, "h3").text
    assert uploaded_text == "File Uploaded!"


def assert_checkbox_state(checkbox_element, should_be_checked):
    actual_state = checkbox_element.is_selected()
    assert actual_state == should_be_checked, f"Expected checked={should_be_checked}, but got {actual_state}"