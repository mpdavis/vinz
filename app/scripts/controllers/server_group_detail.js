'use strict';

angular.module('vinzApp')
  .controller('ServerGroupDetailCtrl', ['$scope', 'serverGroups', '$routeParams', function ($scope, serverGroups, $routeParams) {
    
    var serverGroupId = $routeParams.id;
    $scope.serverGroup = serverGroups.getServerGroup(serverGroupId);

    $scope.access = {has:true, message: "Revoke"};
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
        console.log("not in group toggled");
      }

      console.log(caseId);

      $scope.caseId = caseId;

      if (caseId % 2 == 0) {
        $scope.action.buttonClass = "danger";
      } else {
        $scope.action.buttonClass = "success";
      }

      switch(caseId)
      {
      case 0:
        showGroupServers();
        $scope.action.message = "Remove";
        break;
      case 1:
        showNonGroupServers();
        $scope.action.message = "Add";
        break;
      case 2:
        showGroupUsers();
        $scope.action.message = "Revoke";
        break;
      case 3:
        showNonGroupUser();
        $scope.action.message = "Grant";
        break;
      case 4:
        showGroupUserGroups();
        $scope.action.message = "Revoke";
        break;
      case 5:
        showNonGroupUserGroups();
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
        serverGroups.grantUserGroupAccessToGroup(serverGroupId, id);
        break;
      case 5:
        removeFromArray($scope.myUserGroups, id, 'id');
        serverGroups.grantUserGroupAccessToGroup(serverGroupId, id);
        break;
      }
    }    

    function showGroupServers() {
      $scope.myServers = serverGroups.getGroupServers(serverGroupId);
    }

    function showNonGroupServers() {
      $scope.myServers = serverGroups.getNonGroupServers(serverGroupId);
    }

    function showGroupUsers() {
      $scope.myUsers = serverGroups.getServerGroupUsers(serverGroupId);
    }

    function showNonGroupUser() {
      $scope.myUsers = serverGroups.getNonServerGroupUsers(serverGroupId);
    }

    function showGroupUserGroups() {
      $scope.myUserGroups = serverGroups.getServerGroupUserGroups(serverGroupId);
    }

    function showNonGroupUserGroups() {
      $scope.myUserGroups = serverGroups.getNonServerGroupUserGroups(serverGroupId);
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
