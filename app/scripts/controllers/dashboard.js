'use strict';

angular.module('vinzApp')
  .controller('DashboardCtrl', ['$scope', 'dashboard', function ($scope, dashboard) {

    $scope.chartConfig = {
        options: {
            chart: {
                type: 'area'
            }
        },
        series: [{
            name: "Success",
            data: []
        },
        {
            name: "Failure",
            data: []
        }],
        title: {
            text: 'Scans'
        },
        yAxis: {
          gridLineWidth: 0,
          minorGridLineWidth: 0,
          title: {
            text: 'Scans'
          },  
        },
        xAxis: {
          title: {
            text: 'Days'
          },
          categories: ['7', '6', '5', '4', '3', '2', '1']

        },
        loading: false
    };

  	dashboard.getStats().success(function(data, status, headers, config) {
    	$scope.stats = data;	
    });

    dashboard.getLogs().success(function(data, status, headers, config) {
      $scope.chartConfig.series[0].data = data.success;
      $scope.chartConfig.series[1].data = data.failure;
    });
    
    
  }]);
