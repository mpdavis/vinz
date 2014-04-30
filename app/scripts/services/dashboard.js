'use strict';

angular.module('vinzApp')
  .factory('dashboard', function ($http) {
    // Service logic
    // ...
    var statsAPI = "/api/stats/";
    var logsAPI = "/api/scan_log_graph/";

    //Users API
    return {
      getStats: function() {
        var stats = $http.get(statsAPI);
        return stats;
      },

      getLogs: function() {
        var logs = $http.get(logsAPI);
        return logs
      }

    };
  });