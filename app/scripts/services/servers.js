'use strict';

angular.module('vinzApp')
  .factory('servers', function ($http, $resource) {
    // Service logic
    // ...
    var serversURL = "/api/servers/";
    var serversAPI = serversURL + ":id";
    var Server = $resource(serversAPI, {id:'@id'});

    //Servers API
    return {
      getServers: function() {
        var servers = Server.query();
        return servers;
      },
      getServer: function(serverId) {
        var server = Server.get({id: serverId});
        return server;
      },
      createServer: function(newServer) {
        $http.post(serversURL, newServer);
      }
    };
  });

