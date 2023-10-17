import os
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.speedtest.net/"
CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]

auth_token = os.environ["AUTH_TOKEN"]
account_sid = os.environ["ACCOUNT_SID"]
twilio_number = os.environ["TWILIO_NUM"]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        start_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        start_button.click()

        time.sleep(110)
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

    def send_message(self):
        client = Client(account_sid, auth_token)
        message = f"Your internet download speed is: {self.down} Mbps\n Your upload speed is: {self.up} Mbps"
        client.messages.create(body=message, from_=twilio_number, to='+15879693432')

