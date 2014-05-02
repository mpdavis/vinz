'use strict';

angular.module('vinzApp')
  .controller('UserDetailCtrl', ['$scope', 'users', '$routeParams', function ($scope, users, $routeParams) {
    
    var userId = $routeParams.id;
    
    $scope.myServers = users.getUserServers(userId);


  }]);
