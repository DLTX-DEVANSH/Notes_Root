
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

#### Matrix Multiplication 
The normal iterative method uses the mathematical definition of  Matrix Multiplication that is $C = A\cdot B$
$$
c_{ij} = \sum_{k=1}^n a_{ik} \cdot b_{kj}
$$
if we take $\Theta(n^2)$ time to initialize the C matrix to 0 we can directly use the assignment 

```python
MATRIX-MULTIPLY(A, B, C, n)
1  for i = 1 to n                      
2      for j = 1 to n                  
3          for k = 1 to n
4              c_ij = c_ij + a_ik * b_kj    
```
as each loop runs n time , we have 3 such loops  and the time taken by line 4 to execute is constant we can conclude that running time of the algorithm is $\Theta(n^3)$
[Link to Source Code in C ](https://github.com/DLTX-DEVANSH/Algorithm-Design-/tree/main/chapter_4/matrixMultiply)


##### Divide and Conquer version 
we have a $n\times n$ matrix , but if we divide each matrix into 4 sub matracies 
 and compute them accordingly and recursively , we can use D&C to solve such problem so 
$$
 A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22}  \end{bmatrix}
\ , \ B=\begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22}  \end{bmatrix}
\ , \ C = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22}  \end{bmatrix}
$$
So we can compute the submatrices of C using these equations 
$$
\begin{aligned}
C_{11} &= A_{11} \cdot B_{11} + A_{12} \cdot B_{21}, \\
C_{12} &= A_{11} \cdot B_{12} + A_{12} \cdot B_{22}, \\
C_{21} &= A_{21} \cdot B_{11} + A_{22} \cdot B_{21}, \\
C_{22} &= A_{21} \cdot B_{12} + A_{22} \cdot B_{22}.
\end{aligned}
$$
and we can recursively go down the path until we reach a base case where the size of each matrix is 1 and we can directly multiply the components 
as $c_{ij} = a_{ik}\cdot b_{kj}$ 

```ruby
MATRIX-MULTIPLY-RECURSIVE(A, B, C, n)
1  if n == 1
2      // Base case.
3      c11 = c11 + a11 * b11
4      return
5  // Divide.
6  partition A, B, and C into n/2 x n/2 submatrices
       A11, A12, A21, A22; B11, B12, B21, B22;
       and C11, C12, C21, C22; respectively
7  // Conquer.
8  MATRIX-MULTIPLY-RECURSIVE(A11, B11, C11, n/2)
9  MATRIX-MULTIPLY-RECURSIVE(A11, B12, C12, n/2)
10 MATRIX-MULTIPLY-RECURSIVE(A21, B11, C21, n/2)
11 MATRIX-MULTIPLY-RECURSIVE(A21, B12, C22, n/2)
12 MATRIX-MULTIPLY-RECURSIVE(A12, B21, C11, n/2)
13 MATRIX-MULTIPLY-RECURSIVE(A12, B22, C12, n/2)
14 MATRIX-MULTIPLY-RECURSIVE(A22, B21, C21, n/2)
15 MATRIX-MULTIPLY-RECURSIVE(A22, B22, C22, n/2)
```
This is when assuming that all the matrices are square and the size of the dimension is an exact power of 2 .
