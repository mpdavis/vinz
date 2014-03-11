'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', ['$scope', 'servers', function ($scope, servers) {
    
    $scope.myServers = servers.getServers();

    $scope.createServer = function(newServer) {
    	servers.createServer(newServer);
    	$scope.myServers = servers.getServers();
    }
  }]);