#### A Rough idea of  $O \text{-notation , } \Omega \text{-notation , } \Theta \text{-notation}$ 

When we study the order of growth we study the **Asymptotic Analysis** that means study when input size is very high *(Limiting Value)* .
Even though we generally talk about the Runtime Asymptotic notation , these notation can be used for anything from space analysis or even functions that haven nothing to do with Algorithms

##### $O\text{-notation}$
This sets the upper bound  for the growth of function , in other words the function grows no faster then the upper limit eg:- if you cars top speed is 250 kmph , then we can be sure that under not circumstances the car would go faster than 250kmph . 

In terms of functions assume this:-
the function is $7n^3 + 8n + 5$ we can be sure that is doesn't grow faster than $n^3$ , hence 
the big O notation for running time for this is $O(n^3)$ , we can also see that this function doesn't grow faster than $n^4,n^5,n^6.......\text{and so on}$ so we can also say that $O(n^k) \text{ where } k \ge 3$ 

##### $\Omega \text{-notation}$ 
This sets a lower bound for the growth of function , in other words we can be sure that the function can grow at least more than the lower limit of the function or at least as fast as the lower limit of the function .
 for the same example we can say easily that the function grows at least $n^3$ , so we can say that the Omega notation for running time is $\Omega(n^3)$ and again we can clearly see that the function grows at least as fast as $n^2,n^1$ so we can say that $\Omega(n^k) \text{ where } k\le3$ .
##### $\Theta \text{-notation}$  
This sets a tight/precise bound for the asymptotic behavior of the function , or in other words it shows the rate of growth above a constant factor and below a certain constant factor ( they need not to be equal) .

$\text{if }O(f(n)) \text{ and } \Omega(f(n)) \text{ then } \Theta(f(n))$  
so for above example $\Theta(n^3)$ 

##### Rough Analysis of Insertion Sort 
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
$O(n^2)$ running time for the Algorithm can be understood as the inner loop runs $j-1$ times and and the outer loop runs $n-1$ times , this can be understood that the inner loop can run at most 
$(n-1)(n-1)$ times and as this is less that $n^2$ we can say that the 
$$
O(n^2) 
$$
we can also see that for the worst case the running time would be $\Omega(n^2)$ . this doesn't mean that after certain input size all would take at least $cn^2$ time as it is for specifically worst case condition 

to analyze the worst case lower bound of the algorithm , let's understand it this way . if the first n/3 large are at the first n/3 positions form `A[1:n/3]` and they need to reach the last n/3 positions `A[2n/3 + 1 : n]` they need to cross the middle n/3 elements . so atleast n/3 values must pass trough n/3 positions to be at final positions . and hence at least the executions would be 
$$
\frac{a}b \cdot \frac{a}b = \frac{n^2}9 \approx \Omega(n^2) 
$$
[Solutions to exercise 3.1](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter_3/exercise_solutions/section3.1)

#### Formal Definition for notations 
##### $O$-notation
the formal definition of $O-notation$ states the *asymptotic upper Bound* for the function 
$$
\begin{aligned}
O(g(n)) = \{f(n): & \text{there exists a positive constant c and }n_0 \text{ such that } \\                    &  0\le f(n) \le cg(n) \text{ for all } n\ge n_0 \}   
\end{aligned}
$$
![[Pasted image 20260109145112.png | 340]]
The definition of $O(g(n))$ requires that $f(n)$ is asymptotically non-negative (not negative for all values of n when ne is sufficiently large  ) . This means that $g(n)$ must also be non-negative
even tho $f(n)$  $\epsilon$ $O(g(n))$ but we still just denote it as $f(n)$  $=$ $O(g(n))$  .

we can see this clearly by example such as $4n^2 + 6000 = O(n^2)$ , 
$$
\begin{aligned}
	& \text{we know that } 4n^2 + 6000 \le cn^2 \\
	& \text{dividing both sides by } n^2 \\
	& = 4 + 6000/n^2 \le c \\
	&\text{the equality holds for } (n,c) = (1,6004)  
\end{aligned}
$$
we can also use this to disprove certain wrong notations  
$$
\begin{aligned}
	  &n^3 - 50n^2 = O(n^2) \\
	  &n^3 - 50n^2 \le cn^2 \\ 
	  &n - 50 \le c \\
	  &\text{no matter what value we choose for n > c + 50 , this equality will never hold } 
\end{aligned}
$$
