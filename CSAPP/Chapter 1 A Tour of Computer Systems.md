In computers data is stored in the form bits and bytes ( 1byte = 8 bits) 
A file that consists of exclusively  ACII characters in known as ***text file*** & all other formats are known as ***binary file*** .

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
- `Assembly Phase` : the assembler translates this assembly program into ***Relocatable Object File*** called as `hello.o` 
- `Linking Phase` : here all the object files are merged by the ***linker*** into a *Simple Executable file* hello.exe 

#### Execution of Program and Hardware Organization of Computer 

To run a command we use a shell `( BASH in UNIX )` . A shell is a *Command Line Interpreter* that waits for the user to write a prompt `(Command)` and the performs the command . if the first word of the command is not recognized by the shell , it assumes that it is the name of a program .
so we can run the program by typing 
```bash
linux> ./hello
```

#### Hardware Organization of Computer 
The Execution a program is not straight forward , it relies heavily on the muti layered hardware steps of computer 

![[Pasted image 20251231151136.png | 600]]
`A Simplified version of Hardware Organization of system`

**Buses:-**  these are electrical conduits (wires) that carry bytes of information to and from different components  . They are typically decided to carry chunks of bytes called **Words** . the number of bytes in a Word is called **Word Size** which can be 4 byte (32 bit) or 8 Byte (64bit) .

**I/O Devices:-** These are systems connection to external world . Each I/O device is connected to I/O Bus via a `Controller or Adapter` . the difference between the two is only that controller is a Chip soldered on the motherboard whereas adapter is installed on a slot in the motherboard .

**Main Memory:-** This is the temporary memory that hold both a program and data that it manipulates while the processor is executing the program. Physically, main memory consists of a collection of dynamic random access memory (DRAM) chips.

**Processor:-** The *CPU* is engine that executes the instructions in main memory . It has a register called `Program Counter` that point to ( contains the address of ) a instruction in memory and updates the pointer often  . The processor appears to operate according to a very simple instruction model called `Instruction Set Architecture` . The operations revolve around main memory , register file ***(The register file is a small storage device with multiple word sized resister each with a unique name*** , and the ALU . these instructions are 
- Load
- Store 
- Operate 
- Jump

