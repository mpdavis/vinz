'use strict';

angular.module('vinzApp')
  .factory('userGroups', function ($http, $resource) {
    // Service logic
    // ...
    var userGroupsURL = "/api/usergroups/";
    var userGroupsAPI = userGroupsURL + ":id";
    var UserGroup = $resource(userGroupsAPI, {id:'@id'});

    var groupUsersAPI = userGroupsAPI + '/users/:user_id';
    var GroupUser = $resource(groupUsersAPI, {id:'@id'});

    var groupServersAPI = userGroupsAPI + '/servers/:server_id';
    var GroupServer = $resource(groupServersAPI, {id:'@id'});

    var groupServerGroupsAPI = userGroupsAPI + '/servergroups/:server_group_id';
    var GroupServerGroup = $resource(groupServerGroupsAPI, {id:'@id'});

    //userGroups API
    return {
      getUserGroups: function() {
        return UserGroup.query();
      },
      getUserGroup: function(userGroupId) {
        return UserGroup.get({id: userGroupId});
      },
      createUserGroup: function(newUserGroup) {
        $http.post(userGroupsURL, newUserGroup);
      },
      getGroupUsers: function(userGroupId) {
        return GroupUser.query({id: userGroupId});
      },
      getNonGroupUsers: function(userGroupId) {
        return GroupUser.query({id: userGroupId, not_in_group: true});
      },
      removeUserFromGroup: function(userGroupId, userId) {
        GroupUser.remove({id: userGroupId, user_id: userId});
      },
      addUserToGroup: function(userGroupId, userId) {
        var groupUsersAPI = userGroupsURL + userGroupId + '/users/';
        $http.post(groupUsersAPI, {user_id: userId});
      }
    };
  });
