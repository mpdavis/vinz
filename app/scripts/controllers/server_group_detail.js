'use strict';

angular.module('vinzApp')
  .controller('ServerGroupDetailCtrl', ['$scope', 'serverGroups', '$routeParams', function ($scope, serverGroups, $routeParams) {
    
    var serverGroupId = $routeParams.id;
    $scope.serverGroup = serverGroups.getServerGroup(serverGroupId);

    $scope.access = {has:true, message: "Revoke"};
    $scope.maintain = {title: "Servers", inGroupYesLabel: "In Group", inGroupNoLabel: "Not In Group"};
    $scope.action = {buttonClass: "danger", message: "Remove"};
    $scope.inGroupYes = true;

    // caseId = 0 => servers in group
    // caseId = 1 => servers not in group
    // caseId = 2 => users with access to group
    // caseId = 3 => users without access to group
    // caseId = 4 => usergroups with access to group
    // caseId = 5 => usergroups without access to group
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
        $scope.myServers = serverGroups.getGroupServers(serverGroupId);
        $scope.action.message = "Remove";
        break;
      case 1:
        $scope.myServers = serverGroups.getNonGroupServers(serverGroupId);
        $scope.action.message = "Add";
        break;
      case 2:
        $scope.myUsers = serverGroups.getServerGroupUsers(serverGroupId);
        $scope.action.message = "Revoke";
        break;
      case 3:
        $scope.myUsers = serverGroups.getNonServerGroupUsers(serverGroupId);
        $scope.action.message = "Grant";
        break;
      case 4:
        $scope.myUserGroups = serverGroups.getServerGroupUserGroups(serverGroupId);
        $scope.action.message = "Revoke";
        break;
      case 5:
        $scope.myUserGroups = serverGroups.getNonServerGroupUserGroups(serverGroupId);
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
        removeFromArray($scope.myServers, id, 'id');
        serverGroups.removeServerFromGroup(serverGroupId, id);
        break;
      case 1:
        removeFromArray($scope.myServers, id, 'id');
        serverGroups.addServerToGroup(serverGroupId, id);
        break;
      case 2:
        removeFromArray($scope.myUsers, id, 'id');
        serverGroups.revokeUserAccessToGroup(serverGroupId, id);
        break;
      case 3:
        removeFromArray($scope.myUsers, id, 'id');
        serverGroups.grantUserAccessToGroup(serverGroupId, id);
        break;
      case 4:
        removeFromArray($scope.myUserGroups, id, 'id');
        serverGroups.revokeUserGroupAccessToGroup(serverGroupId, id);
        break;
      case 5:
        removeFromArray($scope.myUserGroups, id, 'id');
        serverGroups.grantUserGroupAccessToGroup(serverGroupId, id);
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
