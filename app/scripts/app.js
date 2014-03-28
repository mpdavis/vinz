'use strict';

var app = angular.module('vinzApp', [
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
      .when('/servers/:id', {
        templateUrl: 'static/views/server_detail.html',
        controller: 'ServerDetailCtrl'
      })
      .when('/logs', {
        templateUrl: 'static/views/logs.html',
        controller: 'LogsCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
