from selenium import webdriver
from selenium.webdriver.support.select import Select
from PIL import ImageGrab
from email_script import *
import time

# chrome initiation to grab URL
driver = webdriver.Chrome('/Users/Chris/Documents/web_driver/chromedriver')
driver.get('https://covid19.nychealthandhospitals.org/PointOfEntry')
driver.maximize_window()

#credentials
email = driver.find_element_by_id('CorpUserId')
pwd = driver.find_element_by_id('Password')
button = driver.find_element_by_xpath('//*[@id="LoginCtrlID"]/div[3]/div/div/div/div[2]/form/div[3]/div/input')

#filling out forms
email.send_keys('login')
pwd.send_keys('password')
button.click()
time.sleep(3)

#populating the required fields; location, and 3 exposure questions
select = Select(driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/div/div[5]/div[1]/div/select'))
select.select_by_value('17')
driver.find_element_by_xpath('//*[@id="InventoryTrackerCtrlID"]/div/div[1]/form/div[3]/div/div[6]/label[1]').click()
driver.find_element_by_xpath('//*[@id="InventoryTrackerCtrlID"]/div/div[1]/form/div[3]/div/div[1]/label[1]').click()
driver.find_element_by_xpath('//*[@id="InventoryTrackerCtrlID"]/div/div[1]/form/div[3]/div/div[8]/label').click()
driver.find_element_by_xpath('//*[@id="InventoryTrackerCtrlID"]/div/div[1]/form/div[5]/div[2]/div/button').click()

#sleep in case of long loads, screenshot saved to local directory
time.sleep(3)
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
screenshot.close()

#email. might work on this at some point.
#with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #server.login(sender_email, password)
    #server.sendmail(sender_email, receiver_email, text)


driver.close()
