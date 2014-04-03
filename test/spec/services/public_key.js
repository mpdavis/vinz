'use strict';

describe('Service: publicKey', function () {

  // load the service's module
  beforeEach(module('vinzApp'));

  // instantiate service
  var publicKey;
  beforeEach(inject(function (_publicKey_) {
    publicKey = _publicKey_;
  }));

  it('should do something', function () {
    expect(!!publicKey).toBe(true);
  });

});
