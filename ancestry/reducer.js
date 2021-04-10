'use strict';

module.exports = generate;

function generate(flist, begin, delim) {

  return "Fruits starting with letter " + begin + ": " + 
            
          flist.reduce (function (prev, tok) {
              var stock = -1;
              if (typeof tok === "object")
              {
                stock = tok[1];
                tok   = tok[0];
              }

              if (stock <0 || stock> 0 ) { 
                tok = tok.toLowerCase();
                if (tok.charAt(0) === begin) {
                  prev.push(tok);
                }
              }
              return prev;
          }, [])
          .sort().join(delim);

  }
  