import unittest
import os
from src.mai_browser_automation.browser_scripts import verifyBrowserNDriverFiles

class TestVerifyBrowserNDriverFiles(unittest.TestCase):

    def setUp(self):
        # Create temporary directories and files for testing
        self.test_driver_path = "test_driver_path"
        self.test_browser_path = "test_browser_path"
        os.makedirs(self.test_driver_path, exist_ok=True)
        os.makedirs(self.test_browser_path, exist_ok=True)
        with open(os.path.join(self.test_driver_path, "chromedriver.exe"), 'w') as f:
            f.write("test driver content")
        with open(os.path.join(self.test_browser_path, "chrome.exe"), 'w') as f:
            f.write("test browser content")

    def tearDown(self):
        # Remove temporary files after testing
        try:
            os.remove(os.path.join(self.test_driver_path, "chromedriver.exe"))
        except FileNotFoundError:
            pass

        try:
            os.remove(os.path.join(self.test_browser_path, "chrome.exe"))
        except FileNotFoundError:
            pass

        # Remove temporary directories after testing
        os.rmdir(self.test_driver_path)
        os.rmdir(self.test_browser_path)

    def test_verify_paths_exist(self):
        # Test when both driver and browser paths exist
        self.assertTrue(verifyBrowserNDriverFiles(self.test_driver_path, self.test_browser_path))

    def test_driver_path_not_exist(self):
        # Test when driver path does not exist
        with self.assertRaises(FileNotFoundError):
            verifyBrowserNDriverFiles("non_existent_driver_path", self.test_browser_path)

    def test_driver_file_not_exist(self):
        # Test when driver file does not exist
        os.remove(os.path.join(self.test_driver_path, "chromedriver.exe"))
        with self.assertRaises(FileNotFoundError):
            verifyBrowserNDriverFiles(self.test_driver_path, self.test_browser_path)

    def test_browser_path_not_exist(self):
        # Test when browser path does not exist
        with self.assertRaises(FileNotFoundError):
            verifyBrowserNDriverFiles(self.test_driver_path, "non_existent_browser_path")

    def test_browser_file_not_exist(self):
        # Test when browser file does not exist
        os.remove(os.path.join(self.test_browser_path, "chrome.exe"))
        with self.assertRaises(FileNotFoundError):
            verifyBrowserNDriverFiles(self.test_driver_path, self.test_browser_path)

if __name__ == '__main__':
    unittest.main()