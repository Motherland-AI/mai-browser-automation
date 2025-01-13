import os

#This code will be called upon initializing a web_browser @*_browser.py
#This is to ensure we have the correct paths to the browser and driver files
def verifyBrowserNDriverFiles(driver_file, browser_file):
    #*This script can be expanded to check if the file is an executable file
    #*And to compare the size of the file to a reasonable size (i.e expected to be greater than a specific size)
    #*However checking for executable file more require more code for cross platform compatibility 

    if not os.path.isfile(driver_file):
        raise FileNotFoundError(f"Driver file cannot be found at: {driver_file}")
    if not os.path.isfile(browser_file):
        raise FileNotFoundError(f"Browser file cannot be found at: {driver_file}")

    return True