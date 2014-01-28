'use strict';

angular.module('vinzApp')
  .controller('UsersCtrl', function ($scope) {

    $scope.users = [
        {
            name: 'jhummel',
            privelege: 'admin'
        },
        {
            name: 'computemaxer',
            privelege: 'admin'
        },
        {
            name: 'mpdavis',
            privelege: 'admin'
        }
        ];
  });

