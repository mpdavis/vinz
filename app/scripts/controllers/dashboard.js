'use strict';

angular.module('vinzApp')
  .controller('DashboardCtrl', ['$scope', 'dashboard', function ($scope, dashboard) {

  	$scope.dashboardDimensions = {};
    $scope.flotOptions = {

    };
  	dashboard.getStats().success(function(data, status, headers, config) {
    	$scope.stats = data;	
    });

    dashboard.getLogs().success(function(data, status, headers, config) {
      $scope.graph_data = data;
    });

    
  }]);
