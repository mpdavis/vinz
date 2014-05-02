'use strict';

angular.module('vinzApp')
  .factory('users', function ($http, $resource) {
    // Service logic
    // ...
    var usersURL = "/api/users/";
    var usersAPI = usersURL + ":id";
    var User = $resource(usersAPI, {id:'@id'});

    var userServersAPI = usersAPI + '/servers/:server_id';
    var UserServer = $resource(userServersAPI, {id:'@id'});

    //Users API
    return {
      getUsers: function() {
        var users = User.query();
        return users;
      },
      getUser: function(userId) {
        var user = User.get({id: userId});
        return user;
      },
      createUser: function(newUser) {
        $http.post(usersURL, newUser);
      },
      getUserServers: function(userId, callback) {
        var servers = UserServer.query({id: userId}, function() {
          callback(servers);
        });
        return servers;
      },
      getUserNonServers: function(userId, callback) {
        var servers = UserServer.query({id: userId, no_access: true}, function() {
          callback(servers);
        });
        return servers;
      },
      revokeAccess: function(userId, serverId) {
        UserServer.remove({id: userId, server_id: serverId});
      },
      grantAccess: function(userId, serverId) {
        var userServersAPI = usersURL + userId + '/servers/';
        $http.post(userServersAPI, {server_id: serverId});
      }
    };
  });
