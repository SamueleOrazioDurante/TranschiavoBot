import requests
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

directory = r"/download"
url = "https://we.tl/t-9f4P4Jl00w"


# to download a file/folder from the server
r = requests.get(url) 
url = r.url
print(url)

options = Options()

options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", directory)
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("pdfjs.disabled", True)

options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
options.headless = True

driver = webdriver.Firefox(options=options)

driver.get(url)

button1 = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]')
button1.click()
button1.click()
button1.click()

time.sleep(2)

driver.save_screenshot('screen1.png')

button2 = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[2]/button')
button2.click()

driver.save_screenshot('screen2.png')

time.sleep(2)

button = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div/div[2]/button')
button.click()

driver.close()