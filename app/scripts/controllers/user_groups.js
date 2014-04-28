'use strict';

angular.module('vinzApp')
  .controller('UserGroupsCtrl', ['$scope', 'userGroups', '$location', '$timeout', function ($scope, userGroups, $location, $timeout) {
    $scope.newUserGroup = {name: ""};
    $scope.myUsers = userGroups.getUserGroups();

    $scope.createUser = function(newUserGroup) {
    	userGroups.createUserGroup(newUserGroup);
    	$scope.myUser = userGroups.getUserGroups();
    }

    $scope.detail = function(name) {
    	$location.path( '/user_groups/' + name );
    }
  }]);
