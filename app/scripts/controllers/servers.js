'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', function ($scope) {

    $scope.servers = [
        {
            id: '123459',
            name: 'webfilings 1',
            hostname: '173.30.18.93',
            access: 'yes'
        },
        {
            id: '123460',
            name: 'webfilings 2',
            hostname: '173.30.18.94',
            access: 'yes'
        },
        {
            id: '123461',
            name: 'isu ',
            hostname: '173.30.18.95',
            access: 'yes'
        },
        {
            id: '123462',
            name: 'vinz',
            hostname: '173.30.18.98',
            access: 'yes'
        }
        ];
  });

