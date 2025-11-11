Feature: MonkeyType Homepage Loads
    As a cs student
    I want to be able practice
    So that I can improve my typing skills.

  Scenario: Homepage Loads
    Given I am on the Monkeytype homepage
    Then I expect that element "#app" is visible

  Scenario: Logo Loads
    Given I am on the Monkeytype homepage
    Then I expect that element "#logo" is visible

  Scenario: Settings page loads
    Given I am on the Monkeytype homepage
    Then I expect that element ".view-settings" is visible

  Scenario: Login selector exists
    Given I am on the Monkeytype homepage
    Then I expect that element ".view-login" is visible

  Scenario: Settings button is present
    Given I am on the Monkeytype homepage
    Then I expect that element ".view-settings" is visible

  Scenario: Typing test loads
    Given I am on the Monkeytype homepage
    Then I expect that element "#startTestButton" is visible
