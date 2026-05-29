Feature: Product catalog administration
  As a backoffice administrator
  I want to manage products in the catalog
  So that inventory data stays accurate

  Background:
    Given I am on the "PRODUCT MANAGEMENT" page

  Scenario: View an empty inventory state
    Given no products exist in the catalog
    When the inventory is loaded
    Then I should see "No Products Yet"
    And I should be prompted to add the first product

  Scenario: Add a product with required and optional fields
    When I create a product with name, description, price, and category
    Then the product appears in the inventory table
    And a success alert is shown

  Scenario: Validation prevents creating a product without a name
    When I submit the product form without a product name
    Then I should see "Product name is required"
    And the product is not created

  Scenario: Edit an existing product
    Given an existing product is listed in inventory
    When I update its details from the edit action
    Then the inventory shows the updated values
    And a success alert is shown

  Scenario: Delete an existing product
    Given an existing product is listed in inventory
    When I confirm product deletion
    Then the product is removed from inventory
    And a success alert is shown

  Scenario Outline: Filter inventory by text and category
    Given products exist in multiple categories
    When I search for "<search term>" and select category "<category>"
    Then only matching products are shown
    Examples:
      | search term | category    |
      | headset     | Electronics |
      | hoodie      | Clothing    |
      |             | General     |
