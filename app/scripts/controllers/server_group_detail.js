'use strict';

angular.module('vinzApp')
  .controller('ServerGroupDetailCtrl', ['$scope', 'serverGroups', '$routeParams', function ($scope, serverGroups, $routeParams) {
    
    var serverGroupId = $routeParams.id;
  	$scope.serverGroup = serverGroups.getServerGroup(serverGroupId);
    $scope.access = {has:true, message: "Revoke"};

    $scope.tableItems = serverGroups.getGroupServers(serverGroupId);
  	
    // caseId = 0 => servers in group
    // caseId = 1 => servers not in group
    // caseId = 2 => users with access to group
    // caseId = 3 => users without access to group
    // caseId = 4 => usergroups with access to group
    // caseId = 5 => usergroups without access to group
    $scope.shownInTable = function(caseId) {
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
        showNonGroupUsers();
        break;
      case 4:
        showGroupUserGroups();
        break;
      case 5:
        showNonGroupUserGroups();
        break;
      }
    }

    function showGroupServers() {

    }

    function showNonGroupServers() {

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
