'use strict';

angular.module('vinzApp')
  .controller('ServerGroupsCtrl', ['$scope', 'serverGroups', function ($scope, serverGroups) {
    $scope.newServerGroup = {name: ""};
    $scope.myServers = serverGroups.getServerGroups();

    $scope.createServer = function(newServerGroup) {
    	serverGroups.createServerGroup(newServerGroup);
    	$scope.myServers = serverGroups.getServerGroups();
    }
  }]);