# pip install pandas 
# pip install selenium
from cv2 import contourArea
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
import csv
from datetime import date


option = webdriver.ChromeOptions()
option.add_argument('--headless')#Hides the web browser 
driver = webdriver.Chrome(options=option)




'''User Defined Variables Start'''

baseUrl = "https://www.dpsggncampuscare.org"

'''User Defined Variables End'''



'''User Defined Functions Start'''
def sendmail():
    pass

def display(csvfile):
    data = pandas.read_csv(csvfile)
    return data

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

def Studentinfo(username, passwords):
    details = {}
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
    return details

def addabook():
    print('''
    1. Add A New Book.
    2. Update Quantity.\n
    
    ''')
    usrchoice = input('Select An Option: ')
    if usrchoice.isnumeric() and int(usrchoice) == 1:
        while True:
            db = open('db.csv')
            database = csv.reader(db)
            bookid = int(input('Enter Book ID: '))
            bookidindb = False
            for data in database:
                if len(data)==0:
                    continue
                if str(bookid) == data[0]:
                    bookidindb = True
            if bookidindb == True:
                print('Book ID Already Present!!!')
                continue
            bookname = input('Enter Book Name: ')
            booknameindb = False
            db.seek(0)
            for data in database:
                if len(data)==0:
                    continue
                if bookname == data[1]:
                    booknameindb = True
            if booknameindb == True:
                print('Book Already In Database!!!')
                continue
            quantity = int(input('Number of Books: '))
            issuedbook = 0
            today = date.today()
            bookdata = [bookid, bookname, quantity, issuedbook, today,]
            db.close()
            db = open('db.csv', 'a')
            database = csv.writer(db)
            database.writerow(bookdata)
            db.close()
            usrchoice = ''
            usrchoice = input('''
            1. Add Another Book.
            2. Return To Main Menu. '''
            )
            if int(usrchoice) == 1:
                continue
            break
    elif usrchoice.isnumeric() and int(usrchoice) ==2:
        lst =[]
        bookidorname = input('Enter Book ID or Book Name: ')
        db = open('db.csv', 'r')
        database = csv.reader(db)
        for data in database:
            if len(data)==0:
                continue
            bkname = data[1]
            bkid = data[0]
            if bookidorname.lower() == bkname.lower() or bookidorname==bkid:
                print('\n \n Book Name: ',data[1],'\n', 'Book ID: ', data[0], '\n', 'Quantity: ', data[2], '\n')
                quantity = int(input('Enter Updated Quantity: '))
                data[2]=quantity
            lst.append(data)
        db.close()
        db = open('db.csv', 'w')
        database = csv.writer(db)
        database.writerows(lst)
        db.close()


    else:
        pass
    
def removeabook():
    lst =[]
    bookidorname = input('Enter Book ID or Book Name: ')
    db = open('db.csv', 'r')
    database = csv.reader(db)
    for data in database:
        if len(data)==0:
            continue
        bkname = data[1]
        bkid = data[0]
        if bookidorname.lower() == bkname.lower() or bookidorname==bkid:
            print('Details Of The Book Removed\n')
            print('\n \n Book Name: ',data[1],'\n', 'Book ID: ', data[0], '\n', 'Quantity: ', data[2], '\n')
            continue
        lst.append(data)
    db.close()
    db = open('db.csv', 'w')
    database = csv.writer(db)
    database.writerows(lst)
    db.close()

def viewbooks():
    print(display('db.csv'))
    print()
    wait = input('Press Enter to return to Main Menu...')

def issue():
    user = input('Enter The Registration Number: ')
    user = 'p'+ user
    passwd = input('Enter The Password: ')
    details = Studentinfo(user, passwd)
    print(details)

def returnbook():
    pass

'''User Defined Functions End'''
sendmail()
while True:
    print('\n'*20)
    print(
    '''
                    LIBRARY MANAGEMENT SYSTEM


                        1. Add A Book
                        2. Remove A Old Book
                        3. View Book List
                        4. Issue Book To Student
                        5. Return Book
                        6. Exit
                    ''')
    userchoice = input('Select An Option: ')
    print('\n'*20)
    if userchoice.isnumeric():
        pass
    else:
        continue
    if int(userchoice) == 1:
        addabook()
    elif int(userchoice)==2:
        while True:
            removeabook()
            userchoice=''
            userchoice = input('''
            1. Remove Another Book.
            2. Return To Main Menu.
            ''')
            if userchoice.isnumeric() and int(userchoice)==1:
                continue
            else:
                break
    elif int(userchoice)== 3:
        viewbooks()
    elif int(userchoice)== 4:
        issue()
    elif int(userchoice)== 5:
        returnbook()
    elif int(userchoice)== 6:
        break
    
