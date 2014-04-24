'use strict';

angular.module('vinzApp')
  .controller('ServerGroupDetailCtrl', ['$scope', 'serverGroups', '$routeParams', function ($scope, serverGroups, $routeParams) {
    
    var serverGroupId = $routeParams.id;
  	$scope.serverGroup = serverGroups.getServerGroup(serverGroupId);
    $scope.access = {has:true, message: "Revoke"};

    var accessDictionary = {};

    //TODO
    $scope.groupServers = serverGroups.getGroupServers(serverGroupId, function(groupServers) {
  		for (var i=0; i<groupServers.length; i++) {
  			var server = groupServers[i];
  			accessDictionary[server.id] = false;
  		}
  	});

    //TODO
  	$scope.nonGroupServers = serverGroups.getNonGroupServers(serverGroupId, function(nonGroupServers) {
  		for (var i=0; i<nonGroupServers.length; i++) {
  			var server = nonGroupServers[i];
  			accessDictionary[server.id] = true; 
  		}
  	});

  }]);
