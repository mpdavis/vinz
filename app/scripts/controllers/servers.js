'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', ['$scope', 
  								'servers', 
  								'$location', 
  								'$timeout', 
  function ($scope, servers, $location, $timeout) {
    $scope.newServer = {name: "", hostname: ""};
    $scope.myServers = servers.getServers();
    $scope.finish = false;

    $scope.createServer = function(newServer) {
    	servers.createServer(newServer);
    	$scope.myServers = servers.getServers();
    }

    $scope.detail = function(name) {
    	$scope.finish = true;
    	$timeout(function() {
    		$location.path( '/servers/' + name );
    	}, 500);	
    }
  }]);