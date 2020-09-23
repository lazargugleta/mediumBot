from selenium import webdriver
from termcolor import colored
import sys
from time import sleep
import re
from datetime import datetime
import math
from huepy import *

from creditentials import username, password

class MediumBot():
    def __init__(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        #print("Current Time: ", current_time)

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
            sign_in = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/div[4]/div/div[2]/h4/span/a')
            sign_in.click()

            facebook_sign_in = bot.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/div/a')
            bot.driver.execute_script("arguments[0].click();", facebook_sign_in)

            email_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input')
            email_in.send_keys(username)

            password_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input')
            password_in.send_keys(password)

            log_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button')
            log_in.click()
            sleep(5)
        
            #self.earnings()
            #self.followers()
            self.stats()
            #self.unfollow_all()
            #self.follow_random_article()
            self.driver.close()
        except:
            print(colored("Something failed!\n", "red"))
            self.driver.close()
            return True
            

    def earnings(self):
        self.driver.get('https://medium.com/me/partner/dashboard')
        sleep(3)
        #self.remove_cookies()
        total_earnings = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/section/div/div[2]/div/div/div/div[3]')
        print(colored("You made", "blue"), colored(total_earnings.text, "magenta"), colored("this month", "blue"))
        return True
    
    def followers(self):
        self.driver.get('https://medium.com/@lazar.gugleta')
        sleep(3)
        num_of_followers = self.driver.find_element_by_xpath('/html/body/div/div/section/div[1]/div[2]/div[2]/div[4]/span/div/div[2]/a')        
        print(colored("You have: ", "blue" ) + colored(num_of_followers.text, "magenta"))
        return True

    def stats(self):
        global new_val
        self.driver.get('https://medium.com/me/stats')
        sleep(3)
        num_of_days = len(self.driver.find_elements_by_class_name('bargraph-bar'))
        total_views = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/div[1]')
        print(colored("30 days views: ", "blue") + colored(total_views.text, "magenta") + colored(" views", "blue"))
        total_reads = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/ul/li[2]/div/div[1]')
        print(colored("30 days reads: ", "blue") + colored(total_reads.text, "magenta"))
        last_story_views = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[4]/table/tbody/tr[2]/td[2]/span[2]')
        last_story_reads = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[4]/table/tbody/tr[2]/td[3]/span[2]')
        last_story_fans = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[4]/table/tbody/tr[2]/td[5]/span[2]')
        views_nr = last_story_views.text.split()[0]
        reads_nr = last_story_reads.text.split()[0]
        fans_nr = last_story_fans.text.split()[0]
        print(blue("Last story:"), purple(views_nr) + "\n" +blue("Reads:") , purple(reads_nr) + "\n" + blue("Fans:") , purple(fans_nr))
        new_val = total_views.text
        #average views
        match1 = [int(s) for s in total_views.text.split() if s.isdigit()]
        match2 = re.findall("([0-9]+[,.]+[0-9]+)", total_views.text)
        if not match2:
            res = match1[0]
        else:
            res = int(match2[0].replace(',',''))
        
        print(colored("Average views in", "blue") , colored(num_of_days, "magenta"),  colored("days is", "blue") , bold(colored(round(res/num_of_days, 2), "magenta")))
        return True

    def unfollow_all(self):
        self.driver.get('https://medium.com/@lazar.gugleta/following')
        sleep(3)
        n = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[1]/a[1]').get_attribute('title')
        match1 = [int(s) for s in n.split() if s.isdigit()]
        match2 = re.findall("([0-9]+[,.]+[0-9]+)", n)
        if not match2:
            res = match1[0]
        else:
            res = int(match2[0].replace(',',''))
        print(colored("Currently following: ", "blue") + colored(str(res), "magenta") + colored(" users", "magenta"))
        final = 1674
        list = self.driver.find_elements_by_xpath("//span[contains(text(), 'Following')]")
        while len(list) < 150:
            self.driver.execute_script("window.scrollBy(0,4000)")
            sleep(1)
            list = self.driver.find_elements_by_xpath("//span[contains(text(), 'Following')]")
        pop_up = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/button')
        pop_up.click()
        for i in range(len(list)):
            sleep(0.1)
            self.driver.execute_script("arguments[0].scrollIntoView()", list[i])
            list[i].click()
            res -= 1
            if res <= final:
                print(colored("Complete", "green"))
                return False

        

    def average_views(self):
        self.driver.get('https://medium.com/me/stats')
        sleep(3)
        num_of_days = len(self.driver.find_elements_by_class_name('bargraph-bar'))
        total_views = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/ul/li[1]/div/div[1]').text
        
        match1 = [int(s) for s in total_views.split() if s.isdigit()]
        match2 = re.findall("([0-9]+[,.]+[0-9]+)", total_views)
        if not match2:
            res = match1[0]
        else:
            res = int(match2[0].replace(',',''))
        print(colored("Average views in", "blue") , colored(num_of_days, "magenta"),  colored("days is", "blue") , colored(res/num_of_days, "magenta"))
        
            

    def follow_random_article(self):
        self.driver.get('https://elemental.medium.com/a-supercomputer-analyzed-covid-19-and-an-interesting-new-theory-has-emerged-31cb8eba9d63')
        sleep(3)
        
        claps = self.driver.find_element_by_xpath("/html/body/div/div/div[7]/div/div[1]/div/div[4]/div/div[1]/div[1]/span[2]/div/div[2]/div/h4/button")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", claps)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div/div/div[7]/div/div[1]/div/div[4]/div/div[1]/div[1]/span[2]/div/div[2]/div/h4/button").click()
        sleep(10)
        show_more_claps = self.driver.find_element_by_xpath("//button[contains(text(), 'Show more claps')]")

        text = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/h2").text
        split_string = text.split(" from ")
        number_of_people = int(split_string[1].split(" ")[0])
        number_of_rounds = math.floor(number_of_people / 10) - 2

        if (number_of_rounds > 100):
            number_of_rounds = 100

        for i in range(number_of_rounds):
            self.driver.execute_script("arguments[0].scrollIntoView(true)", show_more_claps)
            sleep(1.5)
            show_more_claps.click()
            sleep(0.5)
        cnt = 0
        for i in range(number_of_rounds * 10, 2, -1):
            follow_user = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[" + str(i-40) + "]/div/div[2]/button")
            self.driver.execute_script("arguments[0].scrollIntoView()", follow_user)
            sleep(0.15)
            if (follow_user.text == "Follow"):
                if (cnt == 150):
                    break
                cnt+=1
                follow_user.click()
                if (cnt > 1):
                    sys.stdout.write("\033[F")
                print(colored('You just followed', 'blue'), colored(cnt, 'magenta'), colored('user(s)', 'magenta'))
                sleep(3)
           
while(1):
    bot = MediumBot()
    if not bot.login_facebook():
        break