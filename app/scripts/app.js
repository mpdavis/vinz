'use strict';

var app = angular.module('vinzApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'infinite-scroll'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/views/dashboard.html',
        controller: 'DashboardCtrl'
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
      .when('/public_key', {
        templateUrl: 'static/views/public_key.html',
        controller: 'PublicKeyCtrl'
      })
      .when('/server_groups', {
        templateUrl: 'static/views/server_groups.html',
        controller: 'ServerGroupsCtrl'
      })
      .when('/server_groups/:id', {
        templateUrl: 'static/views/server_group_detail.html',
        controller: 'ServerGroupDetailCtrl'
      })
      .when('/user_groups', {
        templateUrl: 'static/views/user_groups.html',
        controller: 'UserGroupsCtrl'
      })
      .when('/user_groups/:id', {
        templateUrl: 'static/views/user_group_detail.html',
        controller: 'UserGroupDetailCtrl'
      })
      .when('/dashboard', {
        templateUrl: 'static/views/dashboard.html',
        controller: 'DashboardCtrl'
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
