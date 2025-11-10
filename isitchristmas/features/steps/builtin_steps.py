from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I open the url "{url}"')
def step_open_url(context, url):
    context.driver.get(url)

@given('I open the site "{url}"')
def step_open_site(context, url):
    context.driver.get(url)

@then('I expect that element "{selector}" contains the text "{text}"')
def step_element_contains_text(context, selector, text):
    element = context.driver.find_element(By.CSS_SELECTOR, selector)
    assert text.lower() in element.text.lower(), f"Expected '{text}' in element text, but got '{element.text}'"
