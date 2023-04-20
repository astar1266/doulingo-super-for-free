import time
import random
import pyautogui
from selenium import webdriver

email = input ("what on earth is your email bro 💀:")




def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False
    
def getValidCard(cardBin, binMonth, binYear, cvv):
    randDigitLen = 16-len(cardBin)
    while True:
        UnchckCCN = cardBin+str(random.randint(int(10**(randDigitLen-1)), int((10**randDigitLen)-1)))
        if checkLuhn(UnchckCCN):
            ccn = UnchckCCN
            break
        else:
            continue
    if binMonth=="rnd":
        mnth = str(random.randint(1,12))
    else:
        mnth=binMonth
    if binYear=="rnd":
        year = str(random.randint(2022,2030))
    else:
        year = binYear
    if cvv=="rnd":
        cvc = str(random.randint(100,999))
    else:
        cvc = cvv
    full_card = f"{ccn}|{mnth}|{year}|{cvc}"
    return full_card

cardBin = input("Enter the BIN: ")
binMonth = input("Enter the BIN month (e.g. 05 or rnd for random): ")
binYear = input("Enter the BIN year (e.g. 24 or rnd for random): ")
cvv = input("Enter the CVV (e.g. 123 or rnd for random): ")

print("Generating valid card numbers...")

for i in range(10):
    thecreditcard = getValidCard(cardBin, binMonth, binYear, cvv).split("|")[0]
    print(thecreditcard)





# create an instance of the Edge driver
# If you use chrome or firefox or any other webbrowser make sure to change webdriver.(your web browser) and use its driver.
driver = webdriver.Edge("C:\\Windows\\msedgedriver.exe")



# load the login page
driver.get("https://www.duolingo.com/log-in?isLogging=true&isLoggingIn=true")
driver.implicitly_wait(60)
    
# click the signup button
signup = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/div[2]/button')
signup.click()
driver.implicitly_wait(60)
    
# enter age
ageinput = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[1]/label/div/input')
ageinput.send_keys('24')
driver.implicitly_wait(60)
    

# enter email address
emailinput = driver.find_element_by_xpath("//*[@id='overlays']/div[2]/div/div/form/div[1]/div[1]/div[3]/label/div/input")
emailinput.send_keys(email)
driver.implicitly_wait(60)
    
# enter password
passwordinput = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/form/div[1]/div[1]/div[4]/label/div/input')
passwordinput.send_keys("asdfghjkl")
driver.implicitly_wait(60)
    
# click the create account button
createbutton = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/form/div[1]/button')
createbutton.click()
driver.implicitly_wait(60)

# click on spanish 💀
spanish = driver.find_element_by_xpath('//button[@data-test="language-card language-es"]')
spanish.click()
driver.implicitly_wait(60)

time.sleep(8)

driver.get("https://www.duolingo.com")


clickonclose = driver.find_element_by_css_selector('div[data-test="close-button"]')
clickonclose.click()
driver.implicitly_wait(60)

clickonsuper = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/button')
clickonsuper.click()
driver.implicitly_wait(60)

startmytrail = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/div/div/div[2]/div/div[10]/div/button[1]')
startmytrail.click()
driver.implicitly_wait(60)

startmytrail2 = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/div/div/div[2]/div/div[10]/div/button[1]')
startmytrail2.click()
driver.implicitly_wait(60)

startmytrail3 = driver.find_element_by_xpath('//*[@id="overlays"]/div[2]/div/div/div/div/div[2]/div/div[9]/div/div/div[2]/button[1]')
startmytrail3.click()
driver.implicitly_wait(60)




time.sleep(4)

driver.maximize_window()

pyautogui.leftClick(816,312)
pyautogui.typewrite("messi goat")

time.sleep(1)

pyautogui.click(792,411)
pyautogui.typewrite(thecreditcard)

time.sleep(1)

pyautogui.click(787,510)
pyautogui.typewrite(binMonth + binYear)

time.sleep(1)

pyautogui.click(999,509)
pyautogui.typewrite(cvv)

time.sleep(1)

pyautogui.click(832,609)
pyautogui.typewrite("10010")

time.sleep(1)

pyautogui.click()
time.sleep(1)
pyautogui.click(995,705)