Feature: Site navigation
  As a visitor
  I want to move between major sections of the site
  So that I can find information and tools quickly

  Scenario: Navigate from home to product management
    Given I am on the home page
    When I select the "Products" navigation link
    Then the "PRODUCT MANAGEMENT" page is displayed
    And the inventory section is visible

  Scenario: Navigate from home to customer sales summary
    Given I am on the home page
    When I select the "Sales" navigation link
    Then the "CUSTOMER SALES SUMMARY" page is displayed
    And sales controls are visible

  Scenario: Open a coming soon section
    Given I am on the home page
    When I select the "Stores" navigation link
    Then the "STORE FINDER" section is displayed
    And the "COMING SOON" message is visible
