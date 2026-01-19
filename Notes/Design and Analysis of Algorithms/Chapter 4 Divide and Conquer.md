
#### Introduction to Divide and Conquer and Mathematics 
Divide and Conquer is the strategy of designing powerful asymptotically efficient algorithm where we 
**Divide:** The problem into subproblems ( often recursively ) that are smaller instance of the original problem 
**Conquer:** Solve the the subproblems recursively 
**Combine:** Combine the solved subproblems to get the solution to original solution 

If the problem is small enough ***(Base Case)*** then the problem can be solved without recursion , otherwise the recursive case runs 

When the recursion can be solved directly the when we say that the recursion has **bottomed out**

###### Recurrence 
A recurrence is a equation that describes itself in form of its own value when given a different input ( generally smaller ) .
In a Recurrence if the the function invokes itself recursively than it is recursive case , otherwise its the base case .
 The recurrence is **well defined** if there exists atleast one function that satisfies it , otherwise it is **ill-defined** 

##### Algorithmic Recurrence
A recurrence $T(n)$ is **algorithmic** if for a sufficiently large **threshold** constant $n_0 > n$ it hold two properties 
1) for all $n<n_0$  we have $T(n) = \Theta(1)$ 
2) for all $n \ge n_0$ every path of recursion terminates terminates at a base case in finites number of recursive iterations 
###### Explanation of $1^{st}$ property 
when we study the running time an algorithm we are interested in $n\ge n_0$
(for large inputs) . but this math doesn't hold properly when $n<n_0$ . but if we assume the value of $n_0$ to be constant that is large enough , as the number of inputs $<n_0$ are finite we can find the value of n for which it takes the maximum amount of time and call it finite maximum time  $c_2$ , similarly we define the smallest value $c_1$ which is the minimum time for calling the function and returning it . 
and hence $0 \le c_1 \le T(n) \le c_2 \ \ \  \text{    for  }n<n_0$    
###### Explanation of $2^{nd}$ property 
simply means if any recursive path does not terminate in base case , it would result in infinite loop 

##### Methods of solving recurrence
- **Substitution Method**
- **Recursion Tree Method**
- **Master Theorem**
	- Simple Master Theorem
	- Continuous master theorem
- **Akra-Bazzi Method**

----
