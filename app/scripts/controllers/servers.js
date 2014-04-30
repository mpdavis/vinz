'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', ['$scope', 'servers', function ($scope, servers) {
    $scope.newServer = {name: "", hostname: ""};
    $scope.myServers = servers.getServers();

    $scope.createServer = function(newServer) {
    	servers.createServer(newServer);
    	$scope.myServers = servers.getServers();
    }

    var loaded = true;
    $scope.myPagingFunction = function() {
      if (loaded) {
        pageSize++;
        logService.getActivityLogs(page, pageSize, function(logs) {
          for (var i = 0; i < logs.length; i++) {
              $scope.activityLogs.push(logs[i]);
          }
          loaded = true;
        });
      }

      loaded = false;
    }
  }]);