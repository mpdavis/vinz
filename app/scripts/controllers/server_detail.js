'use strict';

angular.module('vinzApp')
  .controller('ServerDetailCtrl', ['$scope', 'servers', 'users', '$routeParams', function ($scope, servers, users, $routeParams) {
    
    var serverId = $routeParams.id;
  	$scope.server = servers.getServer(serverId);

  	var accessDictionary = {};

  	$scope.allUsers = users.getUsers(function(users) {
  		for (var i=0; i<users.length; i++) {
  			var user = users[i];
  			if (!accessDictionary[user.id]) {
  				accessDictionary[user.id] = false;
  			}
  		}
  	});

  	$scope.serverUsers = servers.getServerUsers(serverId, function(serverUsers) {
  		for (var i=0; i<serverUsers.length; i++) {
  			var user = serverUsers[i];
  			accessDictionary[user.id] = true;
  		}
  	});

  	$scope.toggleAccess = function(userId) {
  		if ($scope.hasAccess(userId)) {
  			servers.revokeAccess(serverId, userId);
  			accessDictionary[userId] = false;
  		} else {
  			servers.grantAccess(serverId, userId);
  			accessDictionary[userId] = true;
  		}
    }

    $scope.hasAccess = function(user) {
    	var userId = user.id;
    	if (accessDictionary[userId]) {
    		return true;
    	} else {
    		return false;
    	}
    }
  }]);
