'use strict';

angular.module('vinzApp')
  .controller('LogsCtrl', ['$scope', 'logService', '$location', '$timeout', function ($scope, logService, $location, $timeout) {
    $scope.activityLogs = logService.getActivityLogs();

  }]);
