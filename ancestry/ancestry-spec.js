"use strict";

let a = require("./ancestry.js");
// require('./ancestry.js');

/**************************
 *
 * Setting up global test data from ancestry data file
 *
 *
 **************************/
let ANCESTRY_FILE = require("./ancestryFile.js");
var ancestry = JSON.parse(ANCESTRY_FILE);

/********* The Actual Test cases ******/

describe("average", function () {
  it("calculates the average age", function () {
    var age = [21, 23, 25, 55, 44];
    expect(a.average(age)).toEqual(33.6);
  });
});

describe("ancestry", function () {
  it("checks that the array contains 39 elements", function () {
    // console.log ("Length of array " + ancestry.length);
    expect(ancestry.length).toEqual(39);
  });
});

describe("ancestry", function () {
  it("calculates average of difference in age between mother and child", function () {
    var withMothers = a.withMothers(ancestry);
    console.log(withMothers);
    expect(withMothers.length).toEqual(18);
    var age = a.buildAgeArray(withMothers);
    expect(a.average(age)).toBeCloseTo(62.83);
  });
});
