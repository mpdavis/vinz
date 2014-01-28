'use strict';

angular.module('vinzApp')
  .controller('ServersCtrl', function ($scope) {

    $scope.servers = [
        {
            id: '123456',
            name: 'vinz_dev',
            hostname: '10.1.1.30',
            permission: 'admin'
        },
        {
            id: '123458',
            name: 'vinz_prod',
            hostname: '10.1.1.32',
            permission: 'user'
        },
        {
            id: '123457',
            name: 'vinz_qa',
            hostname: '10.1.1.50',
            permission: 'user'
        },
        {
            id: '123459',
            name: 'webfilings 1',
            hostname: '10.1.1.32',
            permission: 'user'
        },
        {
            id: '123460',
            name: 'webfilings 2',
            hostname: '10.1.1.50',
            permission: 'user'
        },
        {
            id: '123461',
            name: 'isu ',
            hostname: '10.1.1.32',
            permission: 'user'
        },
        {
            id: '123462',
            name: 'vinz_qa',
            hostname: '10.1.1.50',
            permission: 'user'
        }
        ];
  });
