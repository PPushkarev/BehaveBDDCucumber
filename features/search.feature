Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product HP into the Search box field
    And I click on Search button
    Then Valid product should fet displayed in Search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to Home page
    When I enter invalid product Honda into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results


  @search
  Scenario: Search without any product
    Given I got navigated to Home page
    When I do not enter anything into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results
