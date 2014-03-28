'use strict';

angular.module('vinzApp')
  .controller('ServerDetailCtrl', ['$scope', 'servers', '$routeParams', function ($scope, servers, $routeParams) {
    
    var serverId = $routeParams.id;
  	$scope.server = servers.getServer(serverId);

  	$scope.serverUsers = servers.getServerUsers(serverId);

  	$scope.revoke = function(userId) {
    	servers.revokeAccess(serverId, userId);
    }
  }]);
