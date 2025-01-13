import os
import src.mai_browser_automation.browser_scripts as browser_scripts
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#to use the web_browser, browser and driver paths has to be specified
def web_browser(driver_file, chrome_file, url="https://www.google.com", chrome_options=[]):
    #we want to be sure the path received are correct before passing them down into our code
    #otherwise verifyBrowserNDriverFiles will throw an error
    #browser_scripts.verifyBrowserNDriverFiles(driver_file, chrome_file)

    options = Options() #instantiate Chrome Options
    service = Service(executable_path=driver_file) #instantiate Chrome Service         

    #this option ensures that we specify our own chrome browser
    #not the one installed natively on the windows
    options.binary_location = chrome_file

    #loop through browser arguments and add to options
    for arg in chrome_options:
        options.add_argument(arg)

    browser = Chrome(service=service, options=options)
    browser.get(url)
    return browser
