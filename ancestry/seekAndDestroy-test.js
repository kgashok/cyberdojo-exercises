'use strict';

let destroyer = require('./seekAndDestroy-test.js');

test("destroy", function() {
    deepEqual(destroyer([1, 2, 3], 1, 2), [3], "remove 1 and 2 and leave 3");
});
