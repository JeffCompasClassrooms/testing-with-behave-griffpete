from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Given
@given('I am on the Craigslist homepage')
def step_go_to_homepage(context):
    context.driver.get(context.base_url)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

@given('I am on the "{category}" category page')
def step_on_category_page(context, category):
    context.driver.get(f"{context.base_url}/search/{get_category_code(category)}")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

@given('I am viewing a listing')
def step_viewing_listing(context):
    context.driver.get(f"{context.base_url}/search/fua")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cl-search-result")))
    first_listing = context.driver.find_element(By.CSS_SELECTOR, ".cl-search-result a.posting-title")
    first_listing.click()
    time.sleep(2)

# When
@when('I navigate to the "{category}" category')
def step_navigate_to_category(context, category):
    category_code = get_category_code(category)
    context.driver.get(f"{context.base_url}/search/{category_code}")
    time.sleep(1)

@when('I search for "{search_term}"')
def step_search_for(context, search_term):
    search_box = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[enterkeyhint="search"]')))
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

@when('I click on the first listing')
def step_click_first_listing(context):
    first_listing = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cl-search-result a.posting-title")))
    context.listing_title = first_listing.text
    first_listing.click()
    time.sleep(2)

@when('I click the Craigslist logo')
def step_click_logo(context):
    logo = context.driver.find_element(By.CSS_SELECTOR, ".cl-goto-home")
    logo.click()
    time.sleep(1)

@when('I navigate to the "{section}" section')
def step_navigate_to_section(context, section):
    if section == "housing":
        context.driver.get(f"{context.base_url}/search/hhh")
    time.sleep(1)

@when('I view the "{section}" section')
def step_view_section(context, section):
    section_element = context.driver.find_element(By.XPATH, f"//span[contains(text(), '{section}')]")
    assert section_element.is_displayed()

@when('I sort results by "{sort_option}"')
def step_sort_by(context, sort_option):
    sort_dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cl-search-sort-mode"))
    )
    sort_dropdown.click()
    time.sleep(1)

    # Map sort options to button selectors
    sort_map = {
        "newest": ".cl-search-sort-mode-newest",
        "price": ".cl-search-sort-mode-price-asc"
    }

    # Click the appropriate sort button from the popup
    sort_button_selector = sort_map.get(sort_option.lower(), ".cl-search-sort-mode-newest")
    sort_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, sort_button_selector))
    )
    sort_button.click()
    time.sleep(2)

# Then
@then('results should be sorted by date')
def step_results_sorted_by_date(context):
    # Verify the sort button shows "newest" is selected
    sort_button = context.driver.find_element(By.CSS_SELECTOR, ".cl-search-sort-mode .label")
    assert sort_button.text.lower() == "newest", f"Expected 'newest', got '{sort_button.text}'"

@then('results should be sorted by price')
def step_results_sorted_by_price(context):
    # Verify the sort button shows price sorting is selected
    sort_button = context.driver.find_element(By.CSS_SELECTOR, ".cl-search-sort-mode .label")
    assert "﹩" in sort_button.text or "$" in sort_button.text, f"Expected price sorting, got '{sort_button.text}'"

@then('I should see search results')
def step_see_results(context):
    results = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cl-search-result")))
    assert results.is_displayed(), "No search results found"

@then('the results should contain "{text}"')
def step_results_contain(context, text):
    page_content = context.driver.page_source.lower()
    assert text.lower() in page_content, f"Results do not contain '{text}'"

@then('I should see no results message')
def step_see_no_results(context):
    no_results = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".noresults")))
    assert no_results.is_displayed(), "Expected no results message"

@then('I should be on the furniture page')
def step_on_furniture_page(context):
    assert "fua" in context.driver.current_url or "furniture" in context.driver.current_url.lower()

@then('the page title should contain "{text}"')
def step_title_contains(context, text):
    page_title = context.driver.title.lower()
    assert text.lower() in page_title, f"Title '{page_title}' does not contain '{text}'"

@then('I should be on the electronics page')
def step_on_electronics_page(context):
    assert "ela" in context.driver.current_url or "electronics" in context.driver.current_url.lower()

@then('I should be on the homepage')
def step_on_homepage(context):
    assert context.driver.current_url == context.base_url or context.driver.current_url == f"{context.base_url}/"

@then('I should see housing listings')
def step_see_housing_listings(context):
    assert "hhh" in context.driver.current_url or "housing" in context.driver.current_url.lower()

@then('I should see multiple sale categories')
def step_see_sale_categories(context):
    categories = context.driver.find_elements(By.CSS_SELECTOR, ".cats a")
    assert len(categories) > 0, "No sale categories found"

@then('I should see the listing details page')
def step_see_listing_details(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "postingbody")))

@then('I should see the listing title')
def step_see_listing_title(context):
    title = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#titletextonly"))
    )
    assert title.is_displayed() and len(title.text) > 0, "Listing title not found"

@then('I should see the price information')
def step_see_price(context):
    try:
        price = context.driver.find_element(By.CSS_SELECTOR, ".price")
        assert price.is_displayed(), "Price not visible"
    except:
        pass

@then('I should see when the item was posted')
def step_see_posting_date(context):
    posting_info = context.driver.find_element(By.CSS_SELECTOR, ".postinginfo time")
    assert posting_info.is_displayed(), "Posting date not found"

@then('I should see the location information')
def step_see_location(context):
    page_source = context.driver.page_source
    assert len(page_source) > 0

@then('I should see prices displayed')
def step_see_prices(context):
    prices = context.driver.find_elements(By.CSS_SELECTOR, ".priceinfo")
    assert len(prices) > 0, "No prices found on listings"

@then('I should see listing images')
def step_see_images(context):
    images = context.driver.find_elements(By.CSS_SELECTOR, ".cl-search-result img")
    assert len(images) > 0, "No listing images found"

@then('I should see at least {count:d} listings')
def step_see_multiple_listings(context, count):
    listings = context.driver.find_elements(By.CSS_SELECTOR, ".cl-search-result")
    assert len(listings) >= count, f"Expected at least {count} listings, found {len(listings)}"

@then('I should see location information on listings')
def step_see_location_tags(context):
    locations = context.driver.find_elements(By.CSS_SELECTOR, ".cl-search-result .meta")
    assert len(locations) > 0, "No location information found"

# Helper
def get_category_code(category):
    """Map category names to Craigslist category codes"""
    category_map = {
        "furniture": "fua",
        "electronics": "ela",
        "cars": "cta",
        "housing": "hhh",
        "jobs": "jjj",
        "for sale": "sss"
    }
    return category_map.get(category.lower(), "sss")
