from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import os
from dotenv import load_dotenv

load_dotenv()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
SIMILAR_ACCOUNT=os.environ.get('SIMILAR_ACCOUNT')
USERNAME=os.environ.get('USERNAME')
PASSWORD=os.environ.get('PASSWORD')
driver=webdriver.Chrome(options=chrome_option)

class InstaFollwer:
    def __init__(self,driver):
        self.driver1=driver

    def longin(self):

        self.driver1.get("https://www.instagram.com/accounts/login")
        time.sleep(5)
        user=self.driver1.find_element(By.XPATH,value="//*[@id='loginForm']/div/div[1]/div/label/input")
        user.send_keys(USERNAME)
        pasa=self.driver1.find_element(By.XPATH,value="//*[@id='loginForm']/div/div[2]/div/label/input")
        pasa.click()
        pasa.send_keys(PASSWORD,Keys.ENTER)
        time.sleep(10)
        print("LOGINED Sucessfully")
        not_now=self.driver1.find_element(By.XPATH,value="//div[contains(text(), 'Not now')]") 
        #"//*[@id='mount_0_0_df']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
        if not_now:
            not_now.click()
        # not_now.click()
        time.sleep(10)
        noti=self.driver1.find_element(By.XPATH,value="//button[contains(text(), 'Not Now')]")
        if noti:
            noti.click()
        time.sleep(10)
        self.driver1.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")


    def find_followers(self):
        print("FOLLOWERS FIND PANA PORAN")
        time.sleep(10)
        # self.driver1.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        # time.sleep(5)
        target=self.driver1.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a")
        target.click()
        time.sleep(5)
        modal_xpath="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal=self.driver1.find_element(By.XPATH,value=modal_xpath)
        for i in range(10):
            self.driver1.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",modal)
            time.sleep(5)


    def follow(self):
        print("FOLLOW PANA PORAN")
        follow_button=self.driver1.find_elements(By.XPATH,value="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[94]/div/div/div/div[3]/div/button")
        time.sleep(5)
        for button in follow_button:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button=self.driver.find_element(By.XPATH,value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                time.sleep(3)


        # x9f619



BOT=InstaFollwer(driver=driver)
BOT.longin()
BOT.find_followers()
BOT.follow()