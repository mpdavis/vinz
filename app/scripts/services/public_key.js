'use strict';

angular.module('vinzApp')
  .factory('publicKey', function () {
    // Service logic
    // ...
    var keysURL = "/api/keys/";
    var keysAPI = keysURL + ":id";
    var Key = $resource(keysAPI, {id:'@id'});

    //Keys API
    return {
      getKeys: function() {
        return Key.query();
      },
      getKey: function(keyId) {
        return Key.get({id: KeyId});
      },
      createKey: function(newKey) {
        $http.post(keysURL, newKey);
      },
      removeKey: function(keyId) {
        Key.remove({id: KeyId});
      }
    };
  });
