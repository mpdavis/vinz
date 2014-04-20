'use strict';

angular.module('vinzApp')
  .controller('ServerGroupDetailCtrl', ['$scope', 'serverGroups', '$routeParams', function ($scope, serverGroups, $routeParams) {
    
    var serverGroupId = $routeParams.id;
  	$scope.serverGroup = serverGroups.getServerGroup(serverGroupId);
    $scope.access = {has:true, message: "Revoke"};

    var accessDictionary = {};

    $scope.groupServers = serverGroups.getGroupServers(serverGroupId, function(groupServers) {
  		for (var i=0; i<groupServers.length; i++) {
  			var server = groupServers[i];
  			accessDictionary[server.id] = false;
  		}
  	});

  	$scope.nonGroupServers = serverGroups.getNonGroupServers(serverGroupId, function(nonGroupServers) {
  		for (var i=0; i<nonGroupServers.length; i++) {
  			var server = nonGroupServers[i];
  			accessDictionary[server.id] = true; 
  		}
  	});

   //  $scope.usersToDisplayUnderServer = $scope.serverUsers;
  	// $scope.showHasAccess = function(yes) {
   //    if (yes) {
   //      $scope.access.has = true;
   //      $scope.access.message = "Revoke";
   //      $scope.usersToDisplayUnderServer = $scope.serverUsers;
   //    } else {
   //      $scope.access.has = false;
   //      $scope.access.message = "Grant";
   //      $scope.usersToDisplayUnderServer = $scope.nonServerUsers;
   //    }
  	// }

  	// $scope.toggleAccess = function(user) {
  	// 	if ($scope.access.has) {
  	// 		servers.revokeAccess(serverId, user.id);
  	// 		accessDictionary[user.id] = false;
   //      removeFromArray($scope.serverUsers, user.id, "id");
   //      $scope.nonServerUsers.push(user);
  	// 	} else {
  	// 		servers.grantAccess(serverId, user.id);
  	// 		accessDictionary[user.id] = true;
   //      removeFromArray($scope.nonServerUsers, user.id, "id");
   //      $scope.serverUsers.push(user);
  	// 	}
   //  }

   //  function removeFromArray(myArray, searchTerm, property) {
   //      console.log(myArray);
   //      for(var i = 0, len = myArray.length; i < len; i++) {
   //          if (myArray[i][property] === searchTerm) {
   //            myArray.splice(i, 1);
   //            return true;
   //          }
   //      }
   //      return false;
   //  }

   //  var hasAccess = function(userId) {
   //  	if (accessDictionary[userId]) {
   //  		return true;
   //  	} else {
   //  		return false;
   //  	}
   //  }
  }]);
