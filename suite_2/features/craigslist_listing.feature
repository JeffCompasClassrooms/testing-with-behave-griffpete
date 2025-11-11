Feature: Craigslist Listing Details
  As a Craigslist user
  I want to view listing details
  So that I can learn about items for sale

  Scenario: User views first listing in results
    Given I am on the "furniture" category page
    When I click on the first listing
    Then I should see the listing details page
    And I should see the listing title
    And I should see the price information

  Scenario: User sorts results by newest
    Given I am on the "furniture" category page
    When I sort results by "newest"
    Then results should be sorted by date

  Scenario: User sorts results by price
    Given I am on the "furniture" category page
    When I sort results by "price"
    Then results should be sorted by price

  Scenario: User checks posting date
    Given I am viewing a listing
    Then I should see when the item was posted

  Scenario: User views listing location
    Given I am viewing a listing
    Then I should see the location information

  Scenario: User sees price on listing card
    Given I am on the "furniture" category page
    Then I should see prices displayed

  Scenario: User sees listing images
    Given I am on the "furniture" category page
    Then I should see listing images

  Scenario: User sees multiple listings
    Given I am on the "furniture" category page
    Then I should see at least 10 listings

  Scenario: User can see listing location tags
    Given I am on the "furniture" category page
    Then I should see location information on listings
