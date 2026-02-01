Modern computers store and process information in single binary digits called **bits**  which work on *base-2* instead of *base-10* like Hindu-Arabic numbers . 

The Integer arithmetic used by computers follow almost the same properties as normal arithmetic eg:- $20 + 40 +50 = (20 + 40) +50 = 20 + (40 +50)$ 
But when it comes to floating point number , a lot of standard logic fails due to how floating point numbers are stored and processed eg:- 
$$
\begin{aligned}
& \text{on most computers  } 3.14 + (10^{20} - 10^{20}) = 0 \\
& \text{but  } (3.14 + 10^{20}) - 10^{20} 
\end{aligned}
$$
this is due to rounding of floating point numbers 

---
---
#### Introduction to low level Information storage 
generally computers do not store data in byte , but in **Bytes** where 1 Byte = 8 bits . The machine level code does not see the actual memory locations but sees it as a vary large array of bytes called **virtual memory** . where location of a particular data  is Identified by their *address* , and set of all such addresses is called **virtual address space** . example in C a pointer that points to regardless of data type  , stores the virtual address . The C compiler associates the data type with the pointer so that the machine code knows what to interpret the data as . 

##### Hexa-Decimal Notation 
The values of from a byte ranges from $00000000_2$ to $11111111_2$   and  in decimal $0_{10}$ to $225_{10}$ 
both of these notation are not good , binary notation is to lengthy and decimal is inconvenient to convert . 
So we use a different form called hexadecimal ranging from $0_{16}$ to $F_{16}$ . in C we represent them using 0x or 0X . we can both upper case or lowercase alphabets (or even mixed) 
![[Pasted image 20260124160449.png | 500]]

We can convert the hex value from binary  value by simply writing the corresponding hex value of each decimal value 
eg:- convert  0x173A4C
![[Pasted image 20260124164758.png | 500]]

similarly
 Decimal to Hexadecimal (Repeated Division)

To convert a decimal number to hex, divide the number by **16** repeatedly and track the remainders. The hex value is read from the **bottom (last remainder) to the top (first remainder)**.

###### Example: Convert $188_{10}$ to Hex

1. $188 \div 16 = 11$ remainder **12** (which is **C** in hex)
    
2. $11 \div 16 = 0$ remainder **11** (which is **B** in hex)
    

**Result:** Reading bottom to top, $188_{10} = \text{0xBC}$

 Hexadecimal to Decimal (Positional Weight)

To convert hex to decimal, multiply each digit by $16^n$, where $n$ is the position of the digit (starting from 0 on the right).

Example: Convert $\text{0x2F5}$ to Decimal

Break the hex string into individual digits and multiply by the power of 16:

$$\begin{aligned} \text{Value} &= (2 \times 16^2) + (F \times 16^1) + (5 \times 16^0) \\ \text{Value} &= (2 \times 256) + (15 \times 16) + (5 \times 1) \\ \text{Value} &= 512 + 240 + 5 \\ \text{Value} &= 757_{10} \end{aligned}$$
###### How Subtraction Works in Hex

**Example:** $4b_{16} - d_{16}$

$$
\begin{aligned}
&= 40_{16} + b_{16} - d_{16} \\
&= 30_{16} + 10_{16} + b_{16} - d_{16} \quad \text{(Borrowing } 10_{16} \text{ from } 40_{16}\text{)} \\
&= 30_{16} + b_{16} + 10_{16} - d_{16} \\
&= 3b_{16} + 3_{16} \quad \quad \quad \quad \quad \text{(Since } 10_{16} - d_{16} = 16 - 13 = 3 \text{)} \\
&= 3e_{16} \quad \quad \quad \quad \quad \quad \quad \text{(Since } b_{16} + 3_{16} = 11 + 3 = 14 = e \text{)} \\
&= \text{0x3E}
\end{aligned}
$$
----
##### Data Sizes
###### 1. What is "Word Size"?

In computing, a **word** is the natural unit of data used by a processor. The **word size** (typically 32-bit or 64-bit) determines the size of the "pointers" (the variables that hold memory addresses).

Because the word size dictates the size of a pointer, it determines the absolute maximum amount of RAM (Virtual Address Space) a program can access:

- **32-bit word size:** The max memory address is $2^{32} - 1$. This limits the program to accessing at most **4 Gigabytes (GB)** of memory.
    
- **64-bit word size:** The max memory address is $2^{64} - 1$. This allows access to **16 Exabytes (EB)** of memory (which is practically infinite for today's standards).
    

###### 2. 32-bit vs. 64-bit is about the _Program_, not just the Machine

Modern 64-bit computers have "backward compatibility," meaning they can run older 32-bit software. Therefore, whether a program is "32-bit" or "64-bit" depends on **how it was compiled**, not the hardware it runs on.

- `gcc -m32 prog.c` creates a 32-bit program (4GB limit, even on a 64-bit PC).
    
- `gcc -m64 prog.c` creates a 64-bit program (only runs on 64-bit PCs).
    

###### 3. How C Data Types Change Size

In C, the size of basic data types isn't strictly fixed; it changes depending on whether you compile for 32-bit or 64-bit.


- `char` (1 byte), `short` (2 bytes), `int` (4 bytes), `float` (4 bytes), and `double` (8 bytes) **stay the same size** in both 32-bit and 64-bit programs.
    
- `long` **changes size**: It is 4 bytes in 32-bit, but 8 bytes in 64-bit.
    
- **Pointers** (e.g., `char *`) **change size**: They are 4 bytes in 32-bit, but 8 bytes in 64-bit.
    

###### 4. The "Fixed-Size" Solution

Because sizes change between systems, C99 introduced "fixed-size" data types to give programmers guarantees. If you use `int32_t`, you are guaranteed exactly 4 bytes. If you use `int64_t`, you are guaranteed exactly 8 bytes, regardless of the system.

###### 5. The "Portability Trap" (Bugs in Migration)
a common bug that occurred when the world shifted from 32-bit to 64-bit computers around 2010.

On a 32-bit system, an `int` (4 bytes) and a pointer (4 bytes) are the same size. Lazy programmers used to store memory addresses inside `int` variables.

However, when you re-compile that code for a 64-bit system:

- The pointer becomes 8 bytes.
    
- The `int` stays 4 bytes.
    
- **The Result:** The 8-byte pointer doesn't fit into the 4-byte `int`. Data gets truncated (cut off), the program loses the memory address, and it crashes.
---
