# Created by admin at 10/11/20
Feature: Log in to user account and purchase a subscription plan

  @fixture.browser.chrome.False
  Scenario: User logs in to account and purchases first subscription plan, paying by card

    Given I'm at the landing page
    When I click on log-in button at the landing page
    Then I should see log-in modal pop up

    When I enter login email and password
    And I click log into my account
    Then I should be at the home page
    And I should be able to get the information about my current session balance

    When I click on pricing tab
    Then I should be redirected to pricing page

    When I click on the first pricing plan
    Then I should see the payment method modal pop up

    When I choose to pay with card
    And I wait for payment method modal to dismiss
    And I relocate to home page
    Then I should see an increase in my session balance
