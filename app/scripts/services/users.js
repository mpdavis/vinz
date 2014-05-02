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
        return User.query();
      },
      getUser: function(userId) {
        return User.get({id: userId});
      },
      createUser: function(newUser) {
        $http.post(usersURL, newUser);
      },
      getUserServers: function(userId) {
        return UserServer.query({id: userId});
      },
      getNonUserServers: function(userId) {
        return UserServer.query({id: userId, no_access: true});
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
