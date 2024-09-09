Feature: Login Functionality

  @login
  Scenario Outline: Login with valid credentials
    Given Login page
    When I enter valid email as <email> and valid password as <password> into fields
    And I click on Login button
    Then I get logged
    Examples:
    |email|             |password|
    |peternsk@inbox.ru| |12345678|
    |2136823@gmail.com| |12345678|
    |2136823@gmail.com| |123456789|

  @login
  Scenario: Login with invalid Email and valid password
    Given Login page
    When I enter invalid email peternsk@in88box.ru and valid password 12345678 into fields
    And I click on Login button
    Then I get not  logged and get proper message

 @login
 Scenario: Login with valid Email and invalid password
    Given Login page
    When I enter valid email peternsk@in88box.ru and invalid password 1234565655678 into fields
    And I click on Login button
    Then I get not  logged and get proper message

  @login
  Scenario: Login with invalid Email and invalid password
    Given Login page
    When I enter invalid email peter888nsk@inbox.ru and invalid password 1234565655678 into fields
    And I click on Login button
    Then I get not  logged and get proper message

  @login
  Scenario: Login without  Email and  password
    Given Login page
    When I do not enter email and  password into fields
    And I click on Login button
    Then I get not  logged and get proper message

