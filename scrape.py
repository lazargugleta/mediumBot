from selenium import webdriver
from time import sleep

from creditentials import username, password

class MediumBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def remove_cookies(self):
        close_popup = self.driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/div[2]')
        close_popup.click()

    def login_google(self):
        self.driver.get('https://medium.com/')

        sleep(1)

        #self.remove_cookies()
        sign_in = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[3]/div/div[2]/h4/a')
        sign_in.click()

        google_sign_in = self.driver.find_element_by_xpath('//*[@id="susi-modal-google-button"]/a')
        google_sign_in.click()

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(username)

        go_to_password = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        go_to_password.click()

        sleep(1.5)

        password_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_in.send_keys(password)

        done_with_password = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
        done_with_password.click()

    def login_facebook(self):
        self.driver.get('https://medium.com/')

        sleep(0.7)

        #self.remove_cookies()
        sign_in = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/div/div[3]/div/div[2]/h4/a')
        sign_in.click()

        facebook_sign_in = bot.driver.find_element_by_xpath('//*[@id="susi-modal-fb-button"]/div/a')
        facebook_sign_in.click()

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        log_in = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        log_in.click()
        sleep(3)
        self.earnings()
        self.stats()

    def earnings(self):
        self.driver.get('https://medium.com/me/partner/dashboard')
        sleep(3)
        #self.remove_cookies()
        total_earnings = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/section/div/div[2]/div/div/div/div[3]')
        print(total_earnings.text)

    def stats(self):
        self.driver.get('https://medium.com/me/stats')
        sleep(3)
        total_views = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/div[1]')
        print(total_views.text)

bot = MediumBot()
bot.login_facebook()
