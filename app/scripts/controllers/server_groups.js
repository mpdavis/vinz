'use strict';

angular.module('vinzApp')
  .controller('ServerGroupsCtrl', ['$scope', 'serverGroups', function ($scope, serverGroups) {
    $scope.newServerGroup = {name: ""};
    $scope.myServers = serverGroups.getServerGroups();

    $scope.createServer = function(newServerGroup) {
    	serverGroups.createServerGroup(newServerGroup);
    	$scope.myServers = serverGroups.getServerGroups();
    }
<<<<<<< HEAD

    $scope.detail = function(name) {
    	$location.path( '/server_groups/' + name );
    }
  }]);
=======
  }]);
>>>>>>> d60b754d096937b5d4e954fccfff83b4770f4ee1
