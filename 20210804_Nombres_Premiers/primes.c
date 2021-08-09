#include <time.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

#define SOME_BIG_NUMBER 5000
#define FIRST_PRIME 2

// ----------
// C language does not integer square root, so here is an implementation
// (copy-pasted from the internet)
// ----------
uint64_t isqrt(uint64_t x) {
  uint64_t q = 1, r = 0;
  while (q <= x) {
    q <<= 2;
  }
  while (q > 1) {
    uint64_t t;
    q >>= 2;
    t = x - r - q;
    r >>= 1;
    x = t;
    r += q;
  }
  return r;
}
// ----------


// ----------
// C language does not have high-level types such as Python 'list', C++ 'vector'
// or JavaScript 'Array'
// This code implements a structure & functions which can be used as a (very)
// basic, appendable array.
// ----------

typedef struct {
  uint32_t* _array;
  size_t _current_size;
  size_t _memory_size;
} Primes;

Primes* init_primes(size_t size) {
  uint32_t* array = malloc(sizeof(uint32_t) * size);
  Primes* prime_array = malloc(sizeof(Primes));
  prime_array->_array = array;
  prime_array->_current_size = 0;
  prime_array->_memory_size = size;
  return prime_array;
}

void print(Primes* prime_array) {
  printf("-----\n");
  printf("We have an array containing %zi prime numbers "       \
         "(there is space for a total of %zi numbers)\n",
         prime_array->_current_size, prime_array->_memory_size);
  if (prime_array->_current_size) {
    printf("The prime numbers are:\n");
    for (size_t i=0; i < prime_array->_current_size; i++) {
      printf("%u ", prime_array->_array[i]);
    }
  }
  printf("\n-----\n");
}

size_t size(Primes* prime_array) {
  return prime_array->_current_size;
}

uint32_t get(Primes* prime_array, size_t position) {
  if (position >= prime_array->_current_size) {
    return 0;
  }
  return prime_array->_array[position];
}

void add(uint32_t prime, Primes* prime_array) {
  if (size(prime_array) >= prime_array->_memory_size){
    // current array size is too small: doubling it
    printf(">> realloc\n");
    size_t new_size = prime_array->_memory_size * 2;
    prime_array->_array = realloc(prime_array->_array,
                                  sizeof(uint32_t) * new_size);
    prime_array->_memory_size = new_size;
  }
  prime_array->_array[prime_array->_current_size] = prime;
  prime_array->_current_size++;
}

void free_primes(Primes* prime_array) {
  free(prime_array->_array);
  free(prime_array);
}
// ----------
// End of the implementation of the structure & functions
// ----------


/* First step */
bool is_dividable(uint32_t candidate, uint32_t divisor) {
  return (candidate%divisor == 0);
}

/* Second step */
bool is_prime(uint32_t candidate) {
  // first divisor is 2
  // (can't divide by 0, 1 universal divisor)
  for (uint32_t divisor = 2; divisor < candidate; divisor++) {
    if (is_dividable(candidate, divisor)) {
      return false;
    }
  }
  return true;
}

/* Third step */
void n_first_primes(size_t number) {
  printf("--------------------\n Basic\n");
  Primes* primes = init_primes(number);
  // first prime automatically added
  add(FIRST_PRIME, primes);

  uint32_t candidate = FIRST_PRIME+1;
  while (size(primes) < number) {
    if (is_prime(candidate)) {
      add(candidate, primes);
    }

    candidate++;
  }

  // print(primes);
  free_primes(primes);
}

/* Fourth step */

// 1 - candidate number

void n_first_primes_but_slightly_better(size_t number) {
  printf("--------------------\n Slightly better\n");
  Primes* primes = init_primes(number);
  add(FIRST_PRIME, primes);

  uint32_t candidate = FIRST_PRIME+1;
  while (size(primes) < number) {
    if (is_prime(candidate)) {
      add(candidate, primes);
    }

    // incrementing by 2, not 1
    // (testing only odd candidates)
    candidate += 2;
  }

  // print(primes);
  free_primes(primes);
}

// 2 - divisor number

bool is_prime_but_better(uint32_t candidate) {
  // only testing divisors <= integer square root of candidate
  for (uint32_t divisor = 2; divisor < isqrt(candidate); divisor++) {
    if (is_dividable(candidate, divisor)) {
      return false;
    }
  }
  return true;
}

void n_first_primes_but_really_better(size_t number) {
  printf("--------------------\n Really better\n");
  Primes* primes = init_primes(number);
  add(FIRST_PRIME, primes);

  uint32_t candidate = FIRST_PRIME+1;
  while (size(primes) < number) {
    if (is_prime_but_better(candidate)) {
      add(candidate, primes);
    }

    // we keep the optimisation of the previous step
    candidate += 2;
  }

  // print(primes);
  free_primes(primes);
}

// 3 - divisor number again

bool is_prime_ultimate(uint32_t candidate, Primes* existing_primes) {
  // only testing dividor which are primes themselves
  for (size_t divisor = 0; divisor < size(existing_primes); divisor++) {
    uint32_t current_prime = get(existing_primes, divisor);

    // we keep the optimisation of the previous step
    // N.B: this works only if existing_primes is sorted,
    // which IS the case by construction
    if (current_prime > isqrt(candidate)) {
      break;
    }

    if (is_dividable(candidate, current_prime)) {
      return false;
    }
  }
  return true;
}

void n_first_primes_ultimate(size_t number) {
  printf("--------------------\n Ultimate\n");
  Primes* primes = init_primes(number);
  add(FIRST_PRIME, primes);

  uint32_t candidate = FIRST_PRIME+1;
  while (size(primes) < number) {
    if (is_prime_ultimate(candidate, primes)) {
      add(candidate, primes);
    }

    candidate += 2;
  }

  // print(primes);
  free_primes(primes);
}


/* MAIN FUNCTION */

int main() {

  clock_t start;

  start = clock();
  n_first_primes(SOME_BIG_NUMBER);
  printf(">> Time spent in previous function: %fs\n",
         ((double) (clock() - start)) / CLOCKS_PER_SEC);

  start = clock();
  n_first_primes_but_slightly_better(SOME_BIG_NUMBER);
  printf(">> Time spent in previous function: %fs\n",
         ((double) (clock() - start)) / CLOCKS_PER_SEC);

  start = clock();
  n_first_primes_but_really_better(SOME_BIG_NUMBER);
  printf(">> Time spent in previous function: %fs\n",
         ((double) (clock() - start)) / CLOCKS_PER_SEC);

  start = clock();
  n_first_primes_ultimate(SOME_BIG_NUMBER);
  printf(">> Time spent in previous function: %fs\n",
         ((double) (clock() - start)) / CLOCKS_PER_SEC);

  return EXIT_SUCCESS;
}


/*

Tests results:

SOME_BIG_NUMBER                    |   10   |  100   | 10 000 | 1 000 000
-----------------------------------+--------+--------+--------+-----------
n_first_primes                     |0.000050|0.000164|1.977241| too slow
-----------------------------------+--------+--------+--------+-----------
n_first_primes_but_slightly_better |0.000032|0.000153|1.969338| too slow
-----------------------------------+--------+--------+--------+-----------
n_first_primes_but_really_better   |0.000011|0.000112|0.171883|250.818555
-----------------------------------+--------+--------+--------+-----------
n_first_primes_ultimate            |0.000014|0.000094|0.047139|40.887992
-----------------------------------+--------+--------+--------+-----------

 */
