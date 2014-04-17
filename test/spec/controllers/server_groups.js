'use strict';

describe('Controller: ServerGroupsCtrl', function () {

  // load the controller's module
  beforeEach(module('vinzApp'));

  var ServerGroupsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ServerGroupsCtrl = $controller('ServerGroupsCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
