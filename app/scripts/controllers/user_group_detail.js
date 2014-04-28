'use strict';

angular.module('vinzApp')
  .controller('UserGroupDetailCtrl', ['$scope', 'userGroups', '$routeParams', function ($scope, userGroups, $routeParams) {
    
    var userGroupId = $routeParams.id;
  	$scope.userGroup = userGroups.getUserGroup(userGroupId);
    $scope.access = {has:true, message: "Revoke"};

    var accessDictionary = {};

    //TODO
    $scope.groupUsers = userGroups.getGroupUsers(userGroupId, function(groupUsers) {
  		for (var i=0; i<groupUsers.length; i++) {
  			var server = groupUsers[i];
  			accessDictionary[user.id] = false;
  		}
  	});

    //TODO
  	$scope.nonGroupUsers = userGroups.getNonGroupUsers(userGroupId, function(nonGroupUsers) {
  		for (var i=0; i<nonGroupUsers.length; i++) {
  			var server = nonGroupUsers[i];
  			accessDictionary[user.id] = true; 
  		}
  	});

  }]);
