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
        templateUrl: 'static/views/logs.html',
        controller: 'LogsCtrl'
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

app.config(['$httpProvider', function($httpProvider){
  var interceptor = ['$rootScope', '$q', function (scope, $q) {
    function success(response) {
        return response;
    }
    function error(response) {
        // Handle 401 errors by redirecting to the login page
        var status = response.status;
        if (status == 401) {
            window.location = "/login/?redirect=" + encodeURIComponent(document.URL);
            return;
        }
        // otherwise
        return $q.reject(response);
    }
    return function (promise) {
        return promise.then(success, error);
    }
  }];
  $httpProvider.responseInterceptors.push(interceptor);
}]);
