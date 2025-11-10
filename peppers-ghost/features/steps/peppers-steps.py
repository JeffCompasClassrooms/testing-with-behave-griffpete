from behave import given, then
from selenium.webdriver.common.by import By

@given('I open the instructables peppers ghost page')
def step_open_peppers_ghost(context):
    context.driver.get('https://www.instructables.com/Peppers-Ghost/')

@then('I expect that there is at least one picture there')
def step_check_pictures(context):
    images = context.driver.find_elements(By.TAG_NAME, 'img')
    assert len(images) > 0, f"Expected at least one image, but found {len(images)}"
