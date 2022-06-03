#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> 

#include "solution.h"

#define STRING_SIZE 100000
#define ARRAY_SIZE  5000

char string[STRING_SIZE]; 

void build_big_string (int ss, int as, int flag) {
    if (ss > STRING_SIZE) 
        ss = STRING_SIZE;
    if (as > ARRAY_SIZE) 
        as = ARRAY_SIZE;
    
    for (int i = 0; i < ss; i++) 
        string[i] = 'a';
    string[ss] = '\0'; 
    
    // char_array to be filled with as 
    // many character strings as its size
    //
    char *char_array[as];
    for (int i = 0; i < as; i++) {
        char_array[i] = string; 
    }
    
    char *one = (char *) malloc(ss * as + 1);
    if (one != NULL) { 
        puts("malloc succeeded! "); 
    }
    else {
      perror("malloc:");
      exit(1);
    }
    
    // use strcat (modified version) to concatenate
    // all the strings into one single blob
    char *onep = one;
    for (int i = 0; i < as; i++) {
        onep = mystrcat(onep, char_array[i], flag); 
    }

    printf("string size: %dMB\n", ss  * as / 1000000);
}


#include <time.h> 

double get_time_for(int ss, int as, int flag) { 
    
    clock_t begin = clock();
    build_big_string(ss, as, flag);
    clock_t finish = clock();
    double time_spent = (double)
        (finish - begin) / CLOCKS_PER_SEC;

    printf ("Time taken for %d(size)*%d(num) = %lf\n", ss, as, time_spent); 
    return time_spent; 
}
