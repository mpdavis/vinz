'use strict';

angular.module('vinzApp')
  .factory('logService', function ($http, $resource) {
    // Service logic
    // ...
    var logsUrl = "/api/logs/";
    var logsApi = logsUrl + ":id";
    var Log = $resource(logsApi, {id:'@id'});

    //Servers API
    return {
      getActivityLogs: function() {
        return Log.query();
      }
    };
  });

