#include "index.h"
#include <string.h>
#include <ctype.h>


int is_not_same (char pc, char tc) { 
    return tolower(pc) != tolower(tc); 
}

int indexOf(char* text, char* pattern, int match_at)

{
    int res = 0;  // by default will return a match at index 0
    int last_match = -1;
    int text_l = strlen(text); 
    int pattern_l = strlen(pattern); 

    for (int index = 0; index < text_l; index++) { 
        res = index; 

        for (int pindex = 0; pindex < pattern_l; pindex++) {
            if (is_not_same(pattern[pindex], text[(index + pindex) % text_l]) )
                res = -1; 
    
        }
        if (res != -1) {
            last_match = res;
            if (match_at-- == FIRST)
                break;
        }
    }

   
    return last_match != -1? last_match : res; 
}