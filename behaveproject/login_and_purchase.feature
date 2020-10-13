# Created by admin at 10/11/20
Feature: Log in to user account and purchase a subscription plan
  @fixture.browser.chrome.False
  Scenario: User logs in to account and purchases first subscription plan, paying by card
    Given I haven't launch the browser

    # open browser and get to the website
    When I launch the browser and get to the website
    And And I click on log-in button at the landing page
    Then I should see log-in modal pop up

    # log in to account, redirect to homepage, and get session balance information
    When I log into my account
    Then I should be at the home page
    And I should be able to get the information about my current session balance

    # redirect to pricing tab
    When I click on pricing tab
    Then I should be redirected to pricing page

    # choose pricing plan
    When I click on the first pricing plan
    Then I should see the payment method modal pop up

    # make payment
    When I choose to pay with card
    Then I should wait for payment successful confirmation
    And I should be redirected to home page
    And I should see an increase in my session balance
