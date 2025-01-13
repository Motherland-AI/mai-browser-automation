import unittest
import os
#from selenium.common.exceptions import WebDriverException
from src.mai_browser_automation import WebDriverException, ChromeBrowser

class TestWebBrowser(unittest.TestCase):
    def setUp(self):
        self.driver_path = "C:\\Users\\USER\\Documents\\Tech\\chromedriver-win64\\chromedriver.exe"
        self.browser_path = "C:\\Users\\USER\\Documents\\Tech\\chrome-win64"
    
    """
    def test_wrong_driver_path(self):
        with self.assertRaises(FileNotFoundError):
            ChromeBrowser("wrong_path", self.browser_path)

    def test_wrong_browser_path(self):
        with self.assertRaises(FileNotFoundError):
            ChromeBrowser(self.driver_path, "wrong_browser_path")
    """

    def test_web_browser_initialization(self):
        try:
            chrome = ChromeBrowser(self.driver_path, self.browser_path)
            #chrome = chrome()
            self.assertIsNotNone(chrome)
        except WebDriverException as e:
            self.fail(f"web_browser initialization failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()