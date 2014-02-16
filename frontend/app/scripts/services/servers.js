'use strict';

angular.module('vinzApp')
  .factory('servers', function ($http) {
    // Service logic
    // ...
    var local = "http://10.13.37.2";
    var serversAPI = "/api/servers/";
    var meaningOfLife = 42;

    // Public API here
    return {
      someMethod: function () {
        return meaningOfLife;
      },
      getServers: function() {
      	var serversArray = [
        {
            id: '123459',
            name: 'webfilings 1',
            hostname: '173.30.18.93',
            access: 'yes'
        },
        {
            id: '123460',
            name: 'webfilings 2',
            hostname: '173.30.18.94',
            access: 'yes'
        },
        {
            id: '123461',
            name: 'isu ',
            hostname: '173.30.18.95',
            access: 'yes'
        },
        {
            id: '123462',
            name: 'vinz',
            hostname: '173.30.18.96',
            access: 'yes'
        }
        ];

      	return serversArray;
      },
      canGetRealServers: function() {
      	$http.get(local + serversAPI).success(function(data) {
	        return "boom";
	    }).error(function(data) {
	        return "nah";
	    });  
      }
  	};
  });
