'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', ['$scope', 'servers', function ($scope, servers) {
    
    $scope.myServers = servers.getServers();
  }]);