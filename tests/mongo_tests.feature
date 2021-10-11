Feature: # Enter feature name here
  # Enter feature description here

  Scenario: edit a profile
    Given there exist a profile
    When I edit the profile
    Then the profile is actually edited