from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

# Define your TikTok username and password here
username = ""
password = ""

# Create a Chrome WebDriver instance with the specified service and options
chrome_service = Service(r'C:\chromedriver.exe')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open TikTok's website
driver.get("https://www.tiktok.com/")

# Wait for the "Log in" button to be clickable
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-e2e='top-login-button' and @id='header-login-button']"))
)
login_button.click()
time.sleep(3)

# Wait for the "Use phone / email / username" element to be clickable
use_phone_email_username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//p[text()='Use phone / email / username']"))
)
use_phone_email_username.click()
time.sleep(3)

# Wait for the "Log in with email or username" link to be clickable
login_with_email_or_username_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/login/phone-or-email/email' and contains(text(), 'Log in with email or username')]"))
)
login_with_email_or_username_link.click()
time.sleep(3)

# Wait for the input field to be clickable
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @placeholder='Email or username' and @name='username' and contains(@class, 'tiktok-11to27l-InputContainer')]"))
)
input_field.click()
input_field.send_keys(username)
time.sleep(3)

# Wait for the password input field to be clickable
password_input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='password' and @placeholder='Password' and @autocomplete='new-password' and contains(@class, 'tiktok-wv3bkt-InputContainer')]"))
)
password_input_field.click()
password_input_field.send_keys(password)
time.sleep(3)

# Wait for the "Log in" button to be clickable
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @data-e2e='login-button' and contains(text(), 'Log in')]"))
)
login_button.click()
time.sleep(3)

# Wait for the login to complete (you may need to adjust the waiting time)
time.sleep(10)

# Continue with the rest of your TikTok automation...

# Close the WebDriver
driver.quit()
