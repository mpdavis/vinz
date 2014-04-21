'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', ['$scope', 'servers', '$location', function ($scope, servers, $location) {
    $scope.newServer = {name: "", hostname: ""};
    $scope.myServers = servers.getServers();

    $scope.createServer = function(newServer) {
    	servers.createServer(newServer);
    	$scope.myServers = servers.getServers();
    }

    $scope.detail = function(name) {
    	$location.path( '/servers/' + name );	
    }
  }]);