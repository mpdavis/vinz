'use strict';

angular.module('vinzApp')
  .factory('userGroups', function ($http, $resource) {
    // Service logic
    // ...

    var meaningOfLife = 42;

    // Public API here
    return {
      someMethod: function () {
        return meaningOfLife;
      }
    };
  });
