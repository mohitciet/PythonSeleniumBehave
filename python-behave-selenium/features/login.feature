Feature: Login

  Scenario: Verify User is able to Login with Valid Credentials
    Given I navigate to the login page
    When I enter the username "test@email.com" and password "abcabc"
    Then I am able to login



