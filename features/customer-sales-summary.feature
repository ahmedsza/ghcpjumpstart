Feature: Customer sales summary
  As a sales analyst
  I want to view customer sales records
  So that I can review account performance

  Background:
    Given I am on the "CUSTOMER SALES SUMMARY" page

  Scenario: Load customer sales data
    When I request sales data
    Then I see a sales summary table
    And pagination details are displayed

  Scenario: Filter sales by customer name
    Given sales data is available
    When I filter results by a customer name
    Then only matching records are shown

  Scenario Outline: Change sales page size
    Given sales data is available
    When I select "<rows>" rows per page and load data
    Then the table is refreshed with up to "<rows>" rows
    Examples:
      | rows |
      | 25   |
      | 100  |
      | 500  |

  Scenario: Handle no matching sales data
    Given sales data is available
    When I filter by a customer name with no matches
    Then I see the message "No Sales Data"
    And I see guidance that no records matched the filter

  Scenario: Show an error when sales data cannot be loaded
    When the sales service returns an error
    Then I see an error alert
    And the sales table is not displayed
