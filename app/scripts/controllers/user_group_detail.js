'use strict';

angular.module('vinzApp')
  .controller('UserGroupDetailCtrl', ['$scope', 'userGroups', '$routeParams', function ($scope, userGroups, $routeParams) {
    
    var userGroupId = $routeParams.id;
    $scope.userGroup = userGroups.getUserGroup(userGroupId);

    $scope.access = {has:true, message: "Revoke"};
    $scope.maintain = {title: "Servers", inGroupYesLabel: "In Group", inGroupNoLabel: "Not In Group"};
    $scope.action = {buttonClass: "danger", message: "Remove"};
    $scope.inGroupYes = true;

    // caseId = 0 => users in group
    // caseId = 1 => users not in group
    // caseId = 2 => servers with access to group
    // caseId = 3 => servers without access to group
    // caseId = 4 => servergroups with access to group
    // caseId = 5 => servergroups without access to group
    $scope.shownInTable = function(caseId) {
      if (!$scope.inGroupYes && caseId % 2 == 0) {
        caseId++;
      }

      $scope.caseId = caseId;

      if ($scope.inGroupYes) {
        $scope.action.buttonClass = "danger";
      } else {
        $scope.action.buttonClass = "success";
      }

      if (caseId == 0 || caseId == 1) {
        $scope.maintain.title = "Servers";
        $scope.maintain.inGroupNoLabel = "Not In Group";
        $scope.maintain.inGroupYesLabel = "In Group";
      } else if (caseId == 2 || caseId == 3) {
        $scope.maintain.title = "Users";
        $scope.maintain.inGroupNoLabel = "No Access";
        $scope.maintain.inGroupYesLabel = "Has Access";
      } else {
        $scope.maintain.title = "User Groups";
        $scope.maintain.inGroupNoLabel = "No Access";
        $scope.maintain.inGroupYesLabel = "Has Access";
      }

      switch(caseId)
      {
      case 0:
        $scope.myUsers = userGroups.getGroupUsers(userGroupId);
        $scope.action.message = "Remove";
        break;
      case 1:
        $scope.myUsers = userGroups.getNonGroupUsers(userGroupId);
        $scope.action.message = "Add";
        break;
      case 2:
        $scope.myServers = userGroups.getUserGroupServers(userGroupId);
        $scope.action.message = "Revoke";
        break;
      case 3:
        $scope.myServers = userGroups.getNonUserGroupServers(userGroupId);
        $scope.action.message = "Grant";
        break;
      case 4:
        $scope.myServerGroups = userGroups.getUserGroupServerGroups(userGroupId);
        $scope.action.message = "Revoke";
        break;
      case 5:
        $scope.myServerGroups = userGroups.getNonUserGroupServerGroups(userGroupId);
        $scope.action.message = "Grant";
        break;
      }
    }

    $scope.shownInTable(0);

    $scope.toggleInGroup = function () {
      //has access
      if ($scope.inGroupYes) {
        $scope.caseId += 1;
      } else { // doesn't have access
        $scope.caseId -= 1;
      }

      $scope.inGroupYes = !$scope.inGroupYes;

      $scope.shownInTable($scope.caseId);
    }

    $scope.switchSides = function(id) {
      switch($scope.caseId)
      {
      case 0:
        removeFromArray($scope.myUsers, id, 'id');
        userGroups.removeUserFromGroup(userGroupId, id);
        break;
      case 1:
        removeFromArray($scope.myUsers, id, 'id');
        userGroups.addUserToGroup(userGroupId, id);
        break;
      case 2:
        removeFromArray($scope.myServers, id, 'id');
        userGroups.revokeServerAccessToGroup(userGroupId, id);
        break;
      case 3:
        removeFromArray($scope.myServers, id, 'id');
        userGroups.grantServerAccessToGroup(userGroupId, id);
        break;
      case 4:
        removeFromArray($scope.myServerGroups, id, 'id');
        userGroups.revokeServerGroupAccessToGroup(userGroupId, id);
        break;
      case 5:
        removeFromArray($scope.myServerGroups, id, 'id');
        userGroups.grantServerGroupAccessToGroup(userGroupId, id);
        break;
      }
    }

    function removeFromArray(myArray, searchTerm, property) {
        for(var i = 0, len = myArray.length; i < len; i++) {
            if (myArray[i][property] === searchTerm) {
              myArray.splice(i, 1);
              return true;
            }
        }
        return false;
    }

  }]);
