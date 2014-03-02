'use strict';

describe('Service: servers', function () {

  // load the service's module
  beforeEach(module('vinzApp'));

  // instantiate service
  var servers;
  beforeEach(inject(function (_servers_) {
    servers = _servers_;
  }));

  it('should do something', function () {
    expect(!!servers).toBe(true);
  });

});
