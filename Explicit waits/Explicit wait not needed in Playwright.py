# Playwright does not need "Explicit Wait" in many cases like in this case, but selenium does need it.

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
chromium = playwright.chromium
browser = chromium.launch(headless=False)

driver = browser.new_page()
driver.goto("https://the-internet.herokuapp.com/dynamic_controls")

button = driver.locator('#input-example > button')
button.click()

textBox = driver.locator ('#input-example > input[type=text]') # Playwright detects when an element is ready to interact with!
textBox.fill('Correct Wait')

driver.close()