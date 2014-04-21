'use strict';

angular.module('vinzApp')
  .controller('ServerGroupsCtrl', ['$scope', 'serverGroups', '$location', '$timeout', function ($scope, serverGroups, $location, $timeout) {
    $scope.newServerGroup = {name: ""};
    $scope.myServers = serverGroups.getServerGroups();

    $scope.createServer = function(newServerGroup) {
    	serverGroups.createServerGroup(newServerGroup);
    	$scope.myServers = serverGroups.getServerGroups();
    }

    $scope.detail = function(name) {
    	$location.path( '/server_groups/' + name );
    }
  }]);