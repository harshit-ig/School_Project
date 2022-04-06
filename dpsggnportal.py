from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(5)


'''User Defined Variables Start'''
details = {}
baseUrl = "https://www.dpsggncampuscare.org"
'''User Defined Variables End'''

'''User Defined Functions Start'''
def login(username, passwords):
    if type(passwords) is list:
        driver.get(baseUrl)
        app = driver.find_element(By.CSS_SELECTOR, 'a.webtextnameerp')
        app.click()
        popup= driver.window_handles[1]
        driver.switch_to.window(popup)

        userfld = driver.find_element(By.XPATH, '//*[@id="txtUserID"]')
        userfld.send_keys(username)
        usernext = driver.find_element(By.XPATH,'//*[@id="showRight"]')
        usernext.click()
        passfld = driver.find_element(By.XPATH, '//*[@id="password"]')
        passnext = driver.find_element(By.XPATH,'//*[@id="btnLogin"]')
        for password in passwords:
            try:
                passfld.clear()
                print(password)
                passfld.send_keys(password)
                passnext.click()
            except:
                break

    elif type(passwords) is str:
        driver.get(baseUrl)
        app = driver.find_element(By.CSS_SELECTOR, 'a.webtextnameerp')
        app.click()
        popup= driver.window_handles[1]
        driver.switch_to.window(popup)

        userfld = driver.find_element(By.XPATH, '//*[@id="txtUserID"]')
        userfld.send_keys(username)
        usernext = driver.find_element(By.XPATH,'//*[@id="showRight"]')
        usernext.click()
        passfld = driver.find_element(By.XPATH, '//*[@id="password"]')
        passfld.send_keys(passwords)
        passnext = driver.find_element(By.XPATH,'//*[@id="btnLogin"]')
        passnext.click()


'''User Defined Functions End'''


def Studentinfo(username, passwords):
    login(username ,passwords)
    personal = driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a/span[1]')
    personal.click()
    myprofile = driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[1]/a')
    myprofile.click()

    #Student Info
    stuname = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[4]/div[1]/div[1]/div[2]/div/strong').text
    details['Name']= stuname
    sclass = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div[4]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
    details['Class']= sclass
    regno = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[4]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]').text
    details['Reg']= regno
    #Email ID
    femailtxt = driver.find_element(By.XPATH,'//*[@id="FEmailIDText"]').text
    memailtxt = driver.find_element(By.XPATH,'//*[@id="MEmailIDText"]').text
    details['FEmail']= femailtxt
    details['MEmail']= memailtxt

