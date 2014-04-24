'use strict';

describe('Service: userGroups', function () {

  // load the service's module
  beforeEach(module('vinzApp'));

  // instantiate service
  var userGroups;
  beforeEach(inject(function (_userGroups_) {
    userGroups = _userGroups_;
  }));

  it('should do something', function () {
    expect(!!userGroups).toBe(true);
  });

});
