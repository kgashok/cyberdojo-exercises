'use strict';

function average (array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

function withMothers (ancestry) {
  var byName = {};
  ancestry.forEach(function(person) {
    byName[person.name] = person;
  });

  return ancestry.filter(function(person) {
    return Boolean(byName[person.mother]); 
  });
}

function buildAgeArray (mlist) { 
  return mlist.map (function (person) {
    return person["died"] - person["born"]; 
  }); 
}


module.exports.buildAgeArray = buildAgeArray;
module.exports.withMothers   = withMothers;
module.exports.average       = average;

