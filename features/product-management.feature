Feature: Product management
  As an inventory manager
  I want to maintain product records
  So that the catalog stays accurate

  Background:
    Given I am on the "PRODUCT MANAGEMENT" page

  Scenario: View an empty inventory state
    Given there are no products in inventory
    When the product list is loaded
    Then I see the message "No Products Yet"
    And I am prompted to add the first product

  Scenario: Add a new product
    When I create a product with a name, description, price, and category
    Then the product is added to inventory
    And I see a success confirmation

  Scenario: Update an existing product
    Given a product exists in inventory
    When I edit the product details and save
    Then the updated values appear in the inventory table
    And I see a success confirmation

  Scenario: Delete an existing product
    Given a product exists in inventory
    When I confirm deleting that product
    Then the product is removed from inventory
    And I see a success confirmation

  Scenario: Validate required product name
    When I try to save a product without a name
    Then I see the message "Product name is required"
    And the product is not saved

  Scenario Outline: Filter products by keyword and category
    Given the inventory contains multiple products
    When I search for "<keyword>" and choose category "<category>"
    Then only matching products are shown
    Examples:
      | keyword | category    |
      | laptop  | Electronics |
      | mug     | Home & Garden |
      |         | General     |
