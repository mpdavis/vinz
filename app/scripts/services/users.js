'use strict';

angular.module('vinzApp')
  .factory('users', function ($http, $resource) {
    // Service logic
    // ...
    var usersURL = "/api/users/";
    var usersAPI = usersURL + ":id";
    var User = $resource(usersAPI, {id:'@id'});

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
      }
    };
  });

