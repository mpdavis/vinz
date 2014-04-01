'use strict';

angular.module('vinzApp')
  .controller('ServerDetailCtrl', ['$scope', 'servers', 'users', '$routeParams', function ($scope, servers, $routeParams) {
    
    var serverId = $routeParams.id;
  	$scope.server = servers.getServer(serverId);

	$scope.nonServerUsers = servers.getServerNonUsers(function(nonServerUsers) {
  		for (var i=0; i<nonServerUsers.length; i++) {
  			var user = nonServerUsers[i];
  			if (!hasAccess(user.id])) {
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

  	$scope.showHasAccessUsers = function(access) {
  		if (access) {
  			$scope.usersToDisplayUnderServer = $scope.serverUsers;
  		} else {
  			$scope.usersToDisplayUnderServer = $scope.nonServerUsers;
  		}
  	}

  	$scope.toggleAccess = function(userId) {
  		if (hasAccess(userId)) {
  			servers.revokeAccess(serverId, userId);
  			accessDictionary[userId] = false;
  		} else {
  			servers.grantAccess(serverId, userId);
  			accessDictionary[userId] = true;
  		}
    }

    function hasAccess = function(user) {
    	var userId = user.id;
    	if (accessDictionary[userId]) {
    		return true;
    	} else {
    		return false;
    	}
    }
  }]);
