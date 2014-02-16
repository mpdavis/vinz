'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', ['$scope', 'servers', function ($scope, servers) {
    $scope.servers = servers.getServers();
    $scope.urlTest = servers.canGetRealServers();
  }]);

