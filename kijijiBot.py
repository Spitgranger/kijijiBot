from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
opts = Options()
opts.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, chrome_options=opts)
url = "https://www.kijiji.ca/t-login.html?targetUrl=L3Atc2VsZWN0LWNhdGVnb3J5Lmh0bWw/XnIrUFRKMS9oU1cxc29PdXAxbjUveFE9PQ--"
tagList = ["gasbike", "motorized bike", "motorized bicycle", "bike engine", "ebike"]
picturePaths = ["C:\picture1.jpg","C:\picture2.jpg"]
username = "thinkpad220@hotmail.com"
password = "windows 95"
itemDescription = "Unlike many others we are NOT resellers of cheap Amazon kits. Highest quality kits on the market. Please see photos for actual pictures of bikes. Call or text 647-795-6360. Motorized bicycles for sale at Robert's Bike Shop! Prebuilts available in 2/4 stroke format. Built by professional team and tested for a minimum of 100km to ensure your safety. Bikes can reach a top speed of 55-60km/h and can go over 130km per tank which only costs $2 to fill. Why spend 5x the price on a eBike which can only go 40km per charge and takes hours to charge? Engine options: 66/80cc 2 stroke: gas/oil premix required, manual clutch - $600 Mounted on Mountain Bike 49cc 4 stroke: straight gas, automatic centrifugal clutch - $820 Mounted on Large frame Mountain Bike/Cruiser All of our bikes come with: -M8 engine mount studs -Slanted head -Upgraded 3 piece centrifugal clutch on 4 strokes -Wide crank arms on 4 strokes -High quality Koyo one way shaft bearing -Japanese 202 main bearings -Upgraded exhaust These bikes are a fun, cheap form of transportation and will last you a lifetime if maintained well. Advantages: - No license or registration of vehicle needed - Low maintenance/running cost - Navigate around the city and through traffic quickly and with ease - Great for food delivery jobs (Uber eats, Door Dash, Grubhub, Deliveroo) Standalone full Kits Available as well! Motorized bicycles require mechanical aptitude to be assembled. If you aren't up to the task, our professional team can install it same day for only $150 All Product/Service Prices: $250 for 2 stroke kit $400 for 4 stroke kit $150 for installation $600 for Prebuilt 2 stroke $820 for Prebuilt 4 stroke We accept cash or etransfer Call or text 647-795-6360. Same day delivery in the GTA for $10 extra."
price = "250"
phoneNumber = "647-795-6360"
driver.get(url)
#15 seconds to login
time.sleep(15)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "emailOrNickname"))
        
    )
    element.send_keys(username) 
except:
    print("goug")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
        
    )
    element.send_keys(password) 
    element.send_keys(Keys.RETURN)
except:
    print("goug")    
#username = driver.find_element_by_class_name("container-227378722 inputBox-3265251147")
#password = driver.find_element_by_id("password")
#username.send_keys("thinkpad220@hotmail.com")
#password.send_keys("windows 95")
#password.send_keys(Keys.RETURN)
time.sleep(6)
title = driver.find_element_by_id("AdTitleForm")
title.send_keys("Motorized Bike Kits")
title.send_keys(Keys.RETURN)
time.sleep(2)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[3]/button'))
        
    )
    element.click()
except:
    driver.quit()
time.sleep(2)
try:
    textbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "pstad-descrptn"))
    )
    textbox.send_keys(itemDescription)
except:
    print("goug")  
try:
    add = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "pstad-tagsInput"))
    )
    for tag in tagList:
        add.send_keys(tag)
        time.sleep(2)
        add.send_keys(Keys.RETURN)
except:
    print("goug")
try:
    images = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "ImageUploadButton"))
    )
    for picture in picturePaths:

        images.click()
        time.sleep(2)
        pyautogui.write(picture,interval=0.25) 
        pyautogui.press('enter')
        time.sleep(2)
except:
    print("goug")
#html5_1fth9l4vlpjj1g0dkvp17mc503
time.sleep(2)
amount = driver.find_element_by_id("PriceAmount")
amount.send_keys(price)
phone = driver.find_element_by_id("PhoneNumber")
phone.send_keys(phoneNumber)
try:
    images = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container-393064055"))
    )
    images.click()
except:
    print("goug")
submit = driver.find_element_by_css_selector('[class = "button-2083332871 button-1997310527 button__primary-1681489609 button__medium-1066667140"]')
submit.click()
#username = driver.find_element_by_class_name("container-227378722 inputBox-3265251147")
#password = driver.find_element_by_id("password")
#username.send_keys("thinkpad220@hotmail.com")
#password.send_keys("windows 95")
#password.send_keys(Keys.RETURN)

#element = driver.find_element_by_class_name("headerButtonPostAd-1524038143")
#element.click()
#search = driver.find_element_by_id("SearchKeyword")
#link = driver.find_element_by_link_text("Sign In")
#time.sleep(10)
#search.send_keys("corolla")
#search.send_keys(Keys.RETURN)
time.sleep(10)
#results  = driver.find_elements_by_class_name("container-results large-images")
#print(results.text)