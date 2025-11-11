from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# GIVEN
@given('I am on the Monkeytype homepage')
def step_open_monkeytype(context):
    context.driver.get("https://monkeytype.com")
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav")))

    try:
        wait = WebDriverWait(context.driver, 10)
        accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal .main .buttons .acceptAll")))
        accept_button.click()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    except:
        pass

    time.sleep(2)

# WHEN
@when('I click on the element "{selector}"')
def step_click_element(context, selector):
    element = context.driver.find_element(By.CSS_SELECTOR, selector)
    element.click()

    # If it opens a new tab, switch to it
    if len(context.driver.window_handles) > 1:
        context.driver.switch_to.window(context.driver.window_handles[-1])

    time.sleep(2)

# THEN
@then('I expect that element "{selector}" contains the text "{text}"')
def step_element_contains_text(context, selector, text):
    element = context.driver.find_element(By.CSS_SELECTOR, selector)
    assert text.lower() in element.text.lower(), f"Expected '{text}' in element text, but got '{element.text}'"

@then('I expect that element "{selector}" is visible')
def step_element_visible(context, selector):
    element = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    assert element.is_displayed(), f"Expected element '{selector}' to be visible, but it was not"

@then('I expect that the url is "{expected_url}"')
def step_check_url(context, expected_url):
    WebDriverWait(context.driver, 10).until(EC.url_to_be(expected_url))
    current_url = context.driver.current_url
    assert current_url == expected_url, f"Expected URL '{expected_url}', but got '{current_url}'"

@then('I expect that the url contains "{expected_part}"')
def step_check_url_contains(context, expected_part):
    WebDriverWait(context.driver, 15).until(EC.url_contains(expected_part))
    current_url = context.driver.current_url
    print(f"\n=== DEBUG ===")
    print(f"Current URL: {current_url}")
    print(f"Looking for: {expected_part}")
    print(f"=============\n")
    assert expected_part in current_url, f"Expected '{expected_part}' in URL, got '{current_url}'"
