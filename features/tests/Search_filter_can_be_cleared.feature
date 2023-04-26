Feature: Search results filter can be cleared

  Scenario: User can see bestseller menu
    Given Open cureskin page
    When Open search results page
    When Click More Filters - Facewash
    When Click on facewash
    When Click on apply
    When Verify filter is "Product type: Face Wash" set
    When Click to "clear all"
    Then Verify filter is removed with '18 results found for “cure”'

