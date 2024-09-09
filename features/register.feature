Feature: Register Account

  @register
  Scenario: Register with all fields
    Given I navigate to RegisterPage
    When I fill all fields
     |name|last_name|phone|password|
     |'Aron'|'Nelson'|'5449035'|'123456'|
    And I click Continue button
    Then Account Should be created


  @register
  Scenario: Register with duplicate email adress
    Given I navigate to RegisterPage
    When I fill all fields and enter duplicate email
    |name|last_name|phone|password|
     |'Aron'|'Nelson'|'5449035'|'123456'|
    And I click Continue button
    Then 1Proper massage should be displayed


  @register
  Scenario: Register with without any details
    Given I navigate to RegisterPage
    When I do not fill any fields
    And I click Continue button
    Then 2Proper massage should be displayed about empty fields
