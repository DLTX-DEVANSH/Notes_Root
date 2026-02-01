#### Project 1: The "Manual" Combinatorics (Easy)

**Goal:** Verify `math.comb` behavior using basic arithmetic operators.

**The Task:**
1. Define two variables, `n = 10` and `k = 3`.
2. Calculate ${n \choose k}$ using `math.comb(n, k)` and store it in `res_lib`.
3. Calculate ${n \choose k}$ _manually_ using the formula $\frac{n(n-1)(n-2)}{3 \times 2 \times 1}$ (hardcode the expansion for $k=3$ using `*` and `/`). Store this in `res_manual`.
4. Print the type of both results.
    
    **The Test:** One will likely be a `float` and one an `int`. Why? (Hint: Division `/` in Python always returns a float, even if clean).

#### Project 2: The Boolean Mask (Medium)
**Goal:** Master the "Booleans are Integers" quirk to write "branchless" code
**The Task:**
You are building a rudimentary data filter. You have a value `score = 50`.
1. Create a boolean `is_passing = score > 40`
2. Create a boolean `is_perfect = score == 100`.
3. Calculate a `final_bonus` variable using **only** math operators (`+`, `*`) and the booleans. 
    - Rule: If they pass, they get 10 bonus points. If they are perfect, they get 50 bonus points (stacking).
    - _Restriction:_ No `if` statements allowed.
        **The "Why":** In Data Science (Pandas/NumPy), we often multiply data arrays by boolean masks to zero-out invalid data without loops.
#### Project 3: The Precision Assassin (Hard)

**Goal:** expose the danger of `math.pow` vs `**` for large numbers (Cryptography/Number Theory context).
**The Task:**
1. Set `base = 10` and `exp = 308` (Just at the edge of `float64` limits).
2. Calculate `a = base ** exp` (Integer math).
3. Calculate `b = math.pow(base, exp)` (Float math) and cast it to `int(b)`.
4. Print `a - b`.
5. Now change `exp` to `309`. Observe what happens to `b` (it might become `inf`) vs `a`.
    **The "Why":** This proves why you **never** use `math.pow` for RSA/Cryptography or Project Euler problems in Python. You will lose data or crash due to 64-bit float overflows, while Python's native `int` could theoretically handle exponents that fill your entire RAM.