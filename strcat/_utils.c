#include <math.h>
#include "_utils.h"

int redirect(const char *fname, FILE *fp, const char *access) {
    FILE *f2 = fopen(fname, "r");
    if (f2 == NULL) {
        fprintf(stderr, "%s: File not found!\n", fname);
        FILE *ff = fopen(fname, "w");
        fclose(ff);
        fprintf(stderr, "%s: File now created!\n", fname);

    } else {
        freopen(fname, access, fp);
    }
    return 0;
}

bool almost_equal(double x, double y) { return fabs(x - y) <= 0.0000005; }

// fill up the given 'arr' with random values
// upto a maximum of 'size' number
// The function will return the number of random values
// that were stored in the given array
// If verbose is 1, it prints the contents of the array
#include <stdlib.h>
int generate_random_array(int arr[], int size, int verbose) {
    int randomval = rand();
    // need to generate this of random size as well
    // including zero size array
    int r_size = randomval % (size + 1);
    if (verbose) printf("random size %d ", r_size);

    // let's have three times more positive
    // values than negative
    int sign[] = {-1, 1, 1, 1};

    int mod = 4;
    int only_positive = randomval % 3;
    if (verbose && only_positive) printf("(+ve only)");
    if (!only_positive) {
        if (rand() % 2) {
            if (verbose) printf("(-ve only)");
            mod = 1;
        }
    }

    if (verbose) puts("");

    for (int i = 0; i < r_size; i++) {
        // for size of 20, this works, with sufficient
        // duplicate values being consistently generated
        // for other size values, it may need to be tweaked
        int rand_val = rand() % ((r_size + 1) * 2);
        if (only_positive)
            arr[i] = rand_val;
        else {
            arr[i] = rand_val * sign[rand() % mod] - 1;
        }
    }

    if (verbose) {
        if (r_size == 0) printf("empty array ");
        for (int i = 0; i < r_size; i++) {
            printf("%d, ", arr[i]);
        }
    }

    return r_size;
}