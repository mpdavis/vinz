'use strict';

angular.module('vinzApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/views/servers.html',
        controller: 'ServersCtrl'
      })
      .when('/servers', {
        templateUrl: 'static/views/servers.html',
        controller: 'ServersCtrl'
      })
      .when('/users', {
        templateUrl: 'static/views/users.html',
        controller: 'UsersCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
