import seleniumwire
from seleniumwire import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import chromedriver_autoinstaller as chromedriver_autoinstaller
from webdriver_manager.core.os_manager import OperationSystemManager,ChromeType
import selenium.common.exceptions
import time
import json
import os
import tempfile
from functools import reduce
import random
import string
import traceback

url = ''

login = "intelceleronherobrin@proton.me"
seleniumwire_options = {
"proxy": {
    'no_proxy': 'localhost,127.0.0.1',
    "verify_ssl": True,
}
}
options = seleniumwire.webdriver.ChromeOptions()
options.set_capability('pageLoadStrategy', "eager")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--user-data-dir=D:\\Python\\rewards\\mr\\user_data\\" + login)
options.add_argument("--enable-javascript")
options.headless = False
#options.add_argument('--headless')
#options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 1, "profile.block_third_party_cookies": False})
br_ver = OperationSystemManager().get_browser_version_from_os(ChromeType.GOOGLE)
version_main=int(br_ver.split('.')[0])
driver = undetected_chromedriver.Chrome(driver_executable_path="C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe", options=options, seleniumwire_options=seleniumwire_options)

def wait_element(driver, by : str, value : str) -> WebElement:
    while (True):
        try:
            element = driver.find_element(by, value)
            return element
        except(selenium.common.exceptions.NoSuchElementException):
            pass


def wait_elements(driver, by : str, value : str) -> WebElement:
    while (True):
        try:
            elements = driver.find_elements(by, value)
            return elements
        except(selenium.common.exceptions.NoSuchElementException):
            pass


def open_page():
    driver.get(url)


def get_login_input():
    field = wait_element(driver, By.XPATH, "//input[@type='text']")
    return field


def get_password_input():
    field = wait_element(driver, By.XPATH, "//input[@type='password']")
    return field


def get_button():
    button = wait_element(driver, By.XPATH, "//button[@type='submit']") 
    return button


def generate_random_string():
    length = random.randint(5, 16)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string


def get_random_email_provider():
    providers = ["@gmail.com", "@mail.ru", "@sfedu.ru", "@yandex.ru"]
    rand = random.randint(0, 3)
    return providers[rand]


def get_random_email():
    return generate_random_string() + get_random_email_provider()


def get_random_password():
    # Ensure the password contains at least one of each: uppercase, lowercase, digit, and symbol
    length = random.randint(8, 16)
    
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one symbol
    ]
    
    # Fill the rest with a random mix of the valid characters
    password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - 4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)


def type_gibberish(login, password):
    try:
        login_input = get_login_input()
        password_input = get_password_input()
        login_input.clear()
        password_input.clear()
        login_input.send_keys(login)
        password_input.send_keys(password)
        button = get_button()
        return True
    except(Exception):
        traceback.print_exc()
        return False


if __name__ == "__main__":
    chromedriver_autoinstaller.install() 
    open_page()
    while True:
        if not type_gibberish(get_random_email(), get_random_password()):
            open_page()
        time.sleep(5)