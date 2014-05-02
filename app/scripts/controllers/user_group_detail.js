'use strict';

angular.module('vinzApp')
  .controller('UserGroupDetailCtrl', ['$scope', 'userGroups', '$routeParams', function ($scope, userGroups, $routeParams) {
    
    var userGroupId = $routeParams.id;
    $scope.userGroup = userGroups.getUserGroup(userGroupId);

    $scope.access = {has:true, message: "Revoke"};
    $scope.maintain = {title: "Users", inGroupYesLabel: "In Group", inGroupNoLabel: "Not In Group"};
    $scope.action = {buttonClass: "danger", message: "Remove"};
    $scope.inGroupYes = true;

    // caseId = 0 => users in group
    // caseId = 1 => users not in group
    $scope.shownInTable = function(caseId) {

      $scope.caseId = caseId;

      if ($scope.inGroupYes) {
        $scope.action.buttonClass = "danger";
      } else {
        $scope.action.buttonClass = "success";
      }

      if (caseId == 0 || caseId == 1) {
        $scope.maintain.title = "Users";
        $scope.maintain.inGroupNoLabel = "Not In Group";
        $scope.maintain.inGroupYesLabel = "In Group";
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
