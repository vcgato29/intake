Feature:  CfA superuser can manage accounts through the Django Admin
  As a CfA staff who manages the application, I want to be able to securely
  manage user accounts through the Django admin site. 

  Background:
     Given a superuser
       And an org user at "cfa"

  Scenario: Superuser can view existing user accounts in the admin
     Given I log in as the superuser
       And a log listener
       And that "/admin/" loads
      When I open "/admin/auth/user/"
      Then ".results table" should say "cfa_user"
       And ".results table" should say "superuser"
       # And there should be a log that contains "access-audit"
       # And there should be a log that contains "action=read"
       # And there should be a log that contains "resource=User"

  Scenario: Superuser can add permissions to an existing account
     Given I log in as the superuser
       And a log listener
       And that "/admin/" loads
      When I open "/admin/auth/user/"
       And I click the "cfa_user" link
       And I select the "auth | group | Can add group" option for "user_permissions_old"
       And I click the "Save" submit button
      Then ".messagelist li.success" should say "The user \"cfa_user\" was changed successfully."
      # And there should be a log that contains "access-audit"
      # And there should be a log that contains "action=add(UserPermission)"


  Scenario: Superuser can add an existing user to a new group
     Given I log in as the superuser
       And a log listener
       And that "/admin/" loads
      When I open "/admin/auth/user/"
       And I click the "cfa_user" link
       And I select the "performance_monitors" option for "groups_old"
       And I click the "Save" submit button
      Then ".messagelist li.success" should say "The user \"cfa_user\" was changed successfully."
       # And there should be a log that contains "access-audit"
       # And there should be a log that contains "action=add(UserGroup)"

  Scenario: Superuser can change a user to be staff and superuser
     Given I log in as the superuser
       And a log listener
       And that "/admin/" loads
      When I open "/admin/auth/user/"
       And I click the "cfa_user" link
       And I click the "is_staff" checkbox
       And I click the "is_superuser" checkbox
       And I click the "Save" submit button
      Then ".messagelist li.success" should say "The user \"cfa_user\" was changed successfully."
      # And there should be a log that contains "access-audit"
      # And there should be a log that contains "action=change"
      # And there should be a log that contains "resource=User"
      # And there should be a log that contains "changed_fields=is_staff,is_superuser"
