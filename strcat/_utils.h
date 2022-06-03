#ifndef REDIR_INCLUDED
#define REDIR_INCLUDED

#include <stdio.h>
#include <stdbool.h>
int redirect(const char*, FILE*, const char*);
bool almost_equal(double x, double y); 
int generate_random_array(int arr[], int size, int verbose);

#endif

