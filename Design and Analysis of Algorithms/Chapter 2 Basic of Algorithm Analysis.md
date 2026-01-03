***Sorting algorithms*** are used to take input a sequence of a number and sorts them in order 
`INPUT:` $\langle a_1 , a_2 , a_3, ......,a_n \rangle$  
`OUTPUT:` $\langle a_1^`,a_2^`,a_2^`......,a_n^` \rangle  \text{  where      }a_1^` \le a_2^` \le a_2^` \le ...... \le a_n^`$  

The numbers to be sorted are called ***keys*** . generally when we sort a compound data like a structure , then keys are called the attribute upon which the sorting is performed and the other associated data is called ***Satellite Data***  . key + satellite data is called record .
eg:- when we sort students on the basis of roll number , then roll no. is called key and the data like name , class etc associated with the roll no. are called satellite data 

We have many sorting algorithms 

#### Insertion sort   
This algorithm is efficient for sorting small number of elements . It is performed in same manner as we sort a deck of cards , we hold sorted cards in our left hand  and pick up cards by our right hand one by one , compare them to each card in left hand until we find the correct position and insert it once we find the correct position. 

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

##### Loop Invariants 
Loop invariants help us understand why an algorithm is correct . for loop invariant we need to show 3 things 
**Initialization :** It is true prior to the first iteration of the loop. 
**Maintenance :** If it is true before an iteration of the loop, it remains true before the next iteration. **Termination :** When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct. 

we can see in insertion sort that during start , subarray only has 1 element and hence that subarray is sorted ( Initialization ) , after each iteration when `i` points to element in `A[i]` then the subarray `A[1 : i-1]` is already sorted (Maintenance )  and after the loop terminates `i` will be equal to `length+1` which would make the subarray as `A[1 : length]` hence the entire subarray is sorted (Termination) 

**Q. 2.1-4**
Consider the problem of adding two $n$-bit binary integers, stored in two $n$-element arrays $A$ and $B$. The sum of the two integers should be stored in binary form in an $(n + 1)$-element array $C$. State the problem formally and write pseudocode for adding the two integers. [Solution](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter%202/exercises_solution/2.1-5)

>[!abstract] Selection sort 
>**Q. 2.2-2**  
Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in `A[1]`.  Then find the second smallest element of A, and exchange it with `A[2]`. Continue in this manner for the first `n-1` elements of A. Write pseudocode for this algorithm, which is known as selection sort.[Solution](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter%202/exercises_solution/2.2-2)

---

#### Introduction to Analysis of algorithm
Before analyzing the algorithm we need a model of the technology where the algorithm run . 
we assume it runs on generic uniprocessor system , on RAM model where instructions execute one by one and takes constant time  . we also needs to clarify the types of instructions for example there cannot be a instruction that sorts data in constant time , as it is not possible . common instructions are `add , subtract , mutliply , divide , remainder . floor` . We also assume the word of data has a limit on the number of bits , for example the input of size $n$  , the number of bits needed for the input are $c \log_2{n}  \text{ where } c\ge 1$ . due to this each word can hold the input and can be individually indexed . also the $c$ must be constant so that the word size doesn't grow to insane size ( if this happened we could have stored insane amount of data in single word and do operations on it in constant time  ) 

we also treat multiplying or computing  by $2^n$ as constant time operations as they can be operated in RAM by shifting the bits by n-units . 

Analyzing the algorithm based on *runtime* is stupid as it would vary language to language , computer by computer . so instead we see that how many times does it execute each line of code ( pseudocode ) .

*Input Size and it types* must also be taken into account , for simple algorithm like Insertion sort the input type can be integers but for other problems like multiplication it can be number of bits in output . for graphs it can be multiple items ( edge + vertex) . 

we assume the $k^{th}$ line takes constant $c_k$ time to execute . also when a loop runs $n$ times , the comparison inside loop happens $n+1$ times as 1 extra iteration is need for fail check of loop 

##### Analyzing Insertion sort 
![[Pasted image 20260102185439.png | 500]]
`pseudocode and it's time and cost`

Let the *total runtime* be $T(n)$ $$T(n) = c_1n  + c_2(n-1) + c_4(n-1) +c_5\sum_{i=2}^nt_i +  c_6\sum_{i=2}^n(t_i - 1) + c_7\sum_{i=2}^n(t_i - 1) + c_8(n-1)$$
this is the rigorous equation for run time , but we are interested in special cases like 
###### Best case 
where the algorithm is already sorted so the loop never runs and $t_i$ would be 1 
so $$\begin{aligned} 
T(n) &= c_1n  + c_2(n-1) + c_4(n-1) +c_5(n-1) + c_8(n-1) \\
     &= (c_1 + c_2 + c_4 + c_5 + c_8)n - (c_2 + c_4 + c_5 + c_8)  \\
     &= an+b				
\end{aligned}$$
in best case it is linear function 
###### Worst case 
where the algorithm is sorted in reverse order so each loop iteration runs it's maximum value $i$ 
$$\begin{aligned} 
T(n) &= c_1n  + c_2(n-1) + c_4(n-1) +c_5\sum_{i=2}^ni +  c_6\sum_{i=2}^n(i - 1) + c_7\sum_{i=2}^n(i - 1) + c_8(n-1) \\
	&= an^2 + bn + c
\end{aligned}$$
hence a quadratic functions 

We generally are interested in worst case as it established a *upper bound for the runtime* and we can be sure that algorithm would not take more than the worst case .

Sometimes we are  interested in the *average-case running* time of an algorithm; we also use the technique of *probabilistic analysis* applied to various algorithms . The scope of average-case analysis is limited, because it may not be apparent what constitutes an “average” input for a particular problem. Often, we shall assume that all inputs of a given size are equally likely. In practice, this assumption may be violated, but we can sometimes use a *randomized algorithm*, which makes random choices, to allow a probabilistic analysis and yield an *expected running time*

##### Order of growth 
we can see that in worst case the the function for insertion sort is quadratic . we can say that the function grows by the order $n^2$ , hence we consider only the leading term or the most significant term in growth of a function  . we also ignore the leading terms constant because for very large values of $n$ the constant is very insignificant 

To highlight the order of growth of running time we use notation $\Theta(n^2)$ we translates to "Roughly proportional to $n^2$ for large values of n " 

---
#### Designing Algorithm 

There are many different algorithm design techniques .  Insertion sort works using **Incremental Method** , another important technique is divide and conquer 

##### Divide & Conquer Method 

Divide and conquer works on the simple principle , dividing the current problem into a smaller sub-problem of similar nature ( Often by **Recursion**) , solve those sub-problems then combine their solution to get the complete solution . when the sub-problem is small enough , then the *base case* can be solved  directly without recursion.

##### Merge sort 
A simple and fast sorting algorithm of divide and conquer technique 
**Divide:** the subarray `A[p:r]` into subarray  `A[p:q]`  and `A[q+1:r]` where `q` is the midpoint of the array calculated using `p and r` 
**Conquer:** sort each of the subarray recursively using merge sort 
**Combine:** merging the subarray into the original array to get the complete answer 
When dividing if only 1 element is in subarray that means that array is already sorted , then we combine two such single element array in such a manner that combined array is sorted , then we return the sorted subarray and combine it with another such subarray and so on and on and on . until we reach back to the original array .
[The actual C code for MergeSort](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter%202/merge_sort)
```js
MERGE(A, p, q, r)
1  n_L = q - p + 1          // length of A[p:q]
2  n_R = r - q              // length of A[q + 1:r]
3  let L[0:n_L - 1] and R[0:n_R - 1] be new arrays
4  for i = 0 to n_L - 1     // copy A[p:q] into L[0:n_L - 1]
5     L[i] = A[p + i]
6  for j = 0 to n_R - 1     // copy A[q + 1:r] into R[0:n_R - 1]
7     R[j] = A[q + j + 1]
8  i = 0                    // i indexes the smallest remaining element in L
9  j = 0                    // j indexes the smallest remaining element in R
10 k = p                    // k indexes the location in A to fill
11 // As long as each of the arrays L and R contains an unmerged element,
   // copy the smallest unmerged element back into A[p:r].
12 while i < n_L and j < n_R
13    if L[i] ≤ R[j]
14       A[k] = L[i]
15       i = i + 1
16    else A[k] = R[j]
17       j = j + 1
18    k = k + 1
19 // Having gone through one of L and R entirely, copy the
   // remainder of the other to the end of A[p:r].
20 while i < n_L
21    A[k] = L[i]
22    i = i + 1
23    k = k + 1
24 while j < n_R
25    A[k] = R[j]
26    j = j + 1
27    k = k + 1 
```
`Pseudocode for Merge fucntion`
Merge function assumes that both the subarrays are already sorted individually (From their own iteration of recursive calls  to merge sort)
`Line 1 & 2:` calculating index(s) as per the subarray that have sorted nature 
`Line 3 to 7:` creating temporary arrays according to calculated index(s) and filling them from original arrays . now both temp arrays must be already sorted . 
`Line 11 to 17:` Merges the smallest unmerged element out of L and R back into the original array
Final loops just merge the remaining back into original array as both subarrays were already sorted so the remaining of the two would also be sorted and can be directly inserted 
>[!abstract] Merge runs in $\Theta(n)$
>here n = r - p + 1 
>![[Pasted image 20260103233846.png | 300]]
>because loops from 4 to 7 take $\Theta(n_l + n_r) = \Theta(n)$
 

![[Pasted image 20260103223131.png]]
`Example of Merge sort in action`
```python 
MERGE-SORT(A, p, r)
1   if p < r
2       q = ⌊(p + r) / 2⌋
3       MERGE-SORT(A, p, q)
4       MERGE-SORT(A, q + 1, r)
5       MERGE(A, p, q, r)
```
`Pseudocode for mergesort`
In the merge sort function we need to do only few things , calculate midpoint`(q)` , apply the same algorithm to both subarray according to midpoint , if p = r `or` p < r that would mean base case where only one element is in subarray and hence is already sorted so no need for anything . 
once both recursive merge-sort functions return we would have two sections in original array `A[p:r]`  that are sorted individually as `A[p:q] & A[q+1:r]`  and then we pass the the array entire along with the value of midpoint  to merge function to combine them both in sorted manner again . 

##### Analyzing Divide & Conquer Algorithm
When we analyze a recursive algorithm we use a **recurrence equation** . Let $T(n)$ be the worst time case on a problem of size $n$ . 
$$
\begin{aligned}
	& \text{when } n \text{ is small enough , } n<n_0 \text{ for some constant }n_0 \\
	& \text{then } T(n) = \Theta(1) \\
	& \\
	&\text{suppose the problem yeilds } a \text{ subproblems each of size } n/b \\
	&\text{so it takes } aT(\frac{n}b) \text{ and if D(n) is for divide and C(n) is   for combine then }\\
	& T(n) = D(n) + aT(\frac{n}b)+C(n)   
\end{aligned}
$$
so our final recurrence function  is 	
$$
T(n) = \begin{cases}
	\Theta(1) & \text{if } n < n_0\\
	D(n) + aT(\frac{n}b) + C(n) & \text{otherwise}
\end{cases}
$$
sometimes n/b might not produce equal size or isn't a integer . example $\lceil n/2 \rceil$ or $\lfloor n/2 \rfloor$ , since the difference between them is at most 1 so  for large values we can just ignore this and say n/2 

since divide is just calculating midpoint $D(n) = \Theta(1)$ , we recursively divide into 2 parts so we solve 2 subproblems always hence $2T(\frac{n}2)$ . and combining is just $\Theta(n)$ because merge is $\Theta(n)$ 

so $$
T(n) = 
\begin{cases} 
    c_1 & \text{if } n = 1, \\
    2T(n/2) + c_2 n & \text{if } n > 1,
\end{cases}
$$
now if we draw a recursion tree ,T(n) combine as $c_2n$ , further the divided T(n/2) will again be combined by $c_2n$ and so on   
![[Pasted image 20260103234409.png | 500]]
we can find the depth of the tree as 
$$
\begin{gather*} \text{tree ends when } n = 1 \\
\text{let that point be } i \\
\therefore \quad \frac{n}{2^i} = 1 \\
n = 2^i \\
\log_2 n = i
\end{gather*}
$$
hence $c_2n\cdot\log_2n$ 
so $\Theta(n\cdot\log_2n)$
