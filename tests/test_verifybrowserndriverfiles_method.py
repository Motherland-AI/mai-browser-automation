import unittest
import os
from src.mai_browser_automation.browser_scripts import verifyBrowserNDriverFiles

class TestVerifyBrowserNDriverFiles(unittest.TestCase):

    def setUp(self):
        # Create temporary directories and files for testing
        self.test_driver_file = "test_driver.exe"
        self.test_browser_file = "test_browser.exe"

        with open(self.test_driver_file, 'w') as f:
            f.write("test driver content")
        with open(self.test_browser_file, 'w') as f:
            f.write("test browser content")

    def tearDown(self):
        # Remove temporary files after testing
        try:
            os.remove(self.test_driver_file)
        except FileNotFoundError:
            pass

        try:
            os.remove(self.test_browser_file)
        except FileNotFoundError:
            pass

    def test_verify_file_paths(self):
        # Test when both driver and browser files exist
        self.assertTrue(verifyBrowserNDriverFiles(self.test_driver_file, self.test_browser_file))

    def test_driver_file_not_exist(self):
        # Test when driver file does not exist
        with self.assertRaises(FileNotFoundError):
            verifyBrowserNDriverFiles("non_existent_driver_file.exe", self.test_browser_file)

    def test_browser_file_not_exist(self):
        # Test when browser file does not exist
        with self.assertRaises(FileNotFoundError):
            verifyBrowserNDriverFiles(self.test_driver_file, "non_existent_browser_file.exe")

if __name__ == '__main__':
    unittest.main()