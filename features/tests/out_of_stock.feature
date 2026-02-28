Feature: User can filter by Out of Stock

  Scenario: User filters properties by Out of Stock status

    Given User opens the login page
    When User logs in
    And User clicks on Off-plan in sidebar
    And User filters by Out of Stock
    Then All products should have Out of Stock status
