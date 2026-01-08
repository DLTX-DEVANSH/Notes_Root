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
