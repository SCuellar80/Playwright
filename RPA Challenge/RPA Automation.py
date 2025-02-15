from playwright.sync_api import sync_playwright
from page_excel import ExcelReader

playwright = sync_playwright().start()
chromium = playwright.chromium
browser = chromium.launch(headless=False)
driver = browser.new_page()
driver.goto("https://rpachallenge.com/")

start = driver.locator("button[class*='btn-large']")
start.click()

excel_reader = ExcelReader()
excel_data = excel_reader.read_excel_data()

for row in excel_data:

    labelFirstName = driver.query_selector("//input[@ng-reflect-name='labelFirstName']")
    labelLastName = driver.query_selector("//input[@ng-reflect-name='labelLastName']")
    labelCompanyName = driver.query_selector( "//input[@ng-reflect-name='labelCompanyName']")
    labelRole = driver.query_selector( "//input[@ng-reflect-name='labelRole']")
    labelAddress = driver.query_selector("//input[@ng-reflect-name='labelAddress']")
    labelEmail = driver.query_selector("//input[@ng-reflect-name='labelEmail']")
    labelPhone = driver.query_selector("//input[@ng-reflect-name='labelPhone']")
    buttonSubmit = driver.query_selector( "input[value*='Submit']")

    labelFirstName.fill(row[0])
    labelLastName.fill(row[1])
    labelCompanyName.fill(row[2])
    labelRole.fill(row[3])
    labelAddress.fill(row[4])
    labelEmail.fill(row[5])
    labelPhone.fill(str(row[6]))

    # After all fields completed, submit it
    buttonSubmit.click()

time = driver.locator( "div[class*='message2']")# "div[class*='message2']"
timeText = time.inner_text()
print(timeText)

driver.close()