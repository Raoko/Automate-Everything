# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import subprocess
import time

""" Update 3.7.4 """
""" 08/8/2018 """

class webmate():

    """  CHROME OPTIIONS """
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()

        """ CHROME ARGUMENTS """
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-notifications')
        self.chrome_options.add_argument('--allow-hidden-media-playback')

    """ *REQUIRED* HIDDEN OR OPEN BROWSER """
    def loadDriver(self, PHANTOM=False):
        if PHANTOM == True:
            self.chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        print "Driver Success..."

    """ *REQUIRED* GO TO URL SITE """
    def goTo(self, URL):
        self.driver.get(URL)
        print "URL Success..."

    """ Automated form input """
    def formInput(self, ID=None, XPATH=None, NAME=None, KEY=None, pressEnter=False, clear=False):
        time.sleep(0.1)
        self.driver.implicitly_wait(10)
        if XPATH:
            elem = self.driver.find_element_by_xpath(XPATH)
            if clear == True:
                elem.clear()
        elif ID:
            elem = self.driver.find_element_by_id(ID)
        elif NAME:
            elem = self.driver.find_element_by_name(NAME)
        elem.send_keys(KEY)
        if pressEnter == True:
            time.sleep(1)
            elem.send_keys(Keys.RETURN)
        print "Success..."

    """ Clicks on buttons"""
    def buttonClick(self, CLASS=None, XPATH=None, NAME=None):
        time.sleep(0.1)
        self.driver.implicitly_wait(10)
        if XPATH:
            self.driver.find_element_by_xpath(XPATH).click()
        elif ID:
            self.driver.find_element_by_class(CLASS).click()
        elif NAME:
            self.driver.find_element_by_name(NAME).click()
        print "Success..."

    """ KILL ANY APPLICATION """
    def killApp(self, app, times=1):
        for i in range(times):
            subprocess.call(["taskkill", "/f", "/IM", app])

    """ QUIT WEBDRIVER """
    def quitDriver(self):
        self.driver.quit()
        print "Driver quit successfull"

    """ Wait for html ID to load"""
    def waitFor(self, delay, wait_for_id):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, wait_for_id)))
            print "Success..."
        except TimeoutException:
            quit()

    """ Web Scrape """
    def getText(self, XPATH=None, CLASS=None):
        if XPATH:
            try:
                time.sleep(1)
                for elem in self.driver.find_elements_by_xpath(XPATH):
                    time.sleep(1)
                    self.webScrape = elem.text
                    
            except:
                print "Failed getting text information"
        if CLASS:
            try:
                time.sleep(0.5)
                for elem in self.driver.find_elements_by_class(CLASS):
                    time.sleep(0.5)
                    self.webScrape = elem.text
            except:
                print "Failed getting text information"

    """ FOR DROP DOWN LIST ----> #BETA <----"""
    def getSelect(self, NAME, VALUE):
        time.sleep(0.5)
        select = Select(self.driver.find_element_by_name(NAME))
        select.all_selected_options
        select.options

        # select by value
        select.select_by_value(VALUE)

if __name__ == "__main__":
    pass
