'use strict';

angular.module('vinzApp')
  .controller('UsersCtrl', ['$scope', 'users', function ($scope, users) {
    $scope.newUser = {username: "", first_name: "", last_name: "", email: ""};
    $scope.myUsers = users.getUsers();

    $scope.createUser = function(newUser) {
    	users.createUser(newUser);
    	$scope.myUsers = users.getUsers();
    }

  }]);
