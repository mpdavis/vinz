'use strict';

angular.module('vinzApp')
  .factory('servers', function ($http, $resource) {
    // Service logic
    // ...
    var serversAPI = "/api/servers/:server_id";
    var Server = $resource(serversAPI, {server_id:'@id'});

    //Servers API
    return {
      getServers: function() {
        var servers = Server.query();
        return servers; 
      }
    };
  });

