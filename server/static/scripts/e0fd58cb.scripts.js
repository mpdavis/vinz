"use strict";angular.module("vinzApp",["ngCookies","ngResource","ngSanitize","ngRoute"]).config(["$routeProvider",function(a){a.when("/",{templateUrl:"views/servers.html",controller:"ServersCtrl"}).when("/servers",{templateUrl:"views/servers.html",controller:"ServersCtrl"}).when("/users",{templateUrl:"views/users.html",controller:"UsersCtrl"}).otherwise({redirectTo:"/"})}]),angular.module("vinzApp").controller("ServersCtrl",["$scope",function(a){a.servers=[{id:"123459",name:"webfilings 1",hostname:"173.30.18.93",access:"yes"},{id:"123460",name:"webfilings 2",hostname:"173.30.18.94",access:"yes"},{id:"123461",name:"isu ",hostname:"173.30.18.95",access:"yes"},{id:"123462",name:"vinz",hostname:"173.30.18.96",access:"yes"}]}]),angular.module("vinzApp").controller("UsersCtrl",["$scope",function(a){a.awesomeThings=["HTML5 Boilerplate","AngularJS","Karma"]}]);