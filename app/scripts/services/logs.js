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
      getActivityLogs: function(callback) {
        var logs = Log.query(function() {
          for (key in logs) {
              if (logs.hasOwnProperty(key)) {
                  logs[key].timestamp = Date.parse(logs[key].timestamp); 
              }
          }

          callback(logs);
        });

        return logs;
      }
    };
  });

