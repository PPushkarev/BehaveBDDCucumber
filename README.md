# Sample Python Selenium Cucumber Framework
# for web site https://tutorialsninja.com/demo/
## There are 3 Test cases class when we test functional working of website in terms of  search of product,  login,  and register user 

A scenario is an example of an interaction a user would have as part of the feature. It is comprised of a series of steps. Each step has to start with a keyword: Given, When, Then, But or And. Here's an example  



The tech stack used in this project are:

    Python as the programming language for writing test code
    Cucumber as the framework
    PIP3 as the build tool
    VSCode as the preferred IDE for writing python code.

Running tests
Type in Terminal this command:

    behave features 
        

Report
Type in Terminal this command:

    allure serve Report

To create new allure Report 
Use this commnand:

    behave -f allure_behave.formatter:AllureFormatter -o Report 



## Scenarios

  ```
@login
  Scenario: Login with invalid Email and valid password
    Given Login page
    When I enter invalid email peternsk@in88box.ru and valid password 12345678 into fields
    And I click on Login button
    Then I get not  logged and get proper message
  ```


## Scenario Outlines


```Feature: Login Functionality
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
  ```



         

