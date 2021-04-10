'use strict';
 
module.exports = destroyer;
 
function destroyer(arr) {
  var args = Array.prototype.slice.call (arguments); 
  args.splice (0, 1); 
 
  for (var x = 0; x < arr.length; x++ ) { 
    for (var y = 0; y < args.length; y++ ) { 
      if (arr[x] === args[y]) {
        delete arr[x]; 
      }
    }
  }
 
  return arr.filter (function (elem) 
    { return Boolean(elem); });  // removes the null elements; 
}

function destroyer(arr) {
 
  var args = Array.prototype.slice.call (arguments); 
  args.splice (0,1); 
 
  var isNotInList = function (elem, list) {
    return list.indexOf (elem) === -1; 
  }; 
 
  var res = arr.filter (function (elem) {
      return isNotInList (elem, args); 
  }); 
 
  console.log (res); 
 
  return res;
}