"use strict";

let generate = require("./reducer.js");

describe("generate", function () {
  it("returns all fruits starting with letter A", function () {
    var fruits = ["apple", "apricot"];
    var letter = "a";
    var delim = "+";

    var sc = "Fruits starting with letter " + letter + ": ";
    var fout = "apple+apricot";
    var expected = sc + fout;

    expect(generate(fruits, letter, delim)).toEqual(expected);
  });
});

describe("generate", function () {
  it("returns all fruits starting with letter A, sorted", function () {
    var fruits = ["apple", "avocado", "apricot"];
    var letter = "a";
    var delim = "+";

    var sc = "Fruits starting with letter " + letter + ": ";
    var fout = "apple+apricot+avocado";
    var expected = sc + fout;

    expect(generate(fruits, letter, delim)).toEqual(expected);
  });
});

describe("generate", function () {
  it("returns only fruits with start A, sorted", function () {
    var fruits = ["apple", "avocado", "mango", "apricot"];
    var letter = "a";
    var delim = "+";

    var sc = "Fruits starting with letter " + letter + ": ";
    var fout = "apple+apricot+avocado";
    var expected = sc + fout;

    expect(generate(fruits, letter, delim)).toEqual(expected);
  });
});

describe("generate", function () {
  it("fruits string for any letter, case-insensitive, sorted", function () {
    var fruits = ["apple", "avocado", "mango", "apricot", "Mongosteen"];
    var letter = "m";
    var delim = ", ";

    var sc = "Fruits starting with letter " + letter + ": ";
    var fout = "mango, mongosteen";
    var expected = sc + fout;

    expect(generate(fruits, letter, delim)).toEqual(expected);
  });
});

let _ = require("./underscore-min.js");

describe("generate", function () {
  it("output containing fruits with inventory above 0", function () {
    var fruits = ["apple", "avocado", "mango", "apricot", "Mongosteen"];
    var finv = [90, 100, 90, 0, 0];

    var fstore = _.zip(fruits, finv);
    console.log(fstore);

    var letter = "a";
    var delim = ", ";

    var sc = "Fruits starting with letter " + letter + ": ";
    var fout = "apple, avocado";
    var expected = sc + fout;

    expect(generate(fstore, letter, delim)).toEqual(expected);
  });
});
