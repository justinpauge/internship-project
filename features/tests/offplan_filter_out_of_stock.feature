Feature: Off-plan inventory filtering

  Scenario: User can filter by Out of Stock
    Given the user opens the main page
    And the user logs in
    When the user clicks "Off-plan" in the left side menu
    Then the Off-plan page should open
    When the user filters sale status by "Out of Stock"
    Then every product should contain "Out of Stock"
