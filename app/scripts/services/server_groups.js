'use strict';

angular.module('vinzApp')
  .factory('serverGroups', function ($http, $resource) {
    // Service logic
    // ...
    var serverGroupsURL = "/api/servergroups/";
    var serverGroupsAPI = serverGroupsURL + ":id";
    var ServerGroup = $resource(serverGroupsAPI, {id:'@id'});

    var groupServersAPI = serverGroupsAPI + '/servers/:servers_id';
    var GroupServer = $resource(groupServersAPI, {id:'@id'});

    //serverGroups API
    return {
      getServerGroups: function() {
        var serverGroups = ServerGroup.query();
        return serverGroups;
      },
      getServerGroup: function(serverGroupId) {
        var serverGroup = ServerGroup.get({id: serverGroupId});
        return serverGroup;
      },
      createServerGroup: function(newServerGroup) {
        $http.post(serverGroupsURL, newServerGroup);
      },
      getGroupServers: function(serverGroupId, callback) {
        var servers = GroupServer.query({id: serverGroupId}, function() {
          callback(servers);
        });
        return servers;
      },
      getNonGroupServers: function(serverGroupId, callback) {
        //TODO
        var servers = GroupServer.query({id: serverGroupId}, function() {
          callback(servers);
        });
        return servers;
      }
    };
  });
