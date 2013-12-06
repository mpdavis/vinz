'use strict';

angular.module('vinzApp')
  .filter('fromNow', function () {
    return function (date) {
      return moment(date).fromNow();
    };
  });