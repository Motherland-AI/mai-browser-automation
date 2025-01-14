## mai-browser-automation

mai-browser-automation is a motherland ai package for browser automation activities

Browser automation can be rigorous and may require several techniques depending on the automation needs

We aim to keep updating this package to cover our automation needs

For now, mai-browser-automation can automate a Chrome browser using the Selenium WebDriver

## Installation

First, we need a Chrome WebDriver and a Chrome browser.
Download the compatible WebDriver and browser.
Find installation steps here: [ChromeDriver Downloads](https://developer.chrome.com/docs/chromedriver/downloads). Carefully follow the installation instructions.

This package was written and tested in a Windows environment but should be compatible with other platforms.

After installing the compatible ChromeDriver and Chrome browser:

Install mai_browser_automation by following the instructions:
1. `git clone https://github.com/Motherland-AI/mai-browser-automation.git`
2. `pip install -r requirements.txt`

The package requires `python3.10.*` and `selenium==4.27.1`.

## Usage

```python
from mai_browser_automation.src.mai_browser_automation import WebDriverException, ChromeBrowser

try:
    chrome = ChromeBrowser(path_to_driver, path_to_browser)
    time.sleep(5)
    chrome.quit()
except WebDriverException as e:
    print(e)
```

This package mandates you provide the path to the Chrome browser,
if you want to automate the default Chrome browser installed on your platform.

Ensure to install the appropriate ChromeDriver for your default Chrome browser, then provide the path to the browser.

Future updates to mai-browser-automation may make the path to the browser optional and would use the default if no path was given, just as Selenium does by default.

See Selenium documentation on how to automate the browser further, then call such methods on `chrome`.

Enjoy your automation!