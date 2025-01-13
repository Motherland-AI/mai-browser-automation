import os, time, unittest
#from selenium.common.exceptions import WebDriverException
from src.mai_browser_automation import WebDriverException, ChromeBrowser

class TestWebBrowser(unittest.TestCase):
    def setUp(self):
        self.driver_file = "C:\\Users\\USER\\Documents\\Tech\\chromedriver-win64\\chromedriver.exe"
        self.browser_file = "C:\\Users\\USER\\Documents\\Tech\\chrome-win64\\chrome.exe"
    
    def test_wrong_driver_path(self):
        with self.assertRaises(FileNotFoundError):
            ChromeBrowser("non_existent_driver_file.exe", self.browser_file)

    def test_wrong_browser_path(self):
        with self.assertRaises(FileNotFoundError):
            ChromeBrowser(self.driver_file, "non_existent_browser_file.exe")

    def test_web_browser_initialization(self):
        try:
            chrome = ChromeBrowser(self.driver_file, self.browser_file)
            time.sleep(5)
            chrome.quit()
            self.assertIsNotNone(chrome)
        except WebDriverException as e:
            self.fail(f"web_browser initialization failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()