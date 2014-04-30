'use strict';

angular.module('vinzApp')
  .controller('LogsCtrl', ['$scope', 'logService', '$interval', function ($scope, logService, $interval) {
  	var numLogs = 0;
    var page = 1;
    var pageSize = 30;
  	
    $scope.activityLogs = logService.getActivityLogs(page, pageSize, function(logs) {
      numLogs = logs.length;
  	});

    var loaded = true;
  	$scope.myPagingFunction = function() {
      if (loaded) {
        page++;
        logService.getActivityLogs(page, pageSize, function(logs) {
          for (var i = 0; i < logs.length; i++) {
              $scope.activityLogs.push(logs[i]);
          }
          loaded = true;
        });
      }

      loaded = false;
    }
}]);
