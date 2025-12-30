### Algorithms

***Algorithms*** is a well defined computational procedure / steps that gives the same output for some input 
![[Pasted image 20251228034522.png | 400]]

***Instance*** of a problem is a specific input that follows all conditions of a problem eg :- for an algorithm that sorts prime number $\langle 3,5,23,11,17\rangle$ is a valid instance but $\langle3,5,23,11,8\rangle$ is not a valid instance as 8 is not a prime number 

A correct algorithm is expected to **stop(halt)** when the correct output is ready in **finite time**

> [!caution] Note
> sometimes incorrect algorithms are also useful if we manage their error %

***NP-complete Algorithms*** are algorithms which have no proven algorithms that work 'or' end in real time . NP complete problems have property that if any one NP-complete solutions is found then all possible NP-complete problems must have a solution eg :-
##### Travelling salesman problem
Imagine you are planning a road trip to visit 15 different cities. You want to visit every city exactly once and finish back at home, using the least amount of gas possible.

This is **NP-Complete** because the number of possible routes explodes uncontrollably as you add cities. With just 15 cities, you have billions of routes to compare; with 60, there are more routes than atoms in the universe. It is extremely fast to calculate the length of _one_ specific route (verification), but impossible for even a supercomputer to check _all_ of them to guarantee it found the absolute best one (solution). It is classified as **NP-Complete** because the number of possible routes grows factorially ($n!$) as you add cities, making it computationally impossible to check every combination for large inputs.

![[travelling_salesman_problem.png | 500]]
***Online Algorithms*** are those algorithms whose data / inputs arrive overtime instead of start 
>[!faq] Why multiple algorithms for same problem? 
>Efficiency e.g: -  
insertion sort takes $c_1 n^2$ seconds { $c_1$ is a constant }
merge sort takes $c_2n \cdot \log_{2} n$ seconds 
now we want to sort $10^8$ numbers { $\approx$ 1GB} and let's say insertion sort is done on computer with $10^{10}$ instructions / second *{fastest supercomputer}* by a genius  programmer that makes $c_1 = 2$ & Merge sort is done on the computer with $10^7$ instructions / second *{basic computer}* by an idiot programmer that makes $c_2 = 50$ 
>>so Insertion sort $\implies$ $$\frac{2 \cdot (10^8)^2}{10^{10}} \text{seconds } \approx \text{ 23 Days}$$
>>merge sort $\implies$ $$\frac{50 \cdot (10^8)^2 \cdot \log_2 10^8}{10^7} \text{seconds } \approx \text{ 5 hours} $$
>So even with all the advantages , a bad algorithms is slower 

![[Pasted image 20251228042510.png | 600]]
###### [[Index |Backlink to main Index]] 


