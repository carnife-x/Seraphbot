from selenium import webdriver
import time

x=1
class SerapBot:
    def __init__(self,username,pwd):
#        options = webdriver.ChromeOptions() chrome_options=options
#        options.add_argument('--ignore-certificate-errors')
#        options.add_argument('--ignore-ssl-errors')
#        driver = webdriver.Chrome()
         self.username = username
         self.pwd = pwd
        
    def login(self):
        driver = webdriver.Chrome()
        driver.minimize_window()
        driver.get("http://www.gstatic.com/generate_204")
        try:
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[1]/div/input[1]').send_keys(self.username)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[1]/div/input[2]').click()
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[2]/div/input[4]').send_keys(self.pwd)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[2]/div/button').click()
            print('Login Succesfull')
            driver.close()
        except:
            print('Redirect')
            driver.get("http://www.msftconnecttest.com/redirect")
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[1]/div/input[1]').send_keys(self.username)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[1]/div/input[2]').click()
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[2]/div/input[4]').send_keys(self.pwd)
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/form[2]/div/button').click()
            print('Login Succesfull')
            driver.close()
            
    def Logout(self):
        print('-----Logging Off-------')
        driver = webdriver.Chrome()
        driver.minimize_window()
        try:
            self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[3]/ul/div/a[1]').click()
            print('Button not found')
        except:
            driver.get("https://seraph.karunya.edu:1003/logout?050e040e0a0389db")
            print('Logout Succesfull')
            time.sleep(2)
            driver.close()
i=5
pas=open('pass.txt','r')
pwd=pas.read(11)
pwd=str(pwd)
a=SerapBot('URK17CS138',pwd)
while x>0:
    a.login()
#    t_end = time.time() + 5
#    while time.time() < t_end:
#        time.sleep(1)
#        i=i-1
#        print(i)
#    print('End of Session')
#    a.Logout()
#    print('-----Restarting Session-------')
    break