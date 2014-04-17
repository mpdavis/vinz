'use strict';

angular.module('vinzApp')
  .factory('serverGroups', function () {
    // Service logic
    // ...
    var serverGroupsURL = "/api/servergroups/";
    var serverGroupsAPI = serverGroupsURL + ":id";
    var ServerGroup = $resource(serverGroupsAPI, {id:'@id'});

    // var serverUsersAPI = serverGroupsAPI + '/users/:user_id';
    // var ServerUser = $resource(serverUsersAPI, {id:'@id'});

    //serverGroups API
    return {
      getserverGroups: function() {
        var serverGroups = ServerGroup.query();
        return serverGroups;
      },
      getServerGroup: function(serverGroupId) {
        var server = Server.get({id: serverGroupId});
        return server;
      },
      createServerGroup: function(newServerGroup) {
        $http.post(serverGroupsURL, newServerGroup);
      },
      // getServerGroupUsers: function(serverId, callback) {
      //   var users = ServerUser.query({id: serverId}, function() {
      //     callback(users);
      //   });
      //   return users;
      // },
      // getNonServerGroupUsers: function(serverId, callback) {
      //   var users = ServerUser.query({id: serverId, no_access: true}, function() {
      //     callback(users);
      //   });
      //   return users;
      // },
      // revokeAccess: function(serverId, userId) {
      //   ServerUser.remove({id: serverId, user_id: userId});
      // },
      // grantAccess: function(serverId, userId) {
      //   var serverUsersAPI = serverGroupsURL + serverId + '/users/';
      //   $http.post(serverUsersAPI, {user_id: userId});
      // }
    };
  });
