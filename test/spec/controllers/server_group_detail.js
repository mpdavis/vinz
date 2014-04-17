'use strict';

describe('Controller: ServerGroupDetailCtrl', function () {

  // load the controller's module
  beforeEach(module('vinzApp'));

  var ServerGroupDetailCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ServerGroupDetailCtrl = $controller('ServerGroupDetailCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
