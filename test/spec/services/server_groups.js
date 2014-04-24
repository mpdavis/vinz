'use strict';

describe('Service: serverGroups', function () {

  // load the service's module
  beforeEach(module('vinzApp'));

  // instantiate service
  var serverGroups;
  beforeEach(inject(function (_serverGroups_) {
    serverGroups = _serverGroups_;
  }));

  it('should do something', function () {
    expect(!!serverGroups).toBe(true);
  });

});
