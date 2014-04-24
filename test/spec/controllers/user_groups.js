'use strict';

describe('Controller: UserGroupsCtrl', function () {

  // load the controller's module
  beforeEach(module('vinzApp'));

  var UserGroupsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    UserGroupsCtrl = $controller('UserGroupsCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
