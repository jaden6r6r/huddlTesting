from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select 
import time

class hudlTester:
    #Class constructor 
    def __init__(self, username, password):
        #instantiate the variables used in the testing. 
        self.username = username
        self.password = password
        self.driver = None
        self.correctLoginResult = None
        self.emailFormatResult = None
        self.absentPasswordResult = None
        self.noEmailSuppliedResult = None
    
    #generic login to prevent need for repeated code. 
    def login(self):
        self.driver.get('https://www.hudl.com/login')
        self.driver.maximize_window()

    #test for correct login details provided. 
    def correctLogin(self):
        #login and provide username and password
        self.driver = webdriver.Chrome('c:/temp/chromedriver')
        self.login()
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'email')))
        elem.send_keys(self.username)
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'password')))
        elem.send_keys(self.password)
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'logIn')))
        elem.send_keys('\uE007')
        #try/catch will prove presence of element only visible in log in page - if not visible, login failed.         
        try:
            elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'uni-subhead')))
            self.correctLoginResult = 'Passed'
            self.driver.quit()
            return 
        except:
            self.correctLoginResult = 'Failed'
            self.driver.quit()
            return 

    def wrongEmailFormat(self):
        #given an incorrect email, the response of the website must match what is declared in this function and not match when a correct log in is provided. 
        self.driver = webdriver.Chrome('c:/temp/chromedriver')
        self.login()
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'email')))
        elem.send_keys('tester@@email.ran') #double domain '@' symbol not valid format. 
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'password')))
        elem.send_keys(self.password)
        elem.send_keys('\uE007')
        try:
            #error box should be found. 
            elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'login-error-container')))
            time.sleep(2)
            if elem.text == "We didn't recognize that email and/or password. Need help?":
                self.emailFormatResult = 'Passed'
                self.driver.quit()

                return
            else:
                self.emailFormatResult = 'Failed'
                self.driver.quit()

                return
        except:
            #login is successful. 
                self.emailFormatResult = 'Passed'
                self.driver.quit()
                return
    
    def noPasswordSupplied(self):
        #check for the ability to login even when no password is given.
        self.driver = webdriver.Chrome('c:/temp/chromedriver')
        self.login()
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'email')))
        elem.send_keys('tester@email.com') #email not important for this test. 
        #Two approaches for this test: use of Enter key to attempt to submit & attempt to click login button. 
        elem.send_keys('\uE007')
        try:
            #error box should be found. 
            elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'login-error-container')))
            time.sleep(2)
            if elem.text == "We didn't recognize that email and/or password. Need help?":
                self.absentPasswordResult = 'Passed'
            else:
                self.absentPasswordResult = 'Failed'
        except:
            #login is successful. 
                self.absentPasswordResult = 'Passed' 
        if self.absentPasswordResult == 'Passed': #Now try to login with click
            elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'email')))
            elem.clear()
            elem.send_keys('tester@email.com')
            time.sleep(2)
            elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'logIn')))
            elem.click()
            try:
                #error box should be found. 
                elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'login-error-container')))
                time.sleep(2)
                if elem.text == "We didn't recognize that email and/or password. Need help?":
                    self.absentPasswordResult = 'Passed'
                    self.driver.quit()
                else:
                    self.absentPasswordResult = 'Failed'
                    self.driver.quit()

            except:
                #login is successful. 
                self.absentPasswordResult = 'Passed' 
                self.driver.quit()
    
    def noEmailSupplied(self):
        #Expect to get error box when logging in without email. 
        self.driver = webdriver.Chrome('c:/temp/chromedriver')
        self.login()
        elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'password')))
        elem.send_keys('passwordOnly') #email not important for this test. 
        #Two approaches for this test: use of Enter key to attempt to submit & attempt to click login button. 
        elem.send_keys('\uE007')
        try:
            #error box should be found. 
            elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'login-error-container')))
            time.sleep(2)
            if elem.text == "We didn't recognize that email and/or password. Need help?":
                self.absentPasswordResult = 'Passed'
            else:
                self.absentPasswordResult = 'Failed'
        except:
            #login is successful. 
                self.absentPasswordResult = 'Passed' 
        if self.absentPasswordResult == 'Passed': #Now try to login with click
            elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'password')))
            elem.clear()
            elem.send_keys('passwordOnly')
            time.sleep(2)
            elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,'logIn')))
            elem.click()
            try:
                #error box should be found. 
                elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'login-error-container')))
                time.sleep(2)
                if elem.text == "We didn't recognize that email and/or password. Need help?":
                    self.noEmailSuppliedResult = 'Passed'
                    self.driver.quit()
                else:
                    self.noEmailSuppliedResult = 'Failed'
                    self.driver.quit()

            except:
                #login is successful. 
                self.noEmailSuppliedResult = 'Passed' 
                self.driver.quit()

            

            
    def orchestrationTest(self):
        self.correctLogin()
        self.wrongEmailFormat()
        self.noPasswordSupplied()
        self.noEmailSupplied()
        print('Result of correctLogin test :',self.correctLoginResult)
        print('Result of wrongEmailFormat test :',self.emailFormatResult)
        print('Result of noPasswordSupplied test :',self.absentPasswordResult)
        print('Result of noEmailSupplied test :',self.noEmailSuppliedResult)



hudlTester = hudlTester('Jahranebryan12@hotmail.com','shellgrove123')
hudlTester.orchestrationTest()
