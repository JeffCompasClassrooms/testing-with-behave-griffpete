from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import os

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

def before_scenario(context, scenario):
    try:
        _ = context.driver.current_url
    except WebDriverException:
        print("WebDriver was lost — restarting Chrome for scenario:", scenario.name)
        before_all(context)

def after_scenario(context, scenario):
    handles = context.driver.window_handles
    if len(handles) > 1:
        main = handles[0]
        for h in handles[1:]:
            context.driver.switch_to.window(h)
            context.driver.close()
        context.driver.switch_to.window(main)

def after_all(context):
    try:
        context.driver.quit()
    except Exception as e:
        print("Error closing driver:", e)
