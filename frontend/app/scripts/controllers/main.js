'use strict';

angular.module('vinzApp')
  .controller('MainCtrl', function ($scope) {

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
        }
        ];

    $scope.notifications = [
        {
            id: '12',
            timestamp: new Date(),
            admin: 'jumbles',
            message: 'added you to',
            server: 'vinz_dev'
        },
        {
            id: '13',
            timestamp: new Date(),
            admin: 'jumbles',
            message: 'added you to',
            server: 'vinz_prod'
        },
        {
            id: '14',
            timestamp: new Date(),
            admin: 'jumbles',
            message: 'added you to',
            server: 'vinz_qa'
        }
        ];
  });
