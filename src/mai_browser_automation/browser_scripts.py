import os

chrome_driver_path = "" #predefined driver path
chrome_browser_path = "" #predefined browser path

driver_file = "chromedriver.exe"
browser_file = "chrome.exe"


#This code will be called upon initializing a web_browser @*_browser.py
#This is to ensure we have the correct browser and driver paths
#And to ensure we can find the files there as well
def verifyBrowserNDriverFiles(driver_path, browser_path):
    driver_file_path = os.path.join(driver_path, "chromedriver.exe")
    browser_file_path = os.path.join(browser_path, "chrome.exe")

    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"Driver path does not exist: {driver_path}")
    if not os.path.isfile(driver_file_path):
        raise FileNotFoundError(f"Driver file {driver_file} does not exist at path: {driver_path}")
    if not os.path.exists(browser_path):
        raise FileNotFoundError(f"Browser path does not exist: {browser_path}")
    if not os.path.isfile(browser_file_path):
        raise FileNotFoundError(f"Browser file {browser_file} does not exist at path: {browser_path}")
    
    #print("Both driver and browser files exist.")
    return True

#I am not sure of the function of the code below so am commenting it out
"""
__all__ = [
    "chrome_browser",
    "chrome_driver"
]
"""