'use strict';

angular.module('vinzApp')
  .controller('UsersCtrl', ['$scope', 'users', '$location', '$timeout', function ($scope, users, $location, $timeout) {
    $scope.newUser = {first_name: "", last_name: "", email: ""};
    $scope.myUsers = users.getUsers();
    $scope.finish = false;

    $scope.createUser = function(newUser) {
    	users.createUser(newUser);
    	$scope.myUsers = users.getUsers();
    }
  }]);
