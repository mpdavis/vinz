'use strict';

angular.module('vinzApp')
  .controller('ServerGroupsCtrl', ['$scope', 'serverGroups', '$location', '$timeout', function ($scope, serverGroups, $location, $timeout) {
    $scope.newServerGroup = {name: ""};
    $scope.myServers = serverGroups.getServerGroups();
    $scope.finish = false;

    $scope.createServer = function(newServerGroup) {
    	serverGroups.createServerGroup(newServerGroup);
    	$scope.myServers = serverGroups.getServerGroups();
    }

    $scope.detail = function(name) {
    	$scope.finish = true;
    	$timeout(function() {
    		$location.path( '/server_groups/' + name );
    	}, 500);
    }
  }]);