'use strict';

angular.module('vinzApp')
  .controller('NotificationsCtrl', function ($scope) {
    
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
