from selenium import webdriver
from time import sleep
import re
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from creditentials import username, password

class MediumBot():
    def __init__(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time: ", current_time)

        self.driver = webdriver.Chrome()
        #self.driver.minimize_window()

    def remove_cookies(self):
        close_popup = self.driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/div[2]')
        close_popup.click()

    def login_google(self):
        self.driver.get('https://medium.com/')

        sleep(3)

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
        try:
            self.driver.get('https://medium.com/')

            sleep(1)

            #self.remove_cookies()
            sign_in = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[3]/div/div[2]/h4/a')
            sign_in.click()

            facebook_sign_in = bot.driver.find_element_by_xpath('//*[@id="susi-modal-fb-button"]/div/a')
            bot.driver.execute_script("arguments[0].click();", facebook_sign_in)

            email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
            email_in.send_keys(username)

            password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
            password_in.send_keys(password)

            log_in = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
            log_in.click()
            sleep(5)
        
            #self.earnings()
            #self.followers()
            #self.stats()
            self.unfollow_all()
            #self.follow_random_article()
            self.driver.close()
        except:
            print("Something failed!\n")
            self.driver.close()
            return True
            

    def earnings(self):
        self.driver.get('https://medium.com/me/partner/dashboard')
        sleep(3)
        #self.remove_cookies()
        total_earnings = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/section/div/div[2]/div/div/div/div[3]')
        print("You made " + total_earnings.text + " this month")
    
    def followers(self):
        self.driver.get('https://medium.com/@lazar.gugleta')
        sleep(3)
        num_of_followers = self.driver.find_element_by_xpath('/html/body/div/div/section/div[1]/div[2]/div[2]/div[4]/span/div/div[2]/a').getAttribute("title")
        print("You have: "+ num_of_followers.text)

    def stats(self):
        global new_val
        self.driver.get('https://medium.com/me/stats')
        sleep(3)
        total_views = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/div[1]')
        print("30 days views: " + total_views.text + " views")
        total_reads = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/ul/li[2]/div/div[1]')
        print("30 days reads: " + total_reads.text)
        last_story_views = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[4]/table/tbody/tr[2]/td[2]/span[2]')
        last_story_reads = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[4]/table/tbody/tr[2]/td[3]/span[2]')
        last_story_fans = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[4]/table/tbody/tr[2]/td[5]/span[2]')
        print("Last story: " + last_story_views.text + " views, " + last_story_reads.text + " reads and " + last_story_fans.text + " fans\n")
        new_val = total_views.text

    def unfollow_all(self):
        self.driver.get('https://medium.com/@lazar.gugleta/following')
        sleep(3)
        n = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[2]/a[1]').get_attribute('title')
        match1 = [int(s) for s in n.split() if s.isdigit()]
        match2 = re.findall("([0-9]+[,.]+[0-9]+)", n)
        if not match2:
            res = match1[0]
        else:
            res = int(match2[0].replace(',',''))
        print("Current following: " + str(res))
        final = 940
        list = self.driver.find_elements_by_xpath("//span[contains(text(), 'Following')]")
        for i in range(res):
            sleep(0.25)
            list[i].click()
            res -= 1
            if res <= final:
                print("Complete")
                return False

    def follow_random_article(self):
        self.driver.get('https://medium.com/better-programming/why-most-code-sucks-ebc73b1a8882')
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div[1]/div/div[4]/div[1]/div[2]/div/h4/button').click()
        sleep(3)
        i = 0
        while(i < 10):
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[22]/button').click()
            i+=1
            sleep(2)
        list = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")
        for i in range(100):
            sleep(2)
            list[i].click()

while(1):
    bot = MediumBot()
    if not bot.login_facebook():
        break