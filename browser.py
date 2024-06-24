from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

def getOptions(DOWNLOAD_DIRECTORY):
    options = Options()

    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", DOWNLOAD_DIRECTORY)
    options.set_preference("browser.download.useDownloadDir", True)
    options.set_preference("pdfjs.disabled", True)

    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    options.headless = True

    return options

def WTDownload(url,DOWNLOAD_DIRECTORY):

    options = getOptions(DOWNLOAD_DIRECTORY)

    driver = webdriver.Firefox(options=options)

    driver.get(url)

    button1 = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]') #FIRST COOKIE ACCEPT BUTTON
    button1.click()
    button1.click()
    button1.click()

    time.sleep(2)

    button2 = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[2]/button') # SECOND POLICY ACCEPT BUTTON
    button2.click()

    time.sleep(2)

    button = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div/div[2]/button') # DOWNLOAD BUTTON
    button.click()

    driver.close()