'use strict';

angular.module('vinzApp')
  .controller('UserDetailCtrl', ['$scope', 'users', '$routeParams', function ($scope, users, $routeParams) {
    
    var userId = $routeParams.id;
  	$scope.user = users.getUser(userId);
    $scope.access = {has:true, message: "Revoke"};

    var accessDictionary = {};

    $scope.nonUserServers = servers.getNonUserServers(userId, function(nonUserServers) {
  		for (var i=0; i<nonUserServers.length; i++) {
  			var server = nonUserServer[i];
  			accessDictionary[server.id] = false;
  		}
  	});

  	$scope.userServers = users.getUserServers(userId, function(userServers) {
  		for (var i=0; i<userServers.length; i++) {
  			var server = userServers[i];
  			accessDictionary[server.id] = true; 
  		}
  	});

    $scope.serversToDisplayUnderUser = $scope.userServers;
  	$scope.showHasAccess = function(yes) {
      if (yes) {
        $scope.access.has = true;
        $scope.access.message = "Revoke";
        $scope.serversToDisplayUnderUser = $scope.userServers;
      } else {
        $scope.access.has = false;
        $scope.access.message = "Grant";
        $scope.serversToDisplayUnderUser = $scope.nonUserServers;
      }
  	}

  	$scope.toggleAccess = function(user) {
  		if ($scope.access.has) {
  			servers.revokeAccess(userId, server.id);
  			accessDictionary[server.id] = false;
        removeFromArray($scope.userServers, server.id, "id");
        $scope.nonUserServers.push(server);
  		} else {
  			servers.grantAccess(userId, server.id);
  			accessDictionary[server.id] = true;
        removeFromArray($scope.nonUserServers, server.id, "id");
        $scope.userServers.push(server);
  		}
    }

    function removeFromArray(myArray, searchTerm, property) {
        console.log(myArray);
        for(var i = 0, len = myArray.length; i < len; i++) {
            if (myArray[i][property] === searchTerm) {
              myArray.splice(i, 1);
              return true;
            }
        }
        return false;
    }

    var hasAccess = function(serverId) {
    	if (accessDictionary[serverId]) {
    		return true;
    	} else {
    		return false;
    	}
    }
  }]);
