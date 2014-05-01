'use strict';

angular.module('vinzApp')
  .factory('serverGroups', function ($http, $resource) {
    // Service logic
    // ...
    var serverGroupsURL = "/api/servergroups/";
    var serverGroupsAPI = serverGroupsURL + ":id";
    var ServerGroup = $resource(serverGroupsAPI, {id:'@id'});

    var groupServersAPI = serverGroupsAPI + '/servers/:server_id';
    var GroupServer = $resource(groupServersAPI, {id:'@id'});

    var groupUsersAPI = serverGroupsAPI + '/users/:user_id';
    var GroupUser = $resource(groupUsersAPI, {id:'@id'});

    var groupUserGroupsAPI = serverGroupsAPI + '/usergroups/:user_group_id';
    var GroupUserGroup = $resource(groupUserGroupsAPI, {id:'@id'});

    //serverGroups API
    return {
      getServerGroups: function() {
        return ServerGroup.query();
      },
      getServerGroup: function(serverGroupId) {
        return ServerGroup.get({id: serverGroupId});
      },
      createServerGroup: function(newServerGroup) {
        $http.post(serverGroupsURL, newServerGroup);
      },
      getGroupServers: function(serverGroupId) {
        return GroupServer.query({id: serverGroupId});
      },
      getNonGroupServers: function(serverGroupId) {
        return GroupServer.query({id: serverGroupId, not_in_group: true});
      },
      removeServerFromGroup: function(serverGroupId, serverId) {
        GroupServer.remove({id: serverGroupId, server_id: serverId});
      },
      addServerToGroup: function(serverGroupId, serverId) {
        var groupServersAPI = serverGroupsURL + serverGroupId + '/servers/';
        $http.post(groupServersAPI, {server_id: serverId});
      },
      getServerGroupUsers: function(serverGroupId) {
        return GroupUser.query({id: serverGroupId});
      },
      getNonServerGroupUsers: function(serverGroupId) {
        return GroupUser.query({id: serverGroupId, no_access: true});
      },
      revokeUserAccessToGroup: function(serverGroupId, userId) {
        GroupUser.remove({id: serverGroupId, user_id: userId});
      },
      grantUserAccessToGroup: function(serverGroupId, userId) {
        var groupUsersAPI = serverGroupsURL + serverGroupId + '/users/';
        $http.post(groupUsersAPI, {user_id: userId});
      },
      getServerGroupUserGroups: function(serverGroupId) {
        return GroupUserGroup.query({id: serverGroupId});
      },
      getNonServerGroupUserGroups: function(serverGroupId) {
        return GroupUserGroup.query({id: serverGroupId, no_access: true});
      },
      revokeUserGroupAccessToGroup: function(serverGroupId, userGroupId) {
        GroupUserGroup.remove({id: serverGroupId, user_group_id: userGroupId});
      },
      grantUserGroupAccessToGroup: function(serverGroupId, userGroupId) {
        var groupUserGroupsAPI = serverGroupsURL + serverGroupId + '/usergroups/';
        $http.post(groupUserGroupsAPI, {user_group_id: userGroupId});
      }
    };
  });
