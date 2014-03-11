'use strict';

angular.module('vinzApp')
  .factory('users', function ($http) {
    // Service logic
    // ...
    var meaningOfLife = 42;

    // Public API here
    return {
      someMethod: function () {
        return meaningOfLife;
      },
      getUsers: function() {
        var usersArray = [
        {
            first_name: 'Michael',
            last_name: 'Davis',
            email: '...'
        },
        {
            first_name: 'Eric',
            last_name: 'Feldmann',
            email: '...'
        },
        {
            first_name: 'Zach',
            last_name: 'Heilman',
            email: '...'
        },
        {
            first_name: 'Jacob',
            last_name: 'Hummel',
            email: '...'
        },
        {
            first_name: 'Max',
            last_name: 'Peterson',
            email: '...'
        },
        {
            first_name: 'Ario',
            last_name: 'Xiao Gin',
            email: '...'
        }
        ];

        return usersArray;
      }
    };
  });

