'use strict';

angular.module('vinzApp')
  .factory('userGroups', function ($http, $resource) {
    // Service logic
    // ...
    var userGroupsURL = "/api/usergroups/";
    var userGroupsAPI = userGroupsURL + ":id";
    var userGroup = $resource(userGroupsAPI, {id:'@id'});

    var groupUsersAPI = userGroupsAPI + '/users/:users_id';
    var GroupUser = $resource(groupUsersAPI, {id:'@id'});

    //serverGroups API
    return {
      getUserGroups: function() {
        var userGroups = UserGroup.query();
        return userGroups;
      },
      getUserGroup: function(userGroupId) {
        var userGroup = UserGroup.get({id: userGroupId});
        return userGroup;
      },
      createUserGroup: function(newUserGroup) {
        $http.post(userGroupsURL, newUserGroup);
      },
      getGroupUsers: function(userGroupId, callback) {
        var servers = GroupUser.query({id: userGroupId}, function() {
          callback(users);
        });
        return users;
      },
      getNonGroupUsers: function(userGroupId, callback) {
        //TODO
        var users = GroupUsers.query({id: userGroupId}, function() {
          callback(users);
        });
        return users;
      }
    };
  });
