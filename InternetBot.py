from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import os, time

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"
GUARANTEED_DOWN = 500
GUARANTEED_UP = 500


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(42)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.down}, up: {self.up}")
        return self.up, self.down

    def tweet_at_provider(self, up, down):
        self.driver.get(TWITTER_URL)
        time.sleep(5)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//label[@class="css-1dbjc4n r-1roi411 r-z2wwpe r-rs99b7 r-18u37iz"]')))
        email = self.driver.find_element(By.XPATH, '//label[@class="css-1dbjc4n r-1roi411 r-z2wwpe r-rs99b7 r-18u37iz"]')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            unusual_activity_verification = self.driver.find_element(By.XPATH, '//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
            unusual_activity_verification.send_keys(TWITTER_USERNAME)
            time.sleep(1)
            unusual_activity_verification.send_keys(Keys.ENTER)
            time.sleep(2)
            password = self.driver.find_element(By.XPATH, '//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu" and @type="password"]')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            tweet = self.driver.find_element(By.XPATH, '//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
            tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {GUARANTEED_DOWN}down/{GUARANTEED_UP}up?")
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0" and text()="Post"]').click()
        except selenium.common.exceptions.NoSuchElementException:
            password = self.driver.find_element(By.XPATH, '//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu" and @type="password"]')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            tweet = self.driver.find_element(By.XPATH, '//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
            tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {GUARANTEED_DOWN} down/{GUARANTEED_UP} up?")
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0" and text()="Post"]').click()

