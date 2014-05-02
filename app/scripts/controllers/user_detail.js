'use strict';

angular.module('vinzApp')
  .controller('UserDetailCtrl', ['$scope', 'users', '$routeParams', function ($scope, users, $routeParams) {
    
    var userId = $routeParams.id;
    
    $scope.user = users.getUser(userId);
    $scope.myServers = users.getUserServers(userId);

    

  }]);
