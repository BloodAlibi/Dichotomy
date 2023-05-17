# Dichotomy
Dichotomy is a Python template to find a number in a specific sorted list.
It uses the well known "Dichotomy" aglorithm.

## How it works

The function takes two arguments : the value you are searching for, and the __sorted__ list of numbers.
It returns True or False, depending on if the value is in the list or not, and its index if True.

Let's imagine the list to explain how this algorithm works. We are looking for 14.

- (STEP 1) : [1,3,6,8,12,14,20]

We'll start by dividing this list in two parts, and see if 14 is in the first or second side. By doing this, we remove a large part of useless numbers.
The middle is a whole number, equal to the right index and left index of this list divided by two. What are these ? They delimit the list we work with.
Let's visualise STEP 1 with the limits : [{1,3,6,8,12,14,20}], { and } being left and right.
- (STEP 2) : [{1,3,6,8,12,14,20}]

We found that the middle is equal to (len(t)+0)//2 = (7+0)//2 = 7//2 = 3
Now, we check if the middle value (of index 3) is the value we are searching for (14). It isn't, so the middle and everything before (smaller) is left untouched. We'll focus on the part bigger.
- (STEP 3) : [1,3,6,{8,12,14,20}]

We now do the same with the reduced list, of only four numbers.
- (STEP 4)

...
- (STEP n)

When the middle is equal to the number we are searching for, we stop and return the index of the middle value.
