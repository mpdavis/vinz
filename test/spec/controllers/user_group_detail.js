'use strict';

describe('Controller: UserGroupDetailCtrl', function () {

  // load the controller's module
  beforeEach(module('vinzApp'));

  var UserGroupDetailCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    UserGroupDetailCtrl = $controller('UserGroupDetailCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
