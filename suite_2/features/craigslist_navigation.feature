Feature: Craigslist Navigation
  As a Craigslist user
  I want to navigate between categories
  So that I can browse different sections

  Scenario: User navigates to furniture category
    Given I am on the Craigslist homepage
    When I navigate to the "furniture" category
    Then I should be on the furniture page
    And the page title should contain "furniture"

  Scenario: User navigates to electronics category
    Given I am on the Craigslist homepage
    When I navigate to the "electronics" category
    Then I should be on the electronics page

  Scenario: User returns to homepage from category
    Given I am on the "furniture" category page
    When I click the Craigslist logo
    Then I should be on the homepage

  Scenario: User navigates to housing category
    Given I am on the Craigslist homepage
    When I navigate to the "housing" section
    Then I should see housing listings

  Scenario: User browses all for sale categories
    Given I am on the Craigslist homepage
    When I view the "for sale" section
    Then I should see multiple sale categories
