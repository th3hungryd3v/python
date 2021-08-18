# A function that calls itself is a recursive function.
# It must have one or more base conditions that will stop the recursion to prevent infinite loops.
def rFib(n): # The beginning of our recursive function
    if n == 0: # Our first base condition
        return 0 # We return 0 if n == 0 and then the function is done
    elif n == 1 or n == 2: # Our second base condition
        return 1 # If n == 1 or 2, then return 1
    return rFib(n-1) + rFib(n-2) # As you can see, we have two recursive calls if n is not equal to 0, 2, or 1

"""
Using rFib(4) as an example:

Since 4 is not equal to 0, 2 or 1. It skips the two conditions that we wrote(if, elif), so the next block to run
will be the last return statement that includes 2 of our recursion calls(from left to right).

n == 4, so n-1 is equal to 3, and then for the second recursion call n is equal to 2,

so, for the first call it will have to run again which will now make n == 2, now a base condition is met,
so that will return 1 and the second recursion returns 1


"""