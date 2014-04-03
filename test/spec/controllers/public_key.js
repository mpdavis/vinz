'use strict';

describe('Controller: PublicKeyCtrl', function () {

  // load the controller's module
  beforeEach(module('vinzApp'));

  var PublicKeyCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PublicKeyCtrl = $controller('PublicKeyCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
