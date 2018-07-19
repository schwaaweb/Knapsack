import time

def nth_fib_first_pass(n):
    if n < 2:
        return n
    return nth_fib_first_pass(n-1) + nth_fib_first_pass(n-2)


def print_fibs(m):
    start_of_loopi = time.time()
    fibonacci = nth_fib_first_pass(m)
    fib_time = time.time() - start_of_loopi
    print("%3d : %13.9f :: %d  " % (m , fib_time, fibonacci))

start_of_execution = time.time()
print(time.strftime("\n %H:%M:%S %a %b %d %Y\n"))

for a in range(35):
    start_of_loop = time.time()
    print_fibs(a)
    #start_of_loop = time.time()
print('\n %8.4f secs.\n' % (time.time() - start_of_execution)) 


### Memoization
"""

 Memoized Recursive Strategy 
  
  The idea: we'll use the same naive recursive logic but augment it 
  with the ability to save work we've already done. This doesn't actually
  improve the theoretical runtime complexity over the naive recursive 
  approach, but it does significantly improve the actual running time.
  
  1. Initialize a cache (can be a list or dictionary)
  2. Write a helper function that checks the cache for the answer we're looking for
  3. If the answer is not found, fall back on our naive logic
  4. The naive helper needs to recursively call the memoized version, not itself
  5. Return the value that the memoized helper function finds

"""

def nth_fib_second_pass(n):
    cache = {}

    def nth_fib_memo_helper(n):
        if n not in cache.keys():
            cache[n] = nth_fib_first_pass_helper(n)
        return cache[n]

    def nth_fib_first_pass_helper(n):
        print(n) #*#
        if n < 2:
            return n
        return nth_fib_memo_helper(n - 1) + nth_fib_memo_helper(n - 2)

    return nth_fib_memo_helper(n)
#print(nth_fib_second_pass(25))

"""
Bottom-Up Iterative

The idea: Generally follow the sam logic as the memoised recuresive approach. 
We still make use of a cache to save prior data. In this case thoughj, wee seed the cache with some initial values an then loop up to our input, along the way
populationg the cache with the anser for the curren iteration.

1. Initialize a cache
2. See the cach with initial values (these are essentially the base case values
form the recuresive approaches)
3. Loop up to our input
4. Populate the caache with the answer for the curren iteration
5. Return cache[n]


 """

def nth_fib_third_pass(n):
    cache = {}
    # seed it with the initial values
    cache[0] = 0
    cache[1] = 1
    # loop from 2 up to n
    for i in range(2, n + 1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

#print(nth_fib_third_pass(100))





    
