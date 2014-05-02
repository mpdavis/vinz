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
      getUserServers: function(userGroupId) {
        return UserServer.query({id: userGroupId});
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
      },
      getUserGroupServer: function(userGroupId) {
        return GroupServer.query({id: userGroupId});
      },
      getNonUserGroupServers: function(userGroupId) {
        return GroupServer.query({id: userGroupId, no_access: true});
      },
      revokeServerAccessToGroup: function(userGroupId, serverId) {
        GroupServer.remove({id: userGroupId, server_id: serverId});
      },
      grantServerAccessToGroup: function(userGroupId, serverId) {
        var groupServersAPI = userGroupsURL + userGroupId + '/servers/';
        $http.post(groupServersAPI, {server_id: serverId});
      },
      getUserGroupServerGroups: function(userGroupId) {
        return GroupServerGroup.query({id: userGroupId}); 
      },
      getNonUserGroupServerGroups: function(userGroupId) {
        return GroupServerGroup.query({id: userGroupId, no_access: true});
      },
      revokeServerGroupAccessToGroup: function(userGroupId, serverGroupId) {
        GroupServerGroup.remove({id: userGroupId, server_group_id: serverGroupId});
      },
      grantServerGroupAccessToGroup: function(userGroupId, serverGroupId) {
        var groupServerGroupsAPI = userGroupsURL + userGroupId + '/servergroups/';
        $http.post(groupServerGroupsAPI, {server_group_id: serverGroupId});
      }
    };
  });
