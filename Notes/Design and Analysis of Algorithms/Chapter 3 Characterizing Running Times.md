#### A Rough idea of  $O \text{-notation , } \Omega \text{-notation , } \Theta \text{-notation}$ 

When we study the order of growth we study the **Asymptotic Analysis** that means study when input size is very high *(Limiting Value)* .
Even though we generally talk about the Runtime Asymptotic notation , these notation can be used for anything from space analysis or even functions that haven nothing to do with Algorithms

##### $O\text{-notation}$
This sets the upper bound  for the growth of function , in other words the function grows no faster then the upper limit eg:- if you cars top speed is 250 kmph , then we can be sure that under no circumstances the car would go faster than 250kmph . 

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

--- 
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
	  & n^3 - 50n^2 = O(n^2) \\
	  & n^3 - 50n^2 \le cn^2 \\ 
	  & n - 50 \le c \\
	  &\text{no matter what value we choose for n > c + 50 , this equality will never hold } \\
	  & \text{if } n = c + k , k > 50 \\
	  & c +k - 50 \le c \\
	  & k \le 50 \text{ this makes are assumptions wrong and hence not possible}
\end{aligned}
$$
##### $\Omega-notation$ 
$\Omega-notation$ provides a *lower asymptotic bound* for the function
$$
\begin{aligned}
\Omega(g(n)) = \{f(n): & \text{there exists a positive constant c and }n_0 \text{ such that } \\                    &  0\le cg(n) \le f(n) \text{ for all } n\ge n_0 \}   
\end{aligned}
$$
![[Pasted image 20260110131405.png |300]]
eg:- if $n^2/100 -100n -500 =\Omega(n^2)$ 
$$
\begin{aligned}
	&\frac{n^2}{100} - 100n - 500 \ge cn^2\\
	&\frac{1}{100} - \frac{100}n - \frac{500}{n^2} \ge c \\
	\\
	&\text{now if we take values of (n,c) like :- (10005 , }2.49 \times10^{-9}) \text{ this equailty holds } 
\end{aligned}
$$
##### $\Theta-notation$
This gives the *Asymptotic Tight Bound* for a function 
$$
\begin{aligned}
	\Theta(g(n)) = \{ f(n):&\text{ there exists postitive constant }c_1,c_2,n_o \text{ such that} \\
	&0\le c_1g(n) \le f(n) \le c_2g(n) \text{ for all } n \ge n_o \} 
\end{aligned}
$$
![[Pasted image 20260110132847.png | 300]]

###### Equivalence theorem for Big-Theta
**Theorem:** For any two strictly positive functions $f(n)$ and $g(n)$, we have $f(n)=\Theta(g(n))$ if and only if $f(n) = \Omega(g(n))$ and $f(n) = O(g(n))$ 
[proof]()

###### Precise use of notation 
when using notations we have to extremely precise as the notations lose any form of significance if a detail is missed in stating them . for example saying insertion sorts running time is $\Theta(n^2)$ makes no sense as in best case scenario it takes $\Theta(n)$ so without specifying what case , the notation is meaningless . we can say $O(n^2)$ for all cases , which is true as even it worst case it goes till $n^2$ but again won't be that useful , same way we can say $\Omega(n)$ for all cases as even in best case it would take at least $n$ .  

Same way if there is a function $3n^2 + 5n + 20$ saying that for worst case the running time is $O(n^4)$ will be correct ( look at our definition ) but it wont be useful , it is like saying a truck will run at most as fast as a bullet train , yeah it is true that it will always run slower than train maybe equal to it ( in imagination ofc) but not more than that , still it doesn't tell us anything about the trucks actual speed .  

##### Notations in equations and inequalities 
we know that   $f(n) = O(n)$ means  $f(n) \ \ \epsilon \ \ O(n)$ . but what if we have a weird equation like $4n^2 + 6n -2 =4n^2 +\Theta(n)$  . what does it mean ? in such case it means that there $4n^2 + 6n -2 =4n^2 + g(n)$ where $g(n) \ \ \epsilon \ \ O(n)$  , just that g(n) is not important enough in comparison to rest of the equation or not we don't care enough to write it's name

what if a notation comes in left hand side , $n^2 +\Theta(n) = \Theta(n^2)$ this simply means that the right hand side must be able to be denoted in the notation that will make the equation valid . 
eg:- $2n^2 + f(n) = g(n) \text{ ,where }g(n) \ \epsilon \ \Theta(n^2)$  . basically saying that right hand side always provides a rougher detail about the function/algorithm 
so it becomes $2n^2 + 50n + 6 \ = \ 2n^2 + \Theta(n) = \Theta(n^2)$ 

##### Weird nuances in notations 
when we use a asymptotic notation , it is pretty clear that with respect to which variable are we studying . if we say $\Theta(g(n))$ we are studying the growth of $g(n)$ wrt to $n \to \infty$ . but when we talk about constant time , it is pretty difficult to guess which variable goes to $\infty$ .
in this case to lessen the ambiguity we generally look for the context to make it clear which variable tend to $\infty$ . example $f(n) = O(1)$ shows the $n \to \infty$ .

another weird issue is with recurrences . take a look 
$T(n) = O(1) \text{ for } n<3$ . okay ? we know that $T(n) \le constant, \text{ for some } n>n_0$  but if that $n_0$ is 3 then what ? we wanted to say that $T(n)$ is less than some constant when n < 3 but now by the definition of big-O notation , it is not possible  .
To get rid of such ambiguity we explicitly say $T(n) \le constant \text{ for some }n>n_0$ 

We also directly say $f(n) \ \epsilon \ \Theta(g(n))$ even when the inputs are not continuous , like an algorithm that takes only inputs of size $2^n$ , in such cases we generally  assume or know that  it holds for the domain of $f(n)$ . 

##### o-notation (little-oh)
O-notation may or may not be asymptotically tight . $2n^2 = O(n^2)$ is asymptotically tight but $5n = O(n^2)$ is not asymptotically tight . we define little o as a upper bound function that is definitely not asymptotically tight . 
$$
\begin{aligned}
o(g(n)) = \{f(n): & \text{for any positive constant  c and }n_0 \text{ such that } \\                    &  0\le f(n) < cg(n) \text{ for all } n\ge n_0 \}   
\end{aligned}
$$
**Note:** unlike big-O , little o needs to be defined for *every constant c*
so $2n = o(n^2) \ \ but \ \ 2n^2\neq o(n^2)$ 
$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0 
$$
as $f(n)<c.g(n)$ for all c > 0 hence g(n) must be of different order (higher than f(n) ) . hence 
$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0 
$$
##### $\omega-notation$ (little omega)
similarly to small o , little omega give lower bound that is definitely not asymptotically tight
$$
\begin{aligned}
\omega(g(n)) = \{f(n): & \text{for any constant c and }n_0 \text{ such that } \\                    &  0\le cg(n) < f(n) \text{ for all } n\ge n_0 \}   
\end{aligned}
$$
and by same logic 
$$
\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty 
$$
----
#### Mathematical Functions 

##### Monotonicity 
 A function is said to be monotonically increasing  if $f(m) \ge g(n)$ if $m \ge n$ 
 >[!note] Explanation of Equality 
 >the reason why we include equality in the above equation for $m \ge n$ is that due to *HemoIsoMorphism* of the function . which means that for any two different values m and n , the equality may or may not hold ( the slop becomes 0 and graph flatlines ) but even if the values of m and n are equal then by common sense the graph will be equal . but just to give the full picture that m = n wiil also hold the equality true , we write it as $m \ge n$ 
 >formally this is written as "The entire  domain maps to Range  of function "
 >

##### Strictly Increasing functions 

A function is said to be strictly increasing if 
$$
\begin{aligned}
	&f(m)>g(n) \text{  ,  if } m> n
\end{aligned}
$$
*The graph of the function cannot flat line in any case*

##### Floor and ceiling functions 

*Floor* of a x denotes the integer value lower or equal to x 
intuitively $\lfloor x \rfloor = x - \{x\}$ where {x} denotes the GIF of the function 

*ceiling* of a x denotes the the integer value just grater or equal to x 
intuitively $\lceil x \rceil = x + 1 - \{ x \}$  

###### The general Inequalilty is 
$$
x - 1 < \lfloor x \rfloor \le x \le \lceil x \rceil < x + 1
$$
###### Reflective Property 
$$
\begin{aligned}
-\lfloor x \rfloor &= \lceil -x \rceil \\
-\lceil x \rceil &= \lfloor -x \rfloor
\end{aligned}
$$
###### Nested Division with bounds 
$$
\begin{aligned}
\left\lfloor \frac{\lfloor x/a \rfloor}{b} \right\rfloor &= \left\lfloor \frac{x}{ab} \right\rfloor \\[10pt]
\left\lceil \frac{\lceil x/a \rceil}{b} \right\rceil &= \left\lceil \frac{x}{ab} \right\rceil \\[10pt]
\left\lceil \frac{a}{b} \right\rceil &\le \frac{a + (b-1)}{b} \\[10pt]
\left\lfloor \frac{a}{b} \right\rfloor &\ge \frac{a - (b-1)}{b}
\end{aligned}
$$
###### Integer Translation 
$$
\begin{aligned}
\lfloor n + x \rfloor &= n + \lfloor x \rfloor \\
\lceil n + x \rceil &= n + \lceil x \rceil
\end{aligned}
$$

---
----
##### Modular Arithmetic
modular arithmetic means focusing on the remainder of the division 
$$
a \ mod \ n = a - n\lfloor \frac{a}n \rfloor
$$
proof 
$$
\begin{aligned}
	& Q = q\cdot n + r \\
	& r = Q - n\cdot q\\
	& r = Q - n \lfloor \frac{Q}{n} \rfloor
\end{aligned}
$$
Equivalency in mod:-   $a\  mod \ n = b \ mod \ n$ then $(a=b) \ mod \ n$. This means that the remainder of 2 numbers is equal not that both numbers are equal 

---
----
##### Polynomial
Polynomial in of degree d is a fucntion $p(n)$ 
$$
\sum_{i=0}^d a_i \cdot n^i 
$$
where $a_d \neq 0$ 

The Asymptotic running bound for p(n) is $p(n) = \Theta(n^d)$
$$
\begin{align*}
% Definition
P(n) &= \sum_{i=0}^{d} a_i n^i \\
\\
% Big O Proof
\text{1. Proof for } O(n^d): \\
0 &\le P(n) \le c \cdot n^d \\
a_0 + a_1 n + a_2 n^2 + \dots + a_d n^d &\le c \cdot n^d \\
\text{Divide by } n^d: \quad \frac{a_0}{n^d} + \frac{a_1}{n^{d-1}} + \dots + \frac{a_{d-1}}{n} + a_d &\le c \\
\text{Choose constants: } (c, n_0) &= \left( \sum_{i=0}^d a_i, 1 \right) \\
\\
% Big Omega Proof
\text{2. Proof for } \Omega(n^d): \\
0 \le c \cdot g(n) = c \cdot n^d &\le a_0 + a_1 n + \dots + a_d n^d \\
c &\le \frac{a_0}{n^d} + \dots + a_d \\
\text{Choose constants: } (c, n_0) &= (a_d, 0) \\
\\
% Conclusion
\therefore \text{By equivalence theorem: } P(n) &= \Theta(n^d)
\end{align*}
$$
----
----

##### Exponential 

$$
e^x = \sum_{i=0}^\infty \frac{x^i}{i!} 
$$
We also have the inequality 
$$
1 + x \le e^x 
$$
When $|x| \le 1$ we have the approximation 
$$
1 + x \le e^x \le  1 + x + x^2 
$$
but when $x \to 0$ we can approximate it to 
$$
e^x = 1 + x + \Theta(x^2)
$$
when $x \to \infty$ we use approximation 
$$
\lim_{n \to \infty} (1 + \frac{x}n)^n = e^x
$$
for ln(x+1)
$$
\ln(1+x) = \sum_{i=1}^\infty (-1)^{2+1} \frac{x^i}i
$$
we also have a inequality for $x > -1$
$$
\frac{x}{1+x} \le \ln(1+x) \le x
$$
we say a function is *polylogarithmically* bounded if $f(n) = O(\lg^k n)$   

----
----
##### Factorial 
$$
n! = \begin{cases} 
  1 & \text{if } n =0\\
  n\cdot (n-1)! & \text{if } n > 0
\end{cases}
$$
###### Sterling's Approximation 
$$
n! = \sqrt{n \pi n} (\frac{n}e)^n (1 + \Theta(\frac{1}n) 
$$

$$
\begin{aligned}
& n! = o(n^n) \\
& n! = \omega(2^n) \\
& \lg(n!) = \Theta(n\cdot lgn)
\end{aligned}
$$
---
---
##### Functional iteration 
$f^{(i)}(n)$ to denote the function $f(n)$ iteratively applied i times until a base case of value $n$ is reached  
$$
f^{(i)}(n) = \begin{cases}
	n & \text{if } i =0 \\
	f(f^{(i-1)}(n))& \text{if  } i >0	
\end{cases}
$$
---
----
##### Iterated Logarithm function 
the term $lg^* n$ to denote the iterated logarithm function . as $lg^{(i)} n$ is only defined for non-negative values $lg^{(i)} n > 0$

$lg^* n = min\{i \ge 0:lg^{(i)} n \le 1\}$
where $lg^* n$ is the smallest integer $i$ such that applying the logarithm $i$ times result in a value becoming $\le 1$ 
Example:-
$$
\begin{aligned}
 &lg^* 16 = 3 \\
  &\text{as } lg(lg(lg(16))) = 1
\end{aligned}
$$


 