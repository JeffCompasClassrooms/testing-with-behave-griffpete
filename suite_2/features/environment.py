from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.set_page_load_timeout(60)
    context.driver.implicitly_wait(10)

    context.base_url = "https://sfbay.craigslist.org"

def after_all(context):
    try:
        context.driver.quit()
    except Exception as e:
        print("Error closing driver:", e)
