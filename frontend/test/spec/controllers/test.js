'use strict';

describe('Controller: TestCtrl', function () {

  // load the controller's module
  beforeEach(module('vinzApp'));

  var TestCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    TestCtrl = $controller('TestCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.gateKeepers.length).toBe(6);
  });
});
