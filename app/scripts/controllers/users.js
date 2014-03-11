'use strict';

angular.module('vinzApp')
  .controller('UsersCtrl', ['$scope', 'users', function ($scope, users) {
    $scope.users = users.getUsers();
  }]);
