Feature: Backoffice navigation
  As an operations administrator
  I want to move between dashboard sections
  So that I can access each management area quickly

  Background:
    Given the ZAVA backoffice dashboard is open

  Scenario: Open the product management page from primary navigation
    When I select "PRODUCTS" from the top navigation
    Then the "PRODUCT MANAGEMENT" page is displayed
    And I can see the "INVENTORY" section

  Scenario: Open customer sales summary from primary navigation
    When I select "SALES" from the top navigation
    Then the "CUSTOMER SALES SUMMARY" page is displayed
    And the "LOAD DATA" action is available

  Scenario: View coming soon content pages
    When I navigate to "STORES"
    Then I should see "COMING SOON"
    When I navigate to "CONTACT"
    Then I should see "COMING SOON"

  Scenario: Navigate using mobile menu
    Given the mobile navigation menu is opened
    When I select "ABOUT"
    Then the "ABOUT ZAVA" page is displayed
