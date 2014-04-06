'use strict';

angular.module('vinzApp')
  .controller('PublicKeyCtrl', ['$scope', 'publicKey', function ($scope, publicKey) {
    $scope.newKey = {key_name: "", value: ""};
    $scope.myKeys = publicKey.getKeys();

    $scope.createKey = function(newKey) {
    	publicKey.createKey(newKey);
    	$scope.myKeys = publicKey.getKeys();
    }

    $scope.removeKey = function(keyId) {
    	publicKey.removeKey(keyId);
    	$scope.myKeys = publicKey.getKeys();
    }
  }]);
