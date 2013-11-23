var angular = require('angular'),

    // RESTANGULAR (REST API CALLS)
    restangular = require('restangular'),

    // VINZ COMPONENTS
    filters = require('filters/init.js'),
    routing = require('routing/init.js')

// VINZ ANGULAR MODULE
var vinz = angular.module('vinz',
    [
        'restangular',
        'vinz-routing'
    ]);

// VINZ CONFIG
function vinzSetup(Restangular) {
    Restangular.setBaseUrl('/api/');
}
vinzSetup.$inject = ['Restangular'];
vinz.run(vinzSetup);

// MANUAL BOOTSTRAP
function vinzBootstrap() {
    angular.element(document).ready(function() {
        angular.bootstrap(document, [vinz.name]);
    });
}

module.exports = {
    'module': vinz,
    'bootstrap': vinzBootstrap
};