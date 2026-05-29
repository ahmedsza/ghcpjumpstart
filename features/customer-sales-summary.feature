Feature: Customer sales summary reporting
  As a business analyst
  I want to load and review customer sales summary data
  So that I can monitor sales performance

  Background:
    Given I am on the "CUSTOMER SALES SUMMARY" page

  Scenario: Load sales data successfully
    Given sales summary data is available from the backend
    When I click "LOAD DATA"
    Then I should see a sales table with row data
    And pagination controls should be visible

  Scenario: Filter sales rows by customer name
    Given sales summary data contains multiple customer names
    When I enter a customer name filter and load data
    Then only matching customer rows are displayed

  Scenario: Change rows per page setting
    Given sales summary data contains more rows than the default page size
    When I select "25 rows" and load data
    Then the page should display at most 25 rows
    And the paging indicator should reflect the current page

  Scenario: Handle empty result sets
    Given no sales records match the selected filter
    When I load data
    Then I should see "No Sales Data"
    And I should see guidance about filter criteria

  Scenario: Handle backend failure while loading sales data
    Given the sales summary API request fails
    When I load data
    Then an error alert is shown
    And no data rows are displayed
