'use strict';

angular.module('vinzApp')
  .factory('servers', function ($http, $resource) {
    // Service logic
    // ...
    var serversURL = "/api/servers/"
    var serversAPI = serversURL + ":server_id";
    var Server = $resource(serversAPI, {server_id:'@id'});

    //Servers API
    return {
      getServers: function() {
        var servers = Server.query();
        return servers; 
      },
      createServer: function(newServer) {
        $http.post(serversURL, newServer);
      }
    };
  });

