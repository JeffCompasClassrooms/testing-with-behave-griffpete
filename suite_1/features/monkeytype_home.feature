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

  Scenario: Test all duration options are visible
    Given I am on the Monkeytype homepage
    Then I expect that element ".time" is visible
    And I expect that element "button.textButton[timeconfig='15']" is visible
    And I expect that element "button.textButton[timeconfig='30']" is visible
    And I expect that element "button.textButton[timeconfig='60']" is visible
    And I expect that element "button.textButton[timeconfig='120']" is visible

  Scenario: Login selector exists
    Given I am on the Monkeytype homepage
    Then I expect that element ".view-login" is visible

  Scenario: Settings button is present
    Given I am on the Monkeytype homepage
    Then I expect that element ".view-settings" is visible

  Scenario: Typing area loads
    Given I am on the Monkeytype homepage
    Then I expect that element "#typingtest" is visible
    And I expect that element "#wordsWrapper" is visible
    And I expect that element "#wordsInput" is visible
