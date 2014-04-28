'use strict';

angular.module('vinzApp')
  .controller('ServerGroupDetailCtrl', ['$scope', 'serverGroups', '$routeParams', function ($scope, serverGroups, $routeParams) {
    
    var serverGroupId = $routeParams.id;
    $scope.access = {has:true, message: "Revoke"};

    $scope.myServers = serverGroups.getGroupServers(serverGroupId);
  	$scope.caseId = 0;

    // caseId = 0 => servers in group
    // caseId = 1 => servers not in group
    // caseId = 2 => users with access to group
    // caseId = 3 => users without access to group
    // caseId = 4 => usergroups with access to group
    // caseId = 5 => usergroups without access to group
    $scope.shownInTable = function(caseId) {
      $scope.caseId = caseId;

      switch(caseId)
      {
      case 0:
        showGroupServers();
        break;
      case 1:
        showNonGroupServers();
        break;
      case 2:
        showGroupUsers();
        break;
      case 3:
        showNonGroupUser();
        break;
      case 4:
        showGroupUserGroups();
        break;
      case 5:
        showNonGroupUserGroups();
        break;
      }
    }

    $scope.toggleHasAccess = function () {
      //has access
      if ($scope.caseId % 2 == 0) {
        $scope.caseId += 1;
      } else { // doesn't have access
        $scope.caseId -= 1;
      }

      $scope.shownInTable($scope.caseId);
    }

    function showGroupServers() {
      $scope.myServers = serverGroups.getGroupServers(serverGroupId);
    }

    function showNonGroupServers() {
      $scope.myServers = serverGroups.getServerGroup(serverGroupId);
    }

    function showGroupUsers() {

    }

    function showNonGroupUsers() {

    }

    function showGroupUserGroups() {

    }

    function showNonGroupUserGroups() {

    }

  }]);
