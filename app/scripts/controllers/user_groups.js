'use strict';

angular.module('vinzApp')
  .controller('UserGroupsCtrl', ['$scope', 'userGroups', function ($scope, userGroups) {
    $scope.newUserGroup = {name: ""};
    $scope.myUserGroups = userGroups.getUserGroups();

    $scope.createUser = function(newUserGroup) {
    	userGroups.createUserGroup(newUserGroup);
    	$scope.myUserGroups = userGroups.getUserGroups();
    }
  }]);
