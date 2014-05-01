'use strict';

angular.module('vinzApp')
  .controller('DashboardCtrl', ['$scope', 'dashboard', function ($scope, dashboard) {

    $scope.flotOptions = {
      'width': 500,
      'height': 500
    };
  	dashboard.getStats().success(function(data, status, headers, config) {
    	$scope.stats = data;	
    });

    dashboard.getLogs().success(function(data, status, headers, config) {
      $scope.graph_data = data.success;
    });

    $scope.graphData = [[1, 2], [2, 5], [3, 7]];
  }]);
