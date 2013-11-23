    // STATUS PAGES
    var fourzerofourController = require('statusPages/fourzerofourController.js'),
    fourzerofourTemplate = require('text!statusPages/fourzerofourTemplate.html');

function routes($routeProvider, $locationProvider) {
    $routeProvider.when('/', {
        'redirectTo': '/dashboard'
    });

    // DASHBOARD
    // $routeProvider.when('/dashboard/', {
    //     'controller': dashboardController,
    //     'template': dashboardTemplate
    // });

    // 404 OTHERWISE
    $routeProvider.otherwise({
        'controller': fourzerofourController,
        'template': fourzerofourTemplate
    });

    // HTML 5 MODE (No hash-bang)
    $locationProvider.html5Mode(true);
}
routes.$inject = ['$routeProvider', '$locationProvider'];
module.exports = routes;