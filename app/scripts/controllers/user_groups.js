'use strict';

angular.module('vinzApp')
  .controller('UserGroupsCtrl', ['$scope', 'userGroups', function ($scope, userGroups) {
    $scope.newUserGroup = {name: ""};
    $scope.myUsers = userGroups.getUserGroups();

    $scope.createUser = function(newUserGroup) {
    	userGroups.createUserGroup(newUserGroup);
    	$scope.myUsers = userGroups.getUserGroups();
    }
  }]);
