

```python
#python auto assigns the correct data type to variable
x = 5
print(type(x))
```

##### Multiplication:- $x \times 2$  
```python
print(x*2)
```

##### Exponentiation:- $x^5$ 
```python
print(x**5)
```
*int* in python have arbitrary precision that means it can grow  beyond limit and python will adjust itself to avoid overflow 

```python
print(abs(-3))
import math
print(math.pow(x,5)) #power(x^5)
print(math.ceil(-3.2)) #cieling function
print(math.floor(3.2)) #floor function
print(math.comb(6,3)) # Combination (nCr)
x += 1   
print(x)  # Prints 
x *= 2
print(x)  # Prints 
y = 2.5
print(type(y)) # Prints "<type 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"
```
here `math.pow` returns an floating number always so it can lose precision very fast where as `x**5` avoids this 

##### Boolean Variables
```python
#boolean variable
t ,f = True , False 
a = 6
b = 3 
```

##### Logical and 
```python
print(t and f) #logical and
print(t != f) #logical XOR
```


```python
print(a and b) #prints 3
print(a or b) #prints 6
print(a != b) #prints 0 
```

In python , a non negative integer is treated as true , and logical operator performs short circuit evaluation . eg `a or b` as `a` is 6 , hence the logic  is true , so it directly return 6 without seeing or evaluating b 

```python
a = 7
b = 8
print(a & b) #bitwise and
```

Output:- 
```
0000 0111  (7)
& 0000 1000  (8)
-----------
  0000 0000  (0)
```


```python
print(a | b) #bitwise or
```

Output:-
```
0000 0111  (7)
| 0000 1000  (8)
-----------
  0000 1111  (8 + 4 + 2 + 1)
```

```python
print(~a) #bitwise NOT
``` 
**The Short Formula:** In Python, `~x` is always equal to **$-(x + 1)$**.

