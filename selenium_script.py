import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
import time
# Logging setup
logging.basicConfig(level=logging.INFO)



client = MongoClient("______MONOGO_URI______")
db = client['twitter_trends']
collection = db['trending_topics']

#Mesh Proxy setup
PROXY_HOST = ""
PROXY_PORT = ""
PROXY_USER = ""
PROXY_PASS = ""
options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server=http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}")

# # Add proxy to Chrome options
options = webdriver.ChromeOptions()
# # Initialize WebDriver

# WebDriver setup
# Set up Chrome options (optional: headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)

# Path to your ChromeDriver
chrome_driver_path = 'C:/chromedriver-win32/chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


try:
    logging.info("Opening Twitter login page...")
    driver.get("https://twitter.com/login")

    logging.info("Waiting for username field to appear...")
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "text"))
    )
    logging.info("Entering username...")
    username_field.send_keys("______YOUR_EMAIL______")

    logging.info("Clicking Next button...")
    driver.find_element(By.XPATH, "//span[text()='Next']").click()

    logging.info("Waiting for password field to appear...")
    password_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    logging.info("Entering password...")
    password_field.send_keys("______YOUR_PASSWORD______")

    logging.info("Clicking Log In button...")
    driver.find_element(By.XPATH, "//span[text()='Log in']").click()

    logging.info("Waiting for 'What’s happening' span to appear...")
    WebDriverWait(driver, 40).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'What’s happening')]")
        )
    )

    # Fetch hashtags
    logging.info("Fetching hashtags...")
    hashtag_elements = WebDriverWait(driver, 70).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//span[starts-with(text(), '#')]")
        )
    )
    hashtags = [element.text for element in hashtag_elements]
    trending_data = {"end_time": time.strftime("%Y-%m-%d %H:%M:%S"),"trends": hashtags}
    collection.insert_one(trending_data)


except TimeoutException as e:
    logging.error("Timeout while waiting for an element: ", exc_info=e)
except NoSuchElementException as e:
    logging.error("Element not found: ", exc_info=e)
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    with open("debug_page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
finally:
    logging.info("Closing the WebDriver.")
    driver.quit()
