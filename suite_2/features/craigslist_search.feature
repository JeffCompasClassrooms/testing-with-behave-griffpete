Feature: Craigslist Search Functionality
  As a Craigslist user
  I want to search for items
  So that I can find what I need

  Scenario: User searches for items in a category
    Given I am on the Craigslist homepage
    When I navigate to the "furniture" category
    And I search for "desk"
    Then I should see search results
    And the results should contain "desk"
