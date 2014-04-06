'use strict';

angular.module('vinzApp')
  .controller('LogsCtrl', ['$scope', 'logService', '$interval', function ($scope, logService, $interval) {
  	var numLogs = 0;
  	$scope.activityLogs = logService.getActivityLogs(function(logs) {
      numLogs = logs.length;
  	});

  	//var count = 1;
  	// var interval = $interval(function() {
   //    console.log(count*30 + 'seconds');
  	// 	logService.getActivityLogs(function(newLogs) {
  	// 		if (newLogs.length != numLogs.length) {
  	// 			$scope.activityLogs = newLogs;
  	// 			numLogs = newLogs.length;
  	// 		}
  	// 	});
  	// }, 30*1000);
  }]);
