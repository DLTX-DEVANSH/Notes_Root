***Sorting algorithms*** are used to take input a sequence of a number and sorts them in order 
`INPUT:` $\langle a_1 , a_2 , a_3, ......,a_n \rangle$  
`OUTPUT:` $\langle a_1^`,a_2^`,a_2^`......,a_n^` \rangle  \text{  where      }a_1^` \le a_2^` \le a_2^` \le ...... \le a_n^`$  

The numbers to be sorted are called ***keys*** . generally when we sort a compound data like a structure , then keys are called the attribute upon which the sorting is performed and the other associated data is called ***Satellite Data***  . key + satellite data is called record .
eg:- when we sort students on the basis of roll number , then roll no. is called key and the data like name , class etc associated with the roll no. are called satellite data 

We have many sorting algorithms 

##### Insertion sort   
This algorithm is efficient for sorting small number of elements . It is performed in same manner as we sort a deck of cards , we hold sorted cards in our left hand  and pick up cards by our right hand one by one , compare them to each card in left hand until we find the correct position and insert it once we find the correct position . 

`pseudo code for algorithm` 
```python
INSERTION-SORT(A)
    for j = 2 to A.length
        key = A[j]                     #Element to be inserted
        i = j - 1                      #Last index of the sorted portion
        
        # Shift elements greater than key one position to the right
        while i > 0 and A[i] > key
            A[i + 1] = A[i]
            i = i - 1
        
        # Place key in its correct position
        A[i + 1] = key
```
[Link to correct source code in C ](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter%202/Insertion_sort)
when `i` points to a element then the sub array `A[1 : i-1]` that is already sorted , then we compare the element `A[i]` by each element in sub array and find the correct spot and insert the value . this loop continues until entire array is sorted . 
![[Pasted image 20251228185737.png]]

####  *Loop Invariants* 
Loop invariants help us understand why an algorithm is correct . for loop invariant we need to show 3 things 
**Initialization :** It is true prior to the first iteration of the loop. 
**Maintenance :** If it is true before an iteration of the loop, it remains true before the next iteration. **Termination :** When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct. 

we can see in insertion sort that during start , subarray only has 1 element and hence that subarray is sorted ( Initialization ) , after each iteration when `i` points to element in `A[i]` then the subarray `A[1 : i-1]` is already sorted (Maintenance )  and after the loop terminates `i` will be equal to `length+1` which would make the subarray as `A[1 : length]` hence the entire subarray is sorted (Termination) 

**Q. 2.1-4**
Consider the problem of adding two $n$-bit binary integers, stored in two $n$-element arrays $A$ and $B$. The sum of the two integers should be stored in binary form in an $(n + 1)$-element array $C$. State the problem formally and write pseudocode for adding the two integers. [Solution](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter%202/exercises_solution/2.1-5)
