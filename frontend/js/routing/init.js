var angular = require('angular'),
    angularRoute = require('angular-route'),
    routes = require('./routes.js');

var routing = angular.module('vinz-routing',
    [
        'ngRoute'
    ]
);
routing.config(routes);