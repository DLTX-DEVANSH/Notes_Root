In computers data is stored in the form bits and bytes ( 1byte = 8 bits) 
A file that consists of exclusively  ACII characters in known as *text file* & all other formats are known as *binary file* .

for example :- 
```c
#include <stdio.h> 

int main()
{
	printf("hello, world\n");
	return 0;
}
``` 
`hello.c`

here hello.c is called a text file , each text character corresponds to a ASCII character and each ASCII character corresponds to a Byte . each line is also terminated by a `\n` line termination  
![[Pasted image 20251225140359.png ]]

For the computer to run this file ,it must be first converted into low level `machine instruction`  these instructions are then packed into a form called `Executable object program/file`
This compilation is performed by a `compiler driver` .

```bash
gcc hello.c -o hello
```

Lifecycle of compilation process 
![[Pasted image 20251225142445.png]]
[[GCC commands.pdf#page=1&selection=2,0,2,40|Commands for specific point in the process ]]

- `Preprocessing phase` : In this phase the preprocessor modifies the original C code into a modified file according to the preprocessing directives beginning by `#`
- `Compilation Phase` : the compiler translated *hello.i* into the actual [Assembly Code](https://github.com/DLTX-DEVANSH/CSAPP_Solutions_and_Source_Code/blob/main/Chapter%201/c_1_1/hello.s) 
- `Assembly Phase` : the assembler translates this assembly program into *Relocatable Object File* called as `hello.o` 
- `Linking Phase` : here all the object files are merged by the *linker* into a *Simple Executable file* hello.exe 

---
#### Execution of Program and Hardware Organization of Computer 

To run a command we use a shell `( BASH in UNIX )` . A shell is a *Command Line Interpreter* that waits for the user to write a prompt `(Command)` and the performs the command . if the first word of the command is not recognized by the shell , it assumes that it is the name of a program .
so we can run the program by typing 
```bash
linux> ./hello
```

---
#### Hardware Organization of Computer 
The Execution a program is not straight forward , it relies heavily on the muti layered hardware steps of computer 

![[Pasted image 20251231151136.png | 500]]
`A Simplified version of Hardware Organization of system`

*Buses:-*  these are electrical conduits (wires) that carry bytes of information to and from different components  . They are typically decided to carry chunks of bytes called **Words** . the number of bytes in a Word is called **Word Size** which can be 4 byte (32 bit) or 8 Byte (64bit) .

*I/O Devices:-* These are systems connection to external world . Each I/O device is connected to I/O Bus via a `Controller or Adapter` . the difference between the two is only that controller is a Chip soldered on the motherboard whereas adapter is installed on a slot in the motherboard .

*Main Memory:-* This is the temporary memory that hold both a program and data that it manipulates while the processor is executing the program. Physically, main memory consists of a collection of [Dynamic Random Access Memory (DRAM)](https://en.wikipedia.org/wiki/Dynamic_random-access_memory#Memory_cell_design) chips.

*Processor:* The *CPU* is engine that executes the instructions in main memory . It has a register called `Program Counter` that point to ( contains the address of ) a instruction in memory and updates the pointer often  . The processor appears to operate according to a very simple instruction model called `Instruction Set Architecture` . The operations revolve around main memory , register file *(The register file is a small storage device with multiple word sized resister each with a unique name* , and the ALU . these instructions are 
- Load
- Store 
- Operate 
- Jump

When we run the `./hello` program in the shell , the shell load the data in hello file from disk to main memory using a technique called `DMA (Direct Memory Access)` which  makes the data travels directly to main memory from disk directly without the involvement of Processor.

---

#### Caches and Memory Hierarchy

When the data is copied from main memory to the processor a lot of time is wasted (Overhead) . This slows the speed of work . physical laws state that `larger storage = Slower speed` and faster speed storage is expensive to make . *Register* is blazingly fast but stores few bytes , main memory is super slow ( comparatively ) but stores millions/billions of bytes . to bridge this gap hardware designers introduces a middle storage called *Cache Memory* . Cache is much faster than main memory but slower than register , but stores way more data than register but less the main memory . They serve as staging ground for the data to go from main memory to register . Cache can be further divided into more level based on speed and size as *L1 , L2 & L3 Cache* . L1 and L2 are implemented as [SRAM (Static Random Access Memory)](https://en.wikipedia.org/wiki/Static_random-access_memory#Design)  

>[!abstract] SRAM and DRAM
>>*SRAM (Static Random Access Memory):-* They are Super fast storage device directly on processor .This type of memory is made out of transistors and flip flops that can retain their state until the electricity is supplied , hence the name *static*
>>*DRAM(Dynamic Random Access Memory):-* they are fast ( slower than SRAM) , they are made out of capacitors that leak charge and needs constant charging from time to time and hence the name dynamic

Caches Exploit the fact of `Locality` which is the tendency of data and programs to access data faster from a specific region 

The Storage Devices are arranged in a hierarchy where the upper most section ( Lowest Level ) has the highest speed but lowest space and the highest Level has slowest speed and very high storage Where each level acts as the staging ground for the data from higher level to lower level of the current level . 
![[Pasted image 20260102050513.png | 600]]

---

#### Operating System and it's Management of Hardware 

Accessing the hardware directly is forbidden to any application program so Operating system , a software that sits between hardware and application software is responsible for protecting the hardware & providing Abstraction like virtual memory , process etc to provide application programs to use hardware .
![[Pasted image 20260102052027.png | 500]]

##### Processes 
The most important abstraction provided by the OS . when a program is compiled from text file to binary file , it has instructions directly written in binary for the CPU to perform `eg:- write data to RAM slot 0x005` . the issue here is what if that instruction directly destroys the CPUs other process  ? or simply is not possible ? If we were to run that program directly it would be very bad . so the operating system provides an abstraction called *Process* , which hides a lot of things from the program . it makes the program think that it has the entire memory and entire CPU for use but in reality it abstracts all the actual hardware details from the program 

>[!bug] Why do we need to abstract the Binary executable file ? 
>Let's say that the binary file has code that says `Use RAM slot 0x005` but this slot is already used by some other program so the MMU (Memory management Unit by OS ) and kernal tells the paging table to map the slot `0x005` to lets say `0x090` but the OS makes the program believe it used the slot it asked for . This is the reason that if you keep running the same program multiple times where we display pointer address using %p , it still displays the same RAM address .

In a *Uniprocessor system* to execute multiple processes concurrently[^1]  we use a mechanism called *context switching* , where we save the context ( register values , program counter etc) and switch to another process then switch back to original process using the saved context 
![[Pasted image 20260102064654.png | 450]]
This process switching is managed by the kernel[^2] of the Operating System 

[^1]: Concurrently means multiple programs whose instructions are interleaved within and seems to be executing parallelly 
[^2]: It is part of the operating system that always resides in the memory 

##### Threads
In modern Computers a process can have multiple execution units called *Threads* each running in the same context of process and sharing the same global variable/data . Threads are more efficient than process and it is easier to share data between threads . 

##### Virtual Memory
It is an abstraction provided to the process that makes feel like that it has entire memory just for itself . Each process has the same view of memory known as *Virtual address space*  
![[Pasted image 20260102070643.png | 490]]
`Linux Virtual Address Space`

the virtual address space seen by each process has well defined sections 
- *Code and data:* Code starts at beginning for each process and is followed by the data for the code 
- *Heap:* the next immediate slot is for run time heap which expands dynamically at runtime 
- *Shared Libraries:* in middle we have shared libraries like stdlib , math etc 
- *Stack:* At top we have stack that also grows dynamically
- *KVM:* At the peak we have kernel virtual memory reserved only for kernel 
##### Files 
A file is a sequence of bytes , nothing more nothing else .

---

#### Amdahl's Law 
This is simple observation made by *Gene Amdahl* that relates the overall speedup of a system to the part and degree of speedup of a specific system.
lets say that the old  time of system is $T_{old}$ . The fraction of the system that is sped up is $\alpha$
by a factor of $k$ so $$T_{new} = (1-\alpha)T_{old} + \frac{\alpha \cdot T_{old}}{k}$$

and the speedup S is $$S = \frac{T_{old}}{T_{new}} = \frac{1}{(1-\alpha) + \frac{\alpha}{k}}$$
special case when k = $\infty$ $$S_{\infty} = \frac{1}{1-\alpha }$$

---

#### Concurrency and Parallelism 
**Concurrency vs. Parallelism and Thread-Level Abstraction** Concurrency refers to a system dealing with multiple simultaneous activities, while parallelism is the use of concurrency specifically to increase system speed. At the highest level, **Thread-Level Concurrency** has evolved from simulated time-sharing on uniprocessors to true parallel execution on **multiprocessor systems**. This is achieved via **Multi-core processors** (multiple CPU cores on a single chip sharing memory interfaces) and **Hyperthreading** (Simultaneous Multi-Threading), which allows a single core to execute multiple control flows by duplicating architectural state (like registers) while sharing execution units. This hardware reduces the overhead of simulating concurrency and allows multi-threaded applications to exploit true parallel execution.

**Instruction-Level Parallelism (ILP)** At a lower level of abstraction, modern processors utilize **Instruction-Level Parallelism** to execute multiple instructions at once. Through **pipelining**, the actions required for an instruction are partitioned into steps, allowing the hardware to process different stages of multiple instructions simultaneously. Modern **superscalar processors** leverage this to sustain execution rates faster than one instruction per clock cycle, enabling programmers to write code that achieves higher throughput by optimizing for the processor's execution model.

**Single-Instruction, Multiple-Data (SIMD)** At the lowest level, **SIMD Parallelism** allows special hardware to execute a single instruction that performs operations on multiple data points simultaneously, such as adding pairs of floating-point numbers in parallel. This mode is primarily used to accelerate multimedia applications (image, sound, and video processing). While compilers can sometimes extract SIMD parallelism automatically, it is most reliably utilized by writing programs with special vector data types.