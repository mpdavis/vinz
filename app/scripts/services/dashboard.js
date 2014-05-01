'use strict';

angular.module('vinzApp')
  .factory('dashboard', function ($http) {
    
    var statsAPI = "/api/stats/";
    var logsAPI = "/api/scan_log_graph/";

    return {
      getStats: function() {
        return $http.get(statsAPI);
      },

      getLogs: function() {
        return $http.get(logsAPI);
      }

    };
  });