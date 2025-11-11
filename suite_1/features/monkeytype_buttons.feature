Feature: MonkeyType Buttons Work
    As a cs student
    I want to be able practice
    So that I can improve my typing skills.

  Scenario: Logo refreshes the page
    Given I am on the Monkeytype homepage
    When I click on the element "#logo"
    Then I expect that the url is "https://monkeytype.com/"

  Scenario: Login button works
    Given I am on the Monkeytype homepage
    When I click on the element ".view-login"
    Then I expect that the url contains "/login"

  Scenario: X link redirects to X
    Given I am on the Monkeytype homepage
    When I click on the element "a.textButton[href='https://x.com/monkeytype']"
    Then I expect that the url is "https://x.com/monkeytype"

  Scenario: GitHub link redirects to GitHub
    Given I am on the Monkeytype homepage
    When I click on the element "a.textButton[href='https://github.com/monkeytypegame/monkeytype']"
    Then I expect that the url is "https://github.com/monkeytypegame/monkeytype"
